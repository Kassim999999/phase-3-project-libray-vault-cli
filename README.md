# 📚 Library Vault

## Description

The **Library Vault** is a command-line application built with Python and SQLAlchemy. It allows a library to manage books, members, and borrowing history in an organized way using object-oriented models and a relational database.

This project demonstrates model relationships, data seeding, and database interactions using an ORM rather than raw SQL.

---

## Features

- Add and manage books
- Register and manage members
- Record book borrowing and returns with date tracking
- View availability of books
- See borrowing history per member

---

## Data Model

- `Book`: Represents a book in the library  
- `Member`: A registered person who can borrow books  
- `BorrowRecord`: A join model linking Members and Books with additional data like borrow and return dates

**Relationships:**
- A book can be borrowed by many members 
- A member can borrow many books
- The many-to-many relationship is managed through `BorrowRecord`

---



## Setup Instructions

### 1. Clone the repository

```bash
git clone git@github.com:Kassim999999/phase-3-project-libray-vault-cli.git
cd library-vault


2. Install dependencies
pipenv install
pipenv shell

3. Seed the database
python lib/seed.py
This will create the database (library.db) and insert some sample books, members, and borrowing records.

4. View the data (optional)
python lib/debug.py

---

## **Technologies Used**
Python 3

SQLAlchemy ORM

SQLite (as the database)

---

## **Next Steps**
 Implement CLI functionality in cli.py

 Add CRUD helpers in helper.py

 Expand tests or add unit tests for model validation

 ---

 ## **Authors**
 - Rooney Kassim

## **License**

This project is open source and available under MIT License






