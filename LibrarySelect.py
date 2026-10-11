# LibrarySelect.py <---- fle name and module name
import mysql.connector as msql

def readrecord():
    while True:
        try:
            # Establish connection
            con = msql.connect(
                host="localhost",
                user="root",
                password="Vinay123",
                database="libraryproject"
            )
            # Using buffered=True allows cur.rowcount to work accurately for SELECT queries
            cur = con.cursor(buffered=True) 
            
            print()
            bno = int(input("Enter the Book number(bno) to see the details: "))
            
            sq = "select * from library where bno=%s"
            cur.execute(sq, (bno,))
            
            # Now rowcount will accurately reflect if rows exist
            if cur.rowcount == 0:
                print("There is no book found with this book number.")
            else:
                # Print Table Headers
                metadata = cur.description
                print("-" * 40)
                for record in metadata:
                    print(record[0], end="\t")
                print()
                print("-" * 40)
                
                # Fetch and print the records
                records = cur.fetchall()
                for row in records:
                    for item in row:
                        print(item, end="\t")
                    print()
                print("-" * 40)
            
            # Clean up cursor and connection
            cur.close()
            con.close()
            
            # Ask user to continue
            ch = input("Do you want another Book details (yes/no): ")
            if ch.lower() == "no":
                print("Thanks for using this program!")
                break
                
        except msql.DatabaseError as db:
            print(f"Problem in the database: {db}")
            break # Break or handle gracefully instead of infinite recursion
        except ValueError:
            print("Please enter a valid numeric Book Number.")


