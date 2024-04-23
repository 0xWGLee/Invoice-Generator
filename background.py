import os
from random import randint
from datetime import date
from tkinter import *
from tkinter.ttk import *


# Class to process all the behind the scenes
class data():
    def __init__(self):
        # Path to CSV file
        self.path = './output.csv'

        # CHANGE THIS VALUE TO CHANGE TAX
        self.tax = 7
        
        # Set tax to a percentage to multiply
        self.tax = self.tax/100

    # Set the required data
    def set_info(self, customer: dict, product: dict):
        # Set customer info
        self.name = customer['name']
        self.contact_phone = customer['phone']
        self.contact_email = customer['email']

        # Set the product info
        self.quantity = product['quantity']
        self.price = product['price']

    def calculate(self):
        # Calculate the subtotal
        self.subtotal = self.quantity * self.price

        # Calculate the tax amount
        self.tax_amount = round(self.subtotal * self.tax, 2)

        # Caculate the final amount
        self.final = self.subtotal + self.tax_amount

        # Generate an invoice number
        self.invoice_number = randint(1000, 9999)

        # Collect the date
        self.date = date.today()

    def save(self):
        # Check if file exists
        if not os.path.exists(self.path):
            # If file does not exist create list of columns
            columns = ['CUSTOMER NAME', 'CUSTOMER PHONE', 'CUSTOMER EMAIL', 'INVOICE NUMBER', 'DATE OF PURCHASE', 'SUBTOTAL', 'TAX AMOUNT', 'FINAL TOTAL']

            # Open new file
            with open(self.path, 'w') as f:
                # Write columns as a header
                f.write(','.join(columns))

        # Add all the info to a list
        columns = [self.name, self.contact_phone, self.contact_email, str(self.invoice_number), str(self.date), str(self.subtotal), str(self.tax_amount), str(self.final)]

        # String to be added to file
        writeable_data = '\n' + ','.join(columns)

        # Open file
        with open(self.path, 'a') as f:
            # append data to files
            f.write(writeable_data)

# This class opens a new window that displays the final invoice
class FinalWindow(Toplevel):
    def __init__(self, d, master=None):
        super().__init__(master=master)

        # Set title for the invoice
        self.title('Invoice Overview')
        # Set the window size
        self.geometry("300x400")

        # Create all the labels to display as a list
        labels = [
            "CUSTOMER INFO",
            "Customer name:   " + d.name, 
            "Customer phone:  " + d.contact_phone,
            "Customer email:  " + d.contact_email,
            "TRANSACTION INFO ",
            "Invoice Number   " + str(d.invoice_number), 
            "Date of purchase " + str(d.date),
            "PRODUCT INFO",
            "Subtotal         " + str(d.subtotal),
            "Tax amount       " + str(d.tax_amount),
            "Final Total      " + str(d.final),
        ]

        # Loop through the list of all the labels
        for label in labels:
            Label(self, text=label).pack()

        

