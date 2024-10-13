pip install fpdf


import os
from fpdf import FPDF

class Theater:
    def __init__(self):
        self.shows_file = 'shows.txt'
        self.bookings_file = 'bookings.txt'
        self.init_files()

    def init_files(self):
        if not os.path.exists(self.shows_file):
            with open(self.shows_file, 'w') as f:
                f.write('ShowID,Movie,Seats,Price\n')
        if not os.path.exists(self.bookings_file):
            with open(self.bookings_file, 'w') as f:
                f.write('BookingID,ShowID,Customer,SeatsBooked,TotalPrice\n')

    def add_show(self, show_id, movie_name, seats, price):
        with open(self.shows_file, 'a') as f:
            f.write(f'{show_id},{movie_name},{seats},{price}\n')
        self.display_header(f'Show "{movie_name}" added successfully!')

    def display_shows(self):
        print("╔════════════════════════════════════════════════╗")
        print("║                Available Shows                 ║")
        print("╚════════════════════════════════════════════════╝")
        with open(self.shows_file, 'r') as f:
            for line in f.readlines()[1:]:
                show = line.strip().split(',')
                print(f"ShowID: {show[0]} | Movie: {show[1]} | Seats: {show[2]} | Price: {show[3]}")
        print("══════════════════════════════════════════════════")

    def check_seats(self, show_id):
        with open(self.shows_file, 'r') as f:
            for line in f.readlines()[1:]:
                show = line.strip().split(',')
                if show[0] == show_id:
                    return int(show[2])
        return -1

    def update_seats(self, show_id, seats_booked):
        shows = []
        with open(self.shows_file, 'r') as f:
            shows = f.readlines()

        with open(self.shows_file, 'w') as f:
            for line in shows:
                show = line.strip().split(',')
                if show[0] == show_id:
                    new_seats = int(show[2]) - seats_booked
                    f.write(f'{show[0]},{show[1]},{new_seats},{show[3]}\n')
                else:
                    f.write(line)

    def book_ticket(self, booking_id, show_id, customer_name, seats_booked):
        price_per_seat = self.get_price(show_id)
        total_price = seats_booked * price_per_seat
        available_seats = self.check_seats(show_id)

        if available_seats >= seats_booked:
            with open(self.bookings_file, 'a') as f:
                f.write(f'{booking_id},{show_id},{customer_name},{seats_booked},{total_price}\n')
            self.update_seats(show_id, seats_booked)
            self.display_header(f'Booking successful for {customer_name}, Total: ${total_price}')
            self.print_ticket_pdf(booking_id, show_id, customer_name, seats_booked, total_price)
        else:
            print(f'Only {available_seats} seats available!')

    def get_price(self, show_id):
        with open(self.shows_file, 'r') as f:
            for line in f.readlines()[1:]:
                show = line.strip().split(',')
                if show[0] == show_id:
                    return int(show[3])
        return 0

    def print_ticket_pdf(self, booking_id, show_id, customer_name, seats_booked, total_price):
        pdf = FPDF()
        pdf.add_page()

        pdf.set_font('Arial', 'B', 16)
        pdf.cell(200, 10, 'Theater Ticket', ln=True, align='C')

        pdf.set_font('Arial', '', 12)
        pdf.ln(10)
        pdf.cell(100, 10, f'Booking ID: {booking_id}', ln=True)
        pdf.cell(100, 10, f'Show ID: {show_id}', ln=True)
        pdf.cell(100, 10, f'Customer: {customer_name}', ln=True)
        pdf.cell(100, 10, f'Seats: {seats_booked}', ln=True)
        pdf.cell(100, 10, f'Total: ${total_price}', ln=True)

        pdf_output = f'ticket_{booking_id}.pdf'
        pdf.output(pdf_output)
        self.display_header(f'Ticket saved as {pdf_output}')

    def display_bookings(self):
        print("╔════════════════════════════════════════════════╗")
        print("║                  All Bookings                  ║")
        print("╚════════════════════════════════════════════════╝")
        with open(self.bookings_file, 'r') as f:
            for line in f.readlines()[1:]:
                booking = line.strip().split(',')
                print(f'BookingID: {booking[0]} | ShowID: {booking[1]} | Customer: {booking[2]} | Seats: {booking[3]} | Total: ${booking[4]}')
        print("══════════════════════════════════════════════════")

    def generate_sales_report(self):
        total_sales = 0
        with open(self.bookings_file, 'r') as f:
            for line in f.readlines()[1:]:
                booking = line.strip().split(',')
                total_sales += int(booking[4])
        self.display_header(f'Total sales: ${total_sales}')
        return total_sales

    def display_header(self, message):
        print("╔════════════════════════════════════════════════╗")
        print(f"║ {message.center(44)} ║")
        print("╚════════════════════════════════════════════════╝")

def main():
    theater = Theater()
    while True:
        print("\n╔════════════════════════════════════════════════╗")
        print("║              Theater Management Menu           ║")
        print("╚════════════════════════════════════════════════╝")
        print("1. Add Show")
        print("2. Display Shows")
        print("3. Book Ticket")
        print("4. Display Bookings")
        print("5. Generate Sales Report")
        print("6. Exit")
        print("══════════════════════════════════════════════════")

        choice = input("Enter your choice: ")

        if choice == '1':
            show_id = input("Enter Show ID: ")
            movie_name = input("Enter Movie Name: ")
            seats = int(input("Enter Seats Available: "))
            price = int(input("Enter Price per Ticket: "))
            theater.add_show(show_id, movie_name, seats, price)

        elif choice == '2':
            theater.display_shows()

        elif choice == '3':
            booking_id = input("Enter Booking ID: ")
            show_id = input("Enter Show ID: ")
            customer_name = input("Enter Customer Name: ")
            seats_booked = int(input("Enter Number of Seats: "))
            theater.book_ticket(booking_id, show_id, customer_name, seats_booked)

        elif choice == '4':
            theater.display_bookings()

        elif choice == '5':
            theater.generate_sales_report()

        elif choice == '6':
            theater.display_header("Exiting Program. Thank you!")
            break

        else:
            theater.display_header("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
