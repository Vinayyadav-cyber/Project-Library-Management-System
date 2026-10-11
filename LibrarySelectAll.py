# LibrarySelectAll.py <---- fle name and module name
import mysql.connector as msql

def readallrecord():
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
           
            sq = "select * from library"
            cur.execute(sq)
            
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
            
                
        except msql.DatabaseError as db:
            print(f"Problem in the database: {db}")
             # Break or handle gracefully instead of infinite recursion
        except ValueError:
            print("Please enter a valid numeric Book Number.")


