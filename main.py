'''
    ====================================================================================

    Name:                   Animesh Bhatt
    Class:                  XII-A
    CBSE Roll No.:          11698578
    Scholar Number:         9072/10
    Program Description:    Program to convert .txt files to .dat files and read them.
    Submitted to:           Resp. Sanjay Sharma sir
    For:                    CBSE Term-1 
    ====================================================================================
'''

#Modules used
import pickle #for working with binary files
from time import sleep # To add a pause

#Functions
def convert(filename,newfilename):
    try:
        with open(filename,'r') as F1:
            lines = F1.readlines()
            with open(newfilename,'wb') as F2:
                for i in lines:
                    pickle.dump(i,F2)
        print('Text file',filename, 'Converted to',newfilename,'successfully! \n')
        sleep(2)
    except FileNotFoundError:
        print('File not found, please try again')
        sleep(1)

def read(filename):
    try:
        F1 = open(filename,'rb')
        try:
            while True: 
                print('\n', pickle.load(F1))
        except EOFError:
            sleep(2)
            print('\n ========= File read successfully! ========= \n')
            sleep(1)
            
    except FileNotFoundError:
        print('File not found, please try again')
        sleep(1)

#Main Program

while True:
    print('========== Python Text to Binary file converter ==========')
    print('1. Convert a Text file to Binary file')
    print('2. Read Binary file')
    print('3. Exit.')
    ch = input('Enter your choice: 1-3: ')
    
    if ch == '1':
        filename = input('Enter the name of text file you want to convert: ')
        newfilename = input('Enter the name for converted file: ')
        convert(filename,newfilename)

    elif ch == '2':
        filename = input('Enter the name of Binary file you want to read: ')
        read(filename)
        
    elif ch == '3':
        print('Thankyou!')
        break
    
    else:
        print('Incorrect input, please try again...')
        sleep(2)

#End of the program.
