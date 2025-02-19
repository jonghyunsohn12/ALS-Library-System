📚 A Library System (ALS)

Overview

A Library System (ALS) is a software application that manages library books and membership records. It provides essential services for book borrowing, returning, reservations, and fines management. This project was developed as part of an academic assignment, implementing a MySQL-backed system with a Java Swing/Python Tkinter GUI to facilitate user interactions.

Features

📌 Membership Management

Create Membership: Register new users with unique membership IDs.

Update Membership: Modify member details (name, faculty, phone, email).

Delete Membership: Remove members (only if no outstanding loans/fines).

📚 Book Management

Acquire Books: Add books with details like title, author, ISBN, publisher, and year.

Withdraw Books: Remove outdated books (if not currently on loan).

🔄 Loan Management

Borrow Books: Members can borrow up to 2 books (if available and no fines).

Return Books: Books must be returned within 14 days; overdue returns incur a $1/day fine.

🔖 Reservation Management

Reserve Books: Place a hold on borrowed books (max 2 reservations per member).

Cancel Reservations: Remove a reservation before fulfillment.

💰 Fine Management

Track Outstanding Fines: Automatically compute fines for late returns.

Fine Payment: Members must pay the exact fine amount.

📊 Reports & Search

Search Books: Find books using title, author, ISBN, or publisher.

View Books on Loan: Check currently borrowed books.

View Reserved Books: List books under reservation.

View Outstanding Fines: Identify members with unpaid fines.

💻 Tech Stack

Backend: MySQL (Database)

Frontend: Java Swing / Python Tkinter
