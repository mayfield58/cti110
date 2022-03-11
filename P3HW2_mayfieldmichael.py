#Program takes user input of number of students and how many people are sharing a pizza and calculates the number of pizzas and  the price.
#11MAR2022
#CTI-110P3HW2-Pizza Order
#Michael Mayfield
#
#Pseudocode:
#Ask for input from user for how mant students to order pizza for
#Ask for input from user on how many people per pizza.
#Make else if structure for 1.5 , 2 , 3.
#If the amount of people per pizza is correct round up and make it the vaule of pizzas.
#Take pizzas and multiply by 5 to figure the cost then multiplay by 1.06 to figure the sales tax amount.
#Then display number of students pizzas needed and price.
#if number of students per pizza is invalid display an invalid entry message.


    
students = int(input('How many students do you want to order pizza for? '))
students_per = float(input('Enter number of people per pizza (1.5, 2 or 3):'))
print()
pizzas = students / students_per
pizza_cost = pizzas * 5
tax = pizza_cost * .06
price = tax + pizza_cost



if students_per == 1.5:
    students_per = 1.5
    print('------Pizza Order-------')
    print('Number of Students : ',(students))
    print('Pizzas Needed :',round(pizzas))
    print('Price $',(price))
    print('-----------------------')
elif students_per == 2:
    students_per = 2
    print('------Pizza Order-------')
    print('Number of Students : ',(students))
    print('Pizzas Needed :',round(pizzas))
    print('Price $',(price))
    print('-----------------------')
elif students_per == 3:
    students_per = 3
    print('------Pizza Order-------')
    print('Number of Students : ',(students))
    print('Pizzas Needed :',round(pizzas))
    print('Price $',(price))
    print('-----------------------')
else:
     print('INVALID ENTRY!!!!')
     print('Should have entered 1.5, 2 or 3\n')
     print('Run Program again')
     print()



