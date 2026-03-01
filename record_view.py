def next_record(self):
    model = self.ui.customer_details_table.model()
    if self.current_record < model.rowCount() - 1:
        self.current_record += 1
    self.highlight_record()

def back_record(self):
    if self.current_record > 0:
        self.current_record -= 1
    self.highlight_record()

def first_record(self):
    self.current_record = 0
    self.highlight_record()

def last_record(self):
    model = self.ui.customer_details_table.model()
    self.current_record = model.rowCount() - 1
    self.highlight_record()

def highlight_record(self):
    self.ui.customer_details_table.selectRow(self.current_record)
    index = self.ui.customer_details_table.model().index(self.current_record, 0)
    self.ui.customer_details_table.scrollTo(index)