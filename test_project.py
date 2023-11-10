# don't test for the sake of testing
# what tests would actually be useful for your project??
# instead of assert, you can simply print to test the output of a function

import csv
from project import time_diff, right_ans, check
from project import ctime

from termcolor import colored, cprint
from pyfiglet import Figlet



def test_time_diff():
    assert time_diff('-4:00','+2:00') == 6
    assert time_diff('+2:00','-1:00') == -3
    assert time_diff('-3:00','-2:00') == 1
    assert time_diff('-4:00','-5:00') == -1
    assert time_diff('+1:00','+4:00') == 3
    assert time_diff('+4:00','+2:00') == -2
    
    assert time_diff('-2:00','-2:00') == 0
    assert time_diff('+1:00','+1:00') == 0
    assert time_diff('+1:00','+5:30') == 4.5    
    assert time_diff('+5:30','+2:00') == -3.5

def test_right_ans():
    print(right_ans('France','Japan','7:00','am',ctime)) #'3:00pm'
    print(right_ans('Mexico','Japan','11:00','pm',ctime)) #'2:00 pm'
    print(right_ans('Australia (Sydney-SE)','Canada (Montreal-SE)','2:00','am',ctime)) #'10:00 am'
    print(right_ans('Egypt','LA (US West)','3:00','pm',ctime)) #'5:00 am'
    print(right_ans('Germany','India','7:00','am',ctime)) #'11:30 am'
    print(right_ans('New York (US East)','India','7:00','pm',ctime)) #'5:30 am'
    print("\n")
    print(right_ans('India','France','5:00','pm',ctime)) #'12:30 pm'
    print(right_ans('India','LA (US West)','1:00','am',ctime)) #'11:30 am'
    print(right_ans('Pakistan','India','12:00','am',ctime)) #'12:30 am'
    print(right_ans('Japan','Mexico','3:00','am',ctime)) #'12:00 pm'
    print("\n")
    print(right_ans('China (Beijing-NE)','LA (US West)','3:00','pm',ctime)) #'11:00 pm'
    print(right_ans('New York (US East)','Japan','1:00','pm',ctime))  #'3:00 am'
    print(right_ans('UK','Mexico','8:00','am',ctime)) #'2:00 am'
    print(right_ans('Saudi Arabia','Mexico','8:00','am',ctime)) #'11:00 pm'
    print('\n')
    print(right_ans('India','Pakistan','12:30','am',ctime)) #'12:00 am'
    print(right_ans('Canada (Montreal-SE)','France','12:00','pm',ctime)) #'6:00 pm'
    print(right_ans('Spain','Japan','12:00','pm',ctime)) #'8:00 pm'
    print('\n')
    print(right_ans('Qatar','Australia (Sydney-SE)','4:30','pm',ctime)) #'12:30 am'
    print(right_ans('Monaco','Mexico','1:30','pm',ctime)) #'6:30 am'
    print(right_ans('LA (US West)','Australia (Sydney-SE)','10:30','pm',ctime)) #'5:30 pm'
    print(right_ans('Australia (Sydney-SE)','LA (US West)','12:30','am',ctime)) #'5:30 am'
    print(right_ans('India','LA (US West)','8:30','am',ctime)) #'7:00 pm'

def test_check():
    print(check('6pm'))
    print(check('3:00PM'))
    print(check('11.30am'))
    print(check('12:00 am'))
    print(check('7.00AM'))
    print(check('10pm'))
    print(check('12 pm'))

# test_time_diff()
# test_right_ans()
test_check()

i=1
t = '7:00'
apm = 'am'
c1 = 'China'
c2 = 'Qatar'
# print(colored(f"Q{i+1}.",color='red',attrs=['bold']),"If it is", colored(t,color='cyan'),colored(apm,color='cyan'),"in", colored(c1,color='yellow'),", what is the time in",colored(c2,color='yellow'),"??\n")
print('\n')
print(colored(f"Q{i+1}",color='magenta',attrs=['bold']))
print("If it is", colored(t,color='cyan'),colored(apm,color='cyan'),"in", colored(c1,color='yellow'),", what is the time in",colored(c2,color='yellow'),"??\n\n")

print(colored('Easy(e)',color='cyan'),'mode or',colored('hard(h)',color='yellow'),'mode ?')

# terminal_width = 133    

def separator(char='-',color='white'):
    length = 80
    print(colored(char*terminal_width,color=color))
    
def center_text(text):
    spaces = (terminal_width - len(text)) // 2
    return " "*spaces + text

# separator(color='blue')

# print(colored(f"Q{i+1}",color='magenta'))


# f3 = Figlet(font='standard')
# score =5
# if score == 5:
#     print(colored(f3.renderText('Excellent !!'),color='blue'),'   😀😀😀😀😀😀😀😀')
# elif score>=3:
#     print(colored(f3.renderText('Well done'),color='magenta'),'   👍👍👍👍👍👍👍👍')

# while True:
#     try: 
#         mode = (input()).lower()
#         if mode not in ['e','easy','h','hard']:
#             raise ValueError()
#     except ValueError: 
#         print('Wrong choice')
#         continue
#     else: 
#         break
        

