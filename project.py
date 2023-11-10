import random
import csv
import re
import tabulate
import pyfiglet
import sys
import time

from tabulate import tabulate
from pyfiglet import Figlet
from termcolor import colored, cprint

ctime = []                      # create a list of dicts of countries and times                    
with open("country_times.csv") as file:   
    reader = csv.DictReader(file)
    for row in reader: 
        ctime.append(row)

terminal_width = 133   # terminal full screen width


  
def quiz(ctime):
    """
    Asks 5 questions, compares with right answer and prints out score in the end.      

    Args:
        ctime (list of dict): list containing time diff of various countries
    
    Vars:
        t (str) - time
        c1 (str)- country 1
        c2 (str)- country 2
        apm (str)- am/pm
        ans - correct answer
        inp - input from user
        resp - corrected response 
        score - your score
        
    """
    separator('^','blue')
    
    i = 0
    score = 0
    cntrys = [line['country'] for line in ctime]    # pythonic way
    
    print(colored('Easy(e)',color='cyan'),'mode or',colored('hard(h)',color='yellow'),'mode ?\n')
    
    while True:
        try: 
            mode = (input()).lower()
            if mode not in ['e','easy','h','hard']:
                raise ValueError()
        except ValueError: 
            print('Wrong choice')
            continue
        else: 
            break
   
    
    while i<5:              #  you get 5 questions
        
        # print('\n')
        time.sleep(1)
        separator()
        # print('\n')
        
        rand = random.sample(cntrys,2)      # get 2 random (but different) countries. sample()- without replacement
        c1 = rand[0]           
        c2 = rand[1]
        
        
        if mode in ['e','easy']:
            t = str(random.randint(1,12))+":00"
        elif mode in ['h','hard']:    
            h = str(random.randint(1,12)) #+":00"           # get random time
            min = random.choice(['00','30'])
            t = h+":"+min
            
               
        apm = random.choice(['am','pm'])
        
        ans,t1,t2 = right_ans(c1,c2,t,apm,ctime)
       
        # print(f"Time in {c2} is {ans}")
        print(colored(f"\n  Q{i+1}\n",color='magenta',attrs=['bold']))
        print("If it is", colored(t,color='cyan'),colored(apm,color='cyan'),"in", colored(c1,color='yellow'),", what is the time in",colored(c2,color='yellow'),"??\n\n")
        while True:
            try: 
                inp = input()
                # inp = input(f"Q{i+1}.If it is {t} {apm} in {c1}, what is the time in {c2} ??\n")
                
                # to exit the program
                if inp in ['exit','E','e']:
                    sys.exit()
                    
                resp = check(inp) # Convert response into correct format
                break
            except ValueError: 
                print(("Time is of wrong format\n"))
                continue
        # print(resp)
        
        
        #-------Checking whether answer is right-------#
        f = Figlet(font='slant') 
        
        i+= 1
        if resp != ans:
            print(colored(f.renderText('WRONG'),'red')) 
            print("   Try again\n")
            print(colored("Hint:",color='cyan'),f"The time difference of {c1} is {t1}, and the time difference of {c2} is {t2}\n")
            inp2 = input()
            resp2 = check(inp2)
            if resp2 != ans:
                print(f"\nTime in {c2} is {ans}")
            else: 
                print(colored(f.renderText('RIGHT!!'),'green')) 
                print(colored("Well done 👍",color='green',attrs=['bold']))
            continue
        else:
            print(colored(f.renderText('RIGHT !!'),'green')) 
            print(colored("Well done 👍",color='green',attrs=['bold']))
            score+= 1
            continue
    
    time.sleep(2)
    
    separator('*','yellow')
    print('\n')
    
    f2 = Figlet(font='big')  # font 2
    print(colored(f2.renderText("Score: \n"),'white'))
    print(colored(f2.renderText(f"{score}"),'blue'),colored(f2.renderText("/5"),'white'))
    
    f3 = Figlet(font='standard')
    if score == 5:
        print(colored(f2.renderText('Excellent !!'),color='blue'))
        print('   😀😀😀😀😀😀😀😀')
    elif score>=3:
        print(colored(f2.renderText('Well done'),color='magenta'))
        print('   👍👍👍👍👍👍👍👍')
    
    print('\n')
    separator('*','yellow')
    separator('*')
    separator('*','yellow')
    print('\n')

           
    
