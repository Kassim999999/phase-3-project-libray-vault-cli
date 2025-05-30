from models import session
from models.book import Book
from models.members import Member
from models.borrow_record import BorrowRecord
from datetime import date

def main_menu():
    while True:
        print("\nLIBRARY SYSTEM MENU")
        print("1. View all books")
        print("2. View all members")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            for book in session.query(Book).all():
                print(book)
        elif choice == '2':
            for member in session.query(Member).all():
                print(member)
        elif choice == '3':
            borrow_book()
        elif choice == '4':
            return_book()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

def borrow_book():
    book_id = int(input("Enter Book ID to borrow: "))
    member_id = int(input("Enter Member ID: "))
    book = session.get(Book, book_id)
    if book and book.available:
        book.available = False
        record = BorrowRecord(book_id=book.id, member_id=member_id, borrow_date=date.today())
        session.add(record)
        session.commit()
        print("Book borrowed.")
    else:
        print("Book not available.")

def return_book():
    book_id = int(input("Enter Book ID to return: "))
    record = session.query(BorrowRecord).filter_by(book_id=book_id, return_date=None).first()
    if record:
        record.return_date = date.today()
        book = session.get(Book, book_id)
        book.available = True
        session.commit()
        print("Book returned.")
    else:
        print("No active borrow record found.")

if __name__ == "__main__":
    main_menu()
