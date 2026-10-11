#LibraryMainproject.py
from LibraryMenu import menu 
from LibraryDelete import deleterecord
from LibraryUpdate import updaterecord
from LibrarySelect import readrecord
from LibrarySelectAll import readallrecord
from LibraryAdd import addbook
while(True):
    menu()
    try:
        ch=int(input("enter your choice: "))
        match(ch):
            case 1:
                    addbook()
                    
            case 2:
                    deleterecord()
            case 3:
                    updaterecord()
            case 4:
                    readrecord()
            case 5:
                    readallrecord()
            case 6:
                   print("Thnx for Using These Program")
                   break
            case _:
                    print("Your selection of option is Invalid pls try again---:")
                    break

    except ValueError:
        print("Don't Enter strs alnums and symbols for Integer Choice:")
