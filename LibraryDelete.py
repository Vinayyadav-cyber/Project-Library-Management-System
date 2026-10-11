
#LibraryDelete.py <---- file name and module name
import mysql.connector as msql
def deleterecord():
    while(True):
        try:
            con=msql.connect(host="localhost",user="root",password="Vinay123",database="libraryproject")
            cur=con.cursor()
            print("-"*70)
            sno=int(input("Enter Book number you want to delete record: "))
            print("-"*70)
            sq="delete from library where bno=%s"
            cur.execute(sq ,(sno,))
            con.commit()
            print("-"*70)
            if(cur.rowcount==0):
                print("Invalid number no record found:")
            else:
                print("{} record delete successfully---verify".format(cur.rowcount))
            print("-"*70)
            print("-"*50)
            ch=input("Do you want to delete Another Book details(yes/no)")
            if(ch.lower()=="no"):
              print("Thnx for using these program:")
              break

        except msql.DatabaseError as db:
            print("Problem in the database",db)

