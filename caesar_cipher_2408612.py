#program to encrypt and decrypt text using caesar method.

import os.path#importing os.path to use in is_file() function
'''
    here import os.path is used to check if the entered file name exists in given
    path. it will return true if file found and false if file name not found.
'''

#declaring letters as global variable so it can be accessed by both encrypt() and decrypt() function
letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num_letter=len(letters)#finding lenght of letters

#declaring main() function as a base of whole program
def main():
    '''
        main() function is used as base of program. All the other function will run or be called once the main()
        function is called. Major use of this function is for running welcome() function and to know if the user
        want to keep runnig the program or end the program.
    '''
    welcome()#calling welcome() function
    enter_message()#calling enter_message() function
    
    while True:#using loop to ask user if they want to continue to use the program or stop the program
        another_message=input("\nWould you like to encrypt or decrypt another message? (y/n):").lower()
        if(another_message.lower()=="y"):
            enter_message()#if the input is 'y' then calling enter_message() function
        elif(another_message.lower()=="n"):
            print("\n Thank You for using the program, goodbye!")
            break#if the input is 'n' then with the help of break program stops.
        else:
            print("Invalid Input")#if the input is invalid then program keeps asking for input unless it is valid.

#declaring welcome() function
def welcome():
    '''
        welcome() function is only called at beggining of the program to show the welcome message
        we want the user to see, what this program is used for.
    '''
    print("Welcome to the Caesar Cipher.")
    print("This Program is used for encrypting and decrypting the text using Caesar Cipher.\n")

#declaring enter_message() function
def enter_message():
    '''
        enter_message() function takes the input from the user as e if encrypt and d if decrypt.
        as per the user input the following function is called. this function also checks if the user
        want to perform encryption or decryption in console or file.
    '''
    
    while True:#using loop to ask user for mode and keep asking till the input is valid
        choice=input("Would you like to encrypt(e) or decrypt(d)?:").upper()
        if(choice=='E' or choice=='D'):
            break
        else:
            print("Invalid Mode")
            
    if(choice=="E"):#run the code if mode is encrypt
        file_console=message_or_file()#calling message_or_file() function
        
        if(file_console=='C'):#using conditional statement to check where the user want to encrypt or decrypt text in console or file.
            print("\n \t ENCRIPTION MODE")
            textToConvert=input("What message would you like to encrypt:").upper()
            
            while True:#using loop to ask for valid shift number
                shift_num=int(input("What is the shift number(0-25):"))
                if(shift_num<=25 and shift_num>=0):
                    break
                else:
                    print("Invalid Shift")
            print(encrypt(textToConvert,shift_num))#calling encrypt() function in console
        else:
            file_name=input("\nEnter a file name:")#asking for file name
            file_name=is_file(file_name)#checking if the file exists using is_file() function
            process_file(file_name,choice)#calling process_file() function
            
    elif(choice=="D"):#run the code if mode if decrypt
        file_console=message_or_file()#using conditional statement to check where the user want to encrypt or decrypt text in console or file.
        
        if(file_console=='C'):#run decrypt() function in console.
            print("\n \t DECRIPTION MODE")
            textToConvert=input("What message would you like to decrypt:").upper()
            
            while True:#using loop to ask for valid shift number
                shift_num=int(input("What is the shift number(0-25):"))
                if(shift_num<=25 and shift_num>=0):
                    break
                else:
                    print("Invalid Shift")
            print(decrypt(textToConvert,shift_num))#calling decrypt() function in console.
        else:
            file_name=input("Enter a file name:")#asking for file name
            file_name=is_file(file_name)#checking if file exists or not by calling is_file() function
            process_file(file_name,choice)#calling process_file

