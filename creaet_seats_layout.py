from PyQt6.QtWidgets import QPushButton
from PyQt6 import QtGui

def draw_seats_and_screen(self):
    """
    Repurposed old tkninter seating layout logic
    """
    #   Seats code
    rows = reversed('ABCDEFGHIJ')
    seats_per_row = 20
    
    self.buttons = {}
    
    for row_number, row in enumerate(rows):
        for chair_number in range(seats_per_row):
            seat_id = f'{row}{chair_number + 1}'
            
            #   defines each button
            button = QPushButton(f'{row}{chair_number + 1}')
            button.setFixedSize(35, 35)
            button.setFont(QtGui.QFont('Arial', 7))
            button.taken = False
            button.cost = self.seat_price
            button.setStyleSheet('background-color: green; color: white;')
            
            #   calls  seat_clicked function after clicked
            button.clicked.connect(lambda checked, b=button: self.seats_clicked(b))
            
            self.ui.seat_layout.addWidget(button, row_number, chair_number)
            self.buttons[seat_id] = button
    
    for user, seats in self.data.items():
        for seat in seats:
            if seat in self.buttons:
                self.buttons[seat].setStyleSheet('background-color: red; color: white; border-spaces: 3px')
                self.buttons[seat].taken = True
                self.buttons[seat].setEnabled(False)
    
    # Screen code
    screen = QPushButton('STAGE')
    screen.setEnabled(False)
    screen.setFixedHeight(20)
    screen.setFixedWidth(seats_per_row * 35)
    screen.setStyleSheet('background-color: white; color: black; border-radius: 0px;')
    self.ui.seat_layout.addWidget(screen, len('ABCDEFGHIJ') + 1, 0, 1, seats_per_row)


def seat_clicked(self, button):
    """Changes seat colour depending on whether button has been interacted with"""
    if not button.taken:
        button.setStyleSheet('background-color: red; color: white;')
        button.taken = True
        self.chosen_seats.append(button.text())
    else:
        button.setStyleSheet('background-color: green; color: white;')
        button.taken = False
        self.chosen_seats.remove(button.text())
