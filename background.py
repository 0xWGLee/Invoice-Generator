from random import randint
from datetime import date
from tkinter import *
from tkinter.ttk import *


# Class to process all the behind the scenes
class data():
    def __init__(self):
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

class FinalWindow(Toplevel):
    def __init__(self, d, master=None):
        super().__init__(master=master)
        self.title('New Window')
        self.geometry("300x400")

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

        for label in labels:
            Label(self, text=label).pack()

        

