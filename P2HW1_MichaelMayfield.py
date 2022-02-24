# This program calculates subtotal, sales tax and overall total
# 24FEB2022
# CTI-110 P2HW1 - Total Purchases
# Michael Mayfield
#
item1 = float(input('Enter the price of item #1: '))
item2 = float(input('Enter the price of item #2: '))
item3 = float(input('Enter the price of item #3: '))
item4 = float(input('Enter the price of item #4: '))
item5 = float(input('Enter the price of item #5: '))
subtotal = item1 + item2 + item3 + item4 + item5
tax = subtotal * 0.07
total = subtotal + tax
print('-------Results-------')
print('Subtotal: ',(f'{total:.2f}'))
print('Sales Tax: ',(f'{tax:.2f}'))
print('Total: ',(f'{total:.2f}'))
