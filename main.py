import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from python_ui_files.main_interface import Ui_MainWindow
from creaet_seats_layout import draw_seats_and_screen, seat_clicked
from manage_databases import Manager
from PyQt6.QtGui import QStandardItemModel, QStandardItem
import sqlite3
from record_view import first_record, last_record, next_record, back_record, highlight_record

class Window(QMainWindow):

    #   Not sure why this has to be outside the __init__, I know its to do with some assigning issues
    #   had to ge claude ode to help me fix this part
    draw_seats_and_screen = draw_seats_and_screen
    seats_clicked = seat_clicked
    next_record = next_record
    back_record = back_record
    first_record = first_record
    last_record = last_record
    highlight_record = highlight_record

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.seat_price = 10
        self.chosen_seats = []
        self.data = {}
        
        self.draw_seats_and_screen()
        self.ui.pushButton.clicked.connect(self.collect_booking_details_and_save)

        self.current_record = 0
        self.ui.next_record.clicked.connect(self.next_record)
        self.ui.previous_record.clicked.connect(self.back_record)
        self.ui.first_record.clicked.connect(self.first_record)
        self.ui.last_record.clicked.connect(self.last_record)

        self.load_table_widget()

    draw_seats_and_screen = draw_seats_and_screen
    seats_clicked = seat_clicked

    def collect_booking_details_and_save(self):
        name = self.name = self.ui.ente_name_entry.text()
        phone = self.phone = self.ui.enter_phone_number.text()
        date = self.date = self.ui.enter_date_edit.text()
        price = self.price = self.ui.enter_price_paid_entry.text()
        seats = self.seats = self.chosen_seats

        paid = False

        price_to_pay = len(seats) * self.seat_price

        if not name or not phone or not date:
            self.ui.enter_price_paid_entry.setPlaceholderText('Please fill in all fields')
            return
        
        if not seats:
            self.ui.enter_price_paid_entry.setPlaceholderText('Please select a minimum of one seat')
            return

        if price == '':
            self.ui.enter_price_paid_entry.setPlaceholderText(f'Enter {price_to_pay}')
            return
        
        try:
            price_inputted = float(price)
        except ValueError:
            self.ui.enter_price_paid_entry.setPlaceholderText('Please input a valid number')
            
        
        if price_inputted < price_to_pay:
            self.ui.enter_price_paid_entry.setText(f'Underpaying - need £{price_to_pay}')
            return
        
        elif price_inputted > price_to_pay:
            self.ui.enter_price_paid_entry.setText(f'Overpaying - need £{price_to_pay}')
            return
        
        handler = Manager()
        handler.store_customer_record(name, phone, date, price_inputted, seats)
        handler.store_management_record(date, price_inputted, len(seats))
        self.load_table_widget()


    def load_table_widget(self):
        conn = sqlite3.connect('databases/cust_record')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cust_record")
        records = cursor.fetchall()
        conn.close()

        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(['Phone Number', 'Name', 'Seats', 'Date', 'Amount Paid'])
        for rows in records:
            row = [QStandardItem(str(field)) for field in rows]
            model.appendRow(row)

        self.ui.customer_details_table.setModel(model)
        self.ui.customer_details_table.horizontalHeader().setStretchLastSection(True)

    


    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())