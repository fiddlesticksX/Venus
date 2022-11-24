####################################
# SERVICES
####################################
import os
import time
import sys
def clear():
    os.system('cls')
score = 0
clear()
####################################
# TOPICS
####################################
# Europe (local)
AAA_TITLE = 'EUROPE'
AAA_TOTAL = '5'
AAA_LOCAL = 'local'
AAA_Q1 = 'Is Paris the capital of France?'
AAA_B1 = True
AAA_Q2 = 'Does Switzerland speak Italian?'
AAA_B2 = True
AAA_Q3 = 'Is Europe a Continent?'
AAA_B3 = True
AAA_Q4 = 'Is Europe the largest Continent?'
AAA_B4 = False
AAA_Q5 = 'Does every European country use Euros?'
AAA_B5 = False
####################################
# CONSOLE INTERFACE
####################################
# general console interface
def ci_mainmenu():
    print('---VENUS_EDUCATIONAL_PROGRAM.py--------------')
    print('        1. Start Learning')
    print('        2. About this Program')
    print('        0. Terminate this Program')
    print('---------------------------------------------')
def ci_optionmenu():
    print('---TOPICS------------------------------------')
    print(f'1. {AAA_TITLE} {AAA_TOTAL}Qs ({AAA_LOCAL})')
    print('2. Not Avaliable')
    print('3. Not Avaliable')
    print('0. Main Menu')
    print('---------------------------------------------')
def ci_aboutprogram():
    print('---ABOUT-------------------------------------')
    print('Programmed by Foot')
    print('Console Interface designed by Foot')
    print('Local Quizes by Foot')
    print('version 0.9, Pre-Build')
    print('---------------------------------------------')
# AAA Console Interface
def ci_AAA_A():
    print('---QUIZ-------------------------------------------------------------------------------------------')
    print(f'This is a Quiz on {AAA_TITLE}!, You only have to Answer {AAA_TOTAL} Questions! Good Luck...')
    print('1. Start Quiz')
    print('0. Exit to Menu')
    print('--------------------------------------------------------------------------------------------------')
def ci_AAA_Q1():
    print('---QUIZ-------------------------------------------------------------------------------------1/5---')
    print(f'Q. {AAA_Q1}')
    print('--------------------------------------------------------------------------------------------------') 
def ci_AAA_Q2():
    print('---QUIZ-------------------------------------------------------------------------------------2/5---')
    print(f'Q. {AAA_Q2}')
    print('--------------------------------------------------------------------------------------------------')
def ci_AAA_Q3():
    print('---QUIZ-------------------------------------------------------------------------------------3/5---')
    print(f'Q. {AAA_Q3}')
    print('--------------------------------------------------------------------------------------------------') 
def ci_AAA_Q4():
    print('---QUIZ-------------------------------------------------------------------------------------4/5---')
    print(f'Q. {AAA_Q4}')
    print('--------------------------------------------------------------------------------------------------') 
def ci_AAA_Q5():
    print('---QUIZ-------------------------------------------------------------------------------------5/5---')
    print(f'Q. {AAA_Q5}')
    print('--------------------------------------------------------------------------------------------------')   
# ci_AAA_B is in PROGRAM   
####################################
# PROGRAM
####################################

# Main Menu
def mainmenu():
    clear()
    ci_mainmenu()
    ci_mainmenuinp = input('Pick an Option: ')
        # Quiz Library
    if ci_mainmenuinp == '1':
        clear()
        ci_optionmenu()
        ci_optionmenuinp = input('Pick a Quiz: ')
        # QUIZ AAA
        if ci_optionmenuinp == '1':
            clear()
            score = 0
            ci_AAA_A()
            ci_aaa_ainp = input('Pick an Option: ')
            if ci_aaa_ainp == '1':
                clear()
                ci_AAA_Q1()
                answer = input('y/n: ')
                if answer == 'y':
                    clear()
                    score += 1
                else:
                    clear()
                ci_AAA_Q2()
                answer = input('y/n: ')
                if answer == 'y':
                    clear()
                    score += 1
                else:
                    clear()
                ci_AAA_Q3()
                answer = input('y/n: ')
                if answer == 'y':
                    clear()
                    score += 1
                else:
                    clear()                   
                ci_AAA_Q4()
                answer = input('y/n: ')
                if answer == 'y':
                    clear()
                elif answer == 'n':
                    clear()
                    score += 1
                ci_AAA_Q5()
                answer = input('y/n: ')
                if answer == 'y':
                    clear()
                elif answer == 'n':
                    clear()
                    score += 1
                def ci_AAA_B():
                    clear()
                    print('---QUIZ-------------------------------------------------------------------------------------------')
                    print(f'You have completed the quiz on {AAA_TITLE}')
                    print(f'Your Score is {score} out of {AAA_TOTAL} Questions')
                    print('--------------------------------------------------------------------------------------------------')
                ci_AAA_B()
                ci_aaa_binp = input('Press Enter to go back to the Main Menu')
                mainmenu()
            elif ci_aaa_ainp == '0':
                mainmenu()
            else:
                print('That is not an option')
                time.sleep(2)
                mainmenu()
        elif ci_optionmenuinp == '2':
            # ADD QUIZ 'AAB' HERE
            mainmenu()
        elif ci_optionmenuinp == '3':
            # ADD QUIZ 'AAC' HERE
            mainmenu()
        elif ci_optionmenuinp == '0':
            mainmenu()
        else:
            print('That is not an Option!')
            time.sleep(2)
            mainmenu()
    elif ci_mainmenuinp == '0':
        sys.exit()
    # this is the About Menu, If you add any mods or quizes you can add yourself onto the about page
    elif ci_mainmenuinp == '2':
        clear()
        ci_aboutprogram()
        input('Press Enter to Exit')
        mainmenu()
    else:
        mainmenu()
    # this kills the program
mainmenu()
