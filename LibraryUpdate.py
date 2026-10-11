#LibraryUpdate.py <--- file name and module name
import mysql.connector as msql
def updaterecord():
    while(True):
        try:
            con=msql.connect(host="localhost",user="root",password="Vinay123",database="libraryproject")
            cur=con.cursor()
            print("-"*70)
            print("Enter the Details You want Update")
            print()
            bookno=int(input("Enter Book Number (bno) to Update details: "))
            print()
            print("Want you want to update press:")
            print("1.Book Name: ")
            print("2.Book Price: ")
            print("3.Book Publication : ")
            rs=int(input("Enter Your Choice (1-3): "))
            print()
            match(rs):
                case 1:
                        bname=input("Enter Updated Name of Book: ")
                        sq="update library set bname=%s where bno=%s"
                        cur.execute(sq,(bname,bookno))
                case 2:
                        bprice=float(input("Enter Updated Price of Book: "))
                        sq="update library set price=%s where bno=%s"
                        cur.execute(sq,(bprice,bookno))
                case 3:
                        pub=input("Enter Updated Book  publication : ")
                        sq="update library set  publication=%s where bno=%s"
                        cur.execute(sq,(pub,bookno))
                case _:
                        print("You enter Invalid Option:")
            con.commit()
            print("-"*70)
            if(cur.rowcount==0):
                print("There is no student found there:")
            else:
                print("{} record update successfully--verify".format(cur.rowcount))
            print("="*70)

            #if user Want to update another record so
            ch=input("Do you want to Update another Record (yes/no):")
            if(ch.lower()=="no"):
                 print("Thnx for using these program :")
                 break



        except msql.DatabaseError as db:
            print("Problem in your database",db)

