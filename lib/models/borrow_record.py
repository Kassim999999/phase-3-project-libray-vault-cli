from sqlalchemy import Column, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from . import Base

class BorrowRecord(Base):
    __tablename__ = 'borrow_records'


    id = Column(Integer, primary_key=True)
    member_id = Column(Integer, ForeignKey('members.id'))
    book_id = Column(Integer, ForeignKey('books.id'))
    borrow_date = Column(Date)
    return_date = Column(Date, nullable=True)


    member = relationship("Member", back_populates="borrow_records")
    book = relationship("Book", back_populates="borrow_records")


    def __repr__(self):
        return f"<BorrowRecord(book='{self.book.title}', member='{self.member.name}', borrow_date={self.borrow_date}, return_date={self.return_date})>"
    