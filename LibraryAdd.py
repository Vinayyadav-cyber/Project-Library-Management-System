#LibraryAdd.py-----File Name and Module Name
import mysql.connector as mqcon
def addbook():
    while(True):
        try:
            con=mqcon.connect(host="localhost",user="root",password="Vinay123",database="libraryproject")
            cur=con.cursor()
            print("-"*50)
            bno=int(input("Enter Book Number:"))
            bname=input("Enter Book Name:")
            price=float(input("Enter Book Price:"))
            pub=input("Enter publication Name:")
            bd=(bno,bname,price,pub)
            sq=("insert into library values(%s,%s,%s,%s)")
            cur.execute(sq,(bd))
            con.commit()
            print("{} Book details saved successfully:".format(cur.rowcount))
            print("-"*50)
            ch=input("Do you want to enter another Book details(yes/no)")
            if(ch.lower()=="no"):
                print("Thnx for using these program:")
                break



        except mqcon.DatabaseError as db:
            print("Problem in the database: ")
        except ValueError:
            print("Don't Enter strs alnums and symbols for Integer Choice:")

#main program