def right_ans(c1,c2,t,apm,ctime):
    """Finds the right answer using given inputs
    
    Args:
        c1 (str): country 1
        c2 (str): country 2
        t (str): random time
        apm (str): 'am'/'pm'
        ctime (list of dict): list containing time diff of various countries
    
    Returns:
        (str): string containing the right answer in the right format
        
    Vars: 
        td (float) - time difference
        a (float) - hr part of time t; is modified to include min as decimal
        b (int) - min part of time t
        newt (float) - new time
    """
    for row in ctime:
        if row['country'] == c1:
            t1 = row['timediff'].lstrip()
        if row['country'] == c2:
            t2 = row['timediff'].lstrip()

    td = time_diff(t1,t2)   # float type. Can be 4.5 etc.
    # print(f"**{td}**")
    
    a,b = t.split(":")
    a = int(a)
    b = int(b)
    a = a + b/60        # for when time is 8:30 etc. (contains ':30')
    
    if a.is_integer():   # to get right of the '.0' if a = 3.0
        a = int(a)

    if a == 12 and apm == 'am':  # midnight
        a = 0
    elif a == 12.5 and apm == 'am': # 12.30 am == 0.5
        a = 0.5
    elif a == 12 and apm == 'pm': # noon
        a = 12 
    elif a == 12.5 and apm == 'pm': # 12.30 pm == 12.5
        a = 12.5
    elif apm == 'pm':  # to convert pm to 24-hr format
        a+= 12
    
    newt = a + td
    # print(newt)
    
    ##---------*---------## 
    # overflow
    
    if newt>24:
        newt = newt - 24
    elif newt<0:
        newt = 24 + newt
    
    ##---------*---------## 
    # re-convert
    
    m = ':00'
    
    if newt == 0:  # midnight
        h = 12
        ap = 'am'
    elif newt == 12: # noon
        h = 12
        ap = 'pm'     
    elif newt > 12:  # 13.00-23:00
        h = newt-12
        if h == 0.5:  # 12.30 pm
            h = 12
            m = ':30'
        elif h%1 == 0.5:
            m = ':30'
        ap = 'pm'
    else:
        h = newt
        if h == 0.5:  # 12.30 am
            h = 12
            m = ':30'
        if h%1 == 0.5:
            m = ':30'
        ap = 'am'
        
    # if h%1 == 0.5:   
    #     m = ':30'  
    # else:
    #     m = ':00'
    
    return str(int(h))+m+" "+ap, t1, t2



    
def time_diff(t1,t2):           
    """calculate time diff between two times

    Args:
        t1 (str): time in hh:mm format
        t2 (str): time in hh:mm format

    Returns:
        td (float): time diff btw t2 and t1
    """
    h1,m1 = t1.split(':')
    h1 = int(h1)
    m1 = int(m1)
    
    if m1 != 0:      #  if timediff is 5hr 30min (5:30) for eg.  
        h1+= 0.5
        
    h2,m2 = t2.split(':')
    h2 = int(h2)
    m2 = int(m2)
    
    if m2 != 0:
        h2+= 0.5
    
    td = h2-h1
    return td
        

def check(inp):  
    """
    check validity of user's input using regex

    Args:
        inp (str): the input given by user

    Raises:
        ValueError: if input is of wrong format

    Returns:
        resp (str): input corrected to the standard format
        
    """
    inp = inp.strip()
    if match:= re.search(r'([0-9]|1[0-2])([:|.][3,0]0)? ?([a|p]m)',inp,re.IGNORECASE):
        # can read 12am,12AM,12:00am,12.00AM
        h = match.group(1)
        apm = (match.group(3)).lower()
        m = match.group(2) if match.group(2) else '00'
        m = m.replace(':','').replace('.','').strip()
        resp = f"{h}:{m} {apm}"
        return resp
    else:
        raise ValueError
        
   
   
def display(ctime):
    """
    Display the time differences of various countries in the form of a table.

    Args:
        ctime (list of dict): list containing time diff of various countries
    """
    
    separator(char='*', color='magenta')
    
    split_pnt = 5   # wrapping table side by side, for better readability
                    # in [a:b], 2nd int,i.e. b, is inclusive

    table1 = (tabulate(ctime[:split_pnt], tablefmt="grid"))
    table2 = (tabulate(ctime[split_pnt:], tablefmt="grid"))
    lines1 = table1.split('\n')
    lines2 = table2.split('\n')
    max_lines = max(len(lines1),len(lines2))
    
    for i in range(max_lines):
        row1 = lines1[i] if i<len(lines1) else ' '*len(lines1[0])
        row2 = lines2[i] if i<len(lines2) else ' '*len(lines2[0])
        print(row1+"        "+row2)
    
    print('\n')
    print(colored(" NOTE:",color='yellow'),"The \'West,SE,etc.\' means what part of the country the city is located. NE means North-East, SE means South-East.")
    
    print('\n')
    separator('=','magenta')
    print('\n')


def separator(char='-',color='white'):
    length = 80
    print(colored(char*terminal_width,color=color))

def center_text(text):
    spaces = (terminal_width - len(text)) // 2
    return " "*spaces + text
    
def main():
    
    separator('=','blue')
    print(colored(center_text('Welcome to Time Zone Teacher'),color='cyan',attrs=['bold']))
    separator('=','blue')
    
    # print(colored(tabulate([['Welcome to Time Zone Teacher']], tablefmt='fancy_grid'),color='cyan',attrs=['bold']))
    
    while True:
        s = input('\n What do you want to do?\n1.Display time zones\n2.Quiz me!!\n\n')
        if s in ['exit','e','E']:
            sys.exit()
        s = int(s)
        match s:
            case 1:
                display(ctime)
                break
            
            case 2:
                print("\nAnswer these 5 questions to test your knowledge!\n")
                quiz(ctime)  
                break
                
            case _:
                print("No such option. Enter again")
                continue
            


if __name__ == "__main__":
    main()