# 📚 A Library System (ALS)

## Overview
A Library System (ALS) is a software application that manages library books and membership records. It provides essential services for **book borrowing, returning, reservations, and fines management**. This project was developed as part of an academic assignment, implementing a **MySQL-backed** system with a **Java Swing/Python Tkinter GUI** to facilitate user interactions.

## Features
### 📌 Membership Management
- **Create Membership**: Register new users with unique membership IDs.
- **Update Membership**: Modify member details (name, faculty, phone, email).
- **Delete Membership**: Remove members (only if no outstanding loans/fines).

### 📚 Book Management
- **Acquire Books**: Add books with details like title, author, ISBN, publisher, and year.
- **Withdraw Books**: Remove outdated books (if not currently on loan).

### 🔄 Loan Management
- **Borrow Books**: Members can borrow up to 2 books (if available and no fines).
- **Return Books**: Books must be returned within 14 days; overdue returns incur a **$1/day fine**.

### 🔖 Reservation Management
- **Reserve Books**: Place a hold on borrowed books (max 2 reservations per member).
- **Cancel Reservations**: Remove a reservation before fulfillment.

### 💰 Fine Management
- **Track Outstanding Fines**: Automatically compute fines for late returns.
- **Fine Payment**: Members must pay the exact fine amount.

### 📊 Reports & Search
- **Search Books**: Find books using title, author, ISBN, or publisher.
- **View Books on Loan**: Check currently borrowed books.
- **View Reserved Books**: List books under reservation.
- **View Outstanding Fines**: Identify members with unpaid fines.

## 💻 Tech Stack
- **Backend:** MySQL (Database)
- **Frontend:** Java Swing / Python Tkinter

## 📂 Project Structure
```
/ALS-Library-System
│── /src
│   ├── models/        # Database schema and entity classes
│   ├── controllers/   # Logic for book loans, reservations, etc.
│   ├── ui/            # Swing/Tkinter-based user interface
│── /sql
│   ├── schema.sql     # Database schema
│   ├── seed_data.sql  # Initial book/member data
│── README.md
```

## 🚀 Installation & Setup
1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/ALS-Library-System.git
   cd ALS-Library-System
   ```

2. **Setup MySQL database**  
   - Create a new MySQL database:
     ```sql
     CREATE DATABASE ALSLibrary;
     ```
   - Import schema and sample data:
     ```bash
     mysql -u root -p ALSLibrary < sql/schema.sql
     mysql -u root -p ALSLibrary < sql/seed_data.sql
     ```

3. **Run the Application**  
   - If using **Java**, compile and run:
     ```bash
     javac -cp .:mysql-connector-java-8.0.26.jar src/*.java
     java -cp .:mysql-connector-java-8.0.26.jar Main
     ```
   - If using **Python**, install dependencies and run:
     ```bash
     pip install mysql-connector-python
     python main.py
     ```
This Library System project showcases **efficient library management** while ensuring **scalability and user-friendly interaction**. 🚀