#declaring encrypt() function
def encrypt(text,shiftINnumber):
    '''
        as the name suggests encrypt() function is used to encrypt the text. it takes two parameter. one is text
        which holds the text that needs to be encrypted and another is shiftINnumber that takes shift number.
        this function will access each letter of text and shift according to shift number. example if the first letter of text
        is 'a' and shiftnumber is 2 then a will be changed to 'c' as shifting 'a' by two times it becomes 'c'. and the letter
        is concatinated to empty string which is declared at first.
    '''
    encrypted_text=""
    for letter in text:#using for loop to take each letter in text and encrypt
        index=letters.find(letter)
        if(index==-1):
            encrypted_text += letter
        else:
            new_index=index + shiftINnumber
            if(new_index >= num_letter):
                new_index -= num_letter
            encrypted_text += letters[new_index]#concatinating the encrypted letter
    return 'e',encrypted_text, shiftINnumber

#declaring decrypt() function
def decrypt(text,shiftINnumber):
    '''
        decrypt() function is used to decrypt the text. it takes two parameter one is text and another is shiftINnumber
        it works on same principle of encrypt but the only difference is during shift inplace of going front it goes backward.
        example in encrypt() if the letter is d and shift is 2 then the letter will be f but in decrypt() d count will go backward
        i.e. it becomes b. 
    '''
    decrypted_text=""
    for letter in text:#using for loop to take each letter in text and decrypt 
        index=letters.find(letter)
        if(index==-1):
            decrypted_text += letter
        else:
            new_index=index - shiftINnumber
            if(new_index < 0):
                new_index += num_letter
            decrypted_text += letters[new_index]#concatinating the decrypted letter
    return 'd',decrypted_text,shiftINnumber

#declaring message_or_file() function
def message_or_file():
    '''
        this function message_or_file() is used only to ask user if they want to run the
        encryption and decryption in console or the file itself. it will take the input as 'F' for file
        and 'C' for console. it the input is other then this it will throw invalid and keep askig till the
        input is correct.
    '''
    while True:
        file_console=input("Would you like to read from a file(f) or the console(c)?").upper()
        if(file_console=='F' or file_console=='C'):
            return file_console
            break
        else:
            print("Invalid Input")

#declaring process_file() function
def process_file(fileName,mode):
    '''
        this function is called if the user want to encrypt or decrypt the text that is stored in file.
        it has two parameterr one is file name through which the data to encrypt or decrypt is taken and
        mode which tell if we want run encrypt mode or decrypt mode.

        according to what mode(e/d) is entered, conditional statement will perform following statements. simply
        file is opend in reading mode then loop is used to access single line at a time. then that line is passed as parameter of
        encrypt() or decrypt() function. as the function returns the output it is stored to list.

        and calls write_message() function, list as parameter to store the encrypted or decrypted items in another file.
    '''
    while True:
        shift_num=int(input("What is the shift number(0-25):"))#asking shift number to perform encrypt or decrypt
        if(shift_num<=25 and shift_num>=0):
            break
        else:
            print("Invalid Shift")
    encrypt_decrypt_list=[]
    if(mode=='E'):
        with open(fileName,'r') as file:
            for line in file:
                line=line.upper()
                encrypt_decrypt_list.append(encrypt(line,shift_num)[1])
    else:
        with open(fileName,'r') as file:
            for line in file:
                line=line.upper()
                encrypt_decrypt_list.append(decrypt(line,shift_num)[1])
    return write_message(encrypt_decrypt_list)

#declaring is_file() function
def is_file(fileName):
    '''
        is_file() function is used to check if the entered file name exists in given path or not.
        till the file is not found the loop will keep asking for file name through which we can
        take texts to encrypt or decrypt text.
    '''
    if(os.path.exists(fileName)):
        fileName=fileName
    else:
        while os.path.exists(fileName) != True:
            print("Invalid Filename")
            fileName=input("Enter a filename:")
    return fileName

#declaring write_message() function
def write_message(messageINfile):
    '''
        write_message() function is used to write the encrypted or decrypted text which was taken from file to
        another file. it simply take single parameter that is the output from list in file_process() function.
        then using loop one item of list is accessed at a time and stored to new file.
    '''
    output_file=input("Output written to:")
    with open(output_file,'w')as file1:
        for encrypt_decrypt in messageINfile:
            file1.write(encrypt_decrypt)
               
main()#calling our main function

