import background
from tkinter import *

# A simple function to create and pack a label while returning a text field
def Field(text, type):
    # Create the label using the text passed to the function
    Label(root, text=text).pack()
    # Return the text input
    return type(root, height=1, width=20)

# A simple function to verify datatypes
def check(type, obj):
    # Try to convert obj to type
    try:
        return type(obj.get('1.0', 'end-1c'))
    # Catch error show an error
    except TypeError:
        print('Error! with type of ' + obj)

# A simple function used to put all the data into a dictionary and pass it to the helper class
def compute():
    # Create a dict for all the customer related info
    customer_data = {
        'name': customer_name_input.get('1.0', 'end-1c'),
        'phone': customer_phone_input.get('1.0', 'end-1c'),
        'email': customer_email_input.get('1.0', 'end-1c'),
    }

    quantity = check(int, product_quantity)
    price = check(float, product_price)

    # Create a dict for all the product related info
    product_data = {
        'quantity': quantity,
        'price': price
    }

    # Pass the data to the background class
    d.set_info(customer=customer_data, product=product_data)
    
    # Calculate all the data in the background class
    d.calculate()

    # Call the new window from the another class
    background.FinalWindow(master=root, d=d)

    
d = background.data()

# intialize GUI
root = Tk()
root.title('Invoice generator')
root.resizable(False, False)

# Set a title label
titlelabel = Label(root, text='Invoice generator')
titlelabel.pack()

# Customer name input element
customer_name_input = Field('Customer Name:', Text)
customer_name_input.pack()

# Customer contact email
customer_phone_input = Field('Customer phone', Text)
customer_phone_input.pack()

# Customer contact phone
customer_email_input = Field('Customer Email', Text)
customer_email_input.pack()

# Product price
product_quantity = Field('Product Quantity:', Text)
product_quantity.pack()

# Product price element
product_price = Field('Product price:', Text)
product_price.pack()

# Calculate button
calc = Button(root, text='Calculate', command=(compute))
calc.pack()

root.mainloop()