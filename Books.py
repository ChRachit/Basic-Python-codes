#Database for Books
#Problem at choice 2 and 3 at line 33 and 47
import sqlite3
Bookstore = sqlite3.connect("BookStore.db")
curs = Bookstore.cursor()
sql = "CREATE TABLE IF NOT EXISTS books(title TEXT NOT NULL, author , price FLOAT);" # Updated line 1
curs.execute(sql) #Executed only once
while True:
    #prompt for intented operation
    choice = int(input("Enter: " +  "\n 1: for Insertion" + "\n 2: for Deletion " + "\n 3: for Updation " + "\n 0: for exit \n"))
    if choice == 1:
        #for inserting a new record
        insertion = "INSERT INTO books(title, author, price) VALUES(?,?,?);"
        tit = input("Enter title: ")
        auth = input("Enter author: ")
        prc = int(input("Enter price: "))
        
        try:         
            curs.execute(insertion, (tit.title(), auth.title(), prc))
            Bookstore.commit()
            print("Records added!")
        
        except:
            print("error in operation.")
            Bookstore.rollback()
            
    if choice == 0:
        #for exiting the loop
        Bookstore.close()
        print("Thank You!")
        break

    elif choice == 2:
        #for deletion of record
        #here the code runs without any problem but record isn't deleted from the database
        record = input("Title of the Book you want to delete: ")
        try:
            curs.execute("DELETE FROM books WHERE title='{}';".format(record)) # Updated line 2
            Bookstore.commit()
            print(" deleted successfully!")

        except:
            print("error in operation.")
            Bookstore.rollback()
            

    elif choice == 3:
        #to update the price
        #throws an error 
        tt = input("Title of the book: ")
        m = float(input("Updated price: "))
        updt = "UPDATE books SET price='{}' WHERE title='{}';".format(m, tt) # Updated line 3       
        try:
            curs.execute(updt)
            Bookstore.commit()
            print("Price updated successfully!")
                                 
        except:
            print("error in operation")
            Bookstore.rollback()
