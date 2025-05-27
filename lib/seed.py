from datetime import date
from models import Base, engine, session
from models.book import Book
from models.members import Member
from models.borrow_record import BorrowRecord


Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


book1 = Book(title="Subbtle Art Of Not Giving A Fuck", author="Mark Manson", isbn="9780451524935")
book2 = Book(title="Chozi La Heri", author="Assumpta K. Matei", isbn="9780060935467")
book3 = Book(title="The Blossoms Of The Savvanah", author="Henry R. ole Kulet", isbn="9780743273565")


member1 = Member(name="Jadah Atieno", email="jadah@example.com")
member2 = Member(name="Bob Oyier", email="bob@example.com")


borrow1 = BorrowRecord(
    member=member1,
    book=book1,
    borrow_date=date(2025, 5, 20),
    return_date=None
)

borrow2 = BorrowRecord(
    member=member2,
    book=book2,
    borrow_date=date(2025, 5, 22),
    return_date=date(2025, 5, 26)
)


book1.available = False
book2.available = True
book3.available = True


session.add_all([book1, book2, book3, member1, member2, borrow1, borrow2])
session.commit()

print("✅ Seed data loaded.")