# Theater Management System

## Overview

The Theater Management System is a command-line interface (CLI) application designed to facilitate the management of movie shows, ticket bookings, and sales reporting for a theater. This application provides an intuitive interface for theater administrators to add shows, book tickets for customers, and generate reports on sales.

## Features

### 1. Show Management
- **Add Show**: Administrators can add new movie shows by providing a unique Show ID, movie name, available seats, and ticket price. This feature helps keep track of all the shows available for booking.

### 2. Display Available Shows
- **View Shows**: Users can view all available shows along with their details, such as Show ID, movie title, available seats, and ticket price. This feature helps customers and administrators keep track of current offerings.

### 3. Ticket Booking
- **Book Tickets**: Users can book tickets for a specific show by providing a Booking ID, Show ID, customer name, and the number of seats they wish to book. The system checks for seat availability and calculates the total cost, ensuring that bookings are only confirmed if there are sufficient seats available.
- **PDF Ticket Generation**: Upon successful booking, the application generates a PDF ticket containing booking details such as Booking ID, Show ID, customer name, seats booked, and total price. This ticket can be printed or saved for customer reference.

### 4. View Bookings
- **Display All Bookings**: Users can view a list of all bookings made in the system, including booking IDs, show IDs, customer names, number of seats booked, and total prices. This feature helps administrators monitor ticket sales and customer engagement.

### 5. Sales Reporting
- **Generate Sales Report**: Administrators can generate a report of total sales based on bookings made. This feature provides insights into the theater’s revenue and helps with financial planning and analysis.

### 6. User-Friendly Command-Line Interface
- **Formatted Outputs**: The application features a well-structured command-line interface with clear menus, headers, and formatted outputs, making it easy for users to navigate and interact with the system.

### 7. Persistent Data Storage
- **File Handling**: The application uses text files (`shows.txt` and `bookings.txt`) to store information about shows and bookings persistently. This allows data to be retained between sessions.

## Requirements
- **Python 3.x**: Ensure you have Python 3.x installed on your machine.
- **FPDF Library**: The application uses the FPDF library for generating PDF tickets. You can install it via pip:
  ```bash
  pip install fpdf

**to run the project python main.py**
