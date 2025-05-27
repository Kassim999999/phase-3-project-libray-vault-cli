from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from . import Base


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    isbn = Column(String, unique=True)
    available = Column(Boolean, default=True)

    borrow_records = relationship("BorrowRecord", back_populates="book")


    def __repr__(self):
        return f"<Book(title='{self.title}', author='{self.author}', available={self.available})>"
    