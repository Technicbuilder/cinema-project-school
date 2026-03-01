#   This file's purpose is to format and maniuplate data from the user
#   It will return management_didctionary(containing revenue generated from sale, tickets sold ), data_dictionary(containing booking info)


class Formatter:
    def __init__(self, seats_booked, phone_number, name, date, price_paid):
        self.seats_booked = seats_booked
        self.phone_number = phone_number
        self.name = name
        self.date = date
        self.price_paid = price_paid

    def booking_data(self):
        customer_data = {'seats':   self.seats_booked,
                         'phone':   self.phone_number,
                         'name':    self.name,
                         'date':    self.date
                         }
        
        return customer_data
    
    def management_data(self):
        finance_data = {
            'price_paid': self.price_paid,
            'tickets_sold': len(self.seats_booked)
        }

        return finance_data