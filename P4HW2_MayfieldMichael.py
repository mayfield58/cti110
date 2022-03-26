#Program takes user input of number of students and how many people are sharing a pizza and calculates the number of pizzas and  the price.
#Michael Mayfield
#CTI-110P4HW2-Pizza Order
#25Mar2022
#Pseudocode:
#Ask for input from user for how mant students to order pizza for
#Ask for input from user on how many people per pizza.
#make while loop if user input isnt in list
#Make else if structure for 1.5 , 2 , 3.
#If the amount of people per pizza is correct round up and make it the vaule of pizzas.
#Take pizzas and multiply by 5 to figure the cost then multiplay by 1.06 to figure the sales tax amount.
#Then display number of students pizzas needed and price.
#if number of students per pizza is invalid display an invalid entry message.
def main():
    
    print('How many students do you want to order pizza for?', end=' ')
    students = int(input())
    print('Enter number of people per pizza ( 1.5, 2 or 3) :', end=' ')
    people_per_pizza = float(input())

    sharer = [1.5, 2, 3]
    
    while people_per_pizza not in [1.5, 2, 3]:
        print('Invalid Entry !')
        print('Should have entered 1.5, 2 or 3') 
        print('Enter number of people per pizza again ( 1.5, 2 or 3) :', end=' ')
        people_per_pizza = float(input())         
       
    
    if people_per_pizza == 1.5:
        pizzas_needed = students / people_per_pizza
    elif people_per_pizza == 2:
        pizzas_needed = students / people_per_pizza
    elif people_per_pizza == 3:
        pizzas_needed = students / people_per_pizza    
  
    cost_per_pizza = 5.00
    sub_total = float(cost_per_pizza * pizzas_needed)
    taxed_total = float(sub_total * 0.06)
    total = sub_total + taxed_total

    print('----Pizza Order--------')
    print('Number of Students :', students)
    print(f'Pizzas Needed :', round(pizzas_needed))
    print(f'Price $, {total:.2f}')
    print('-----Pizza Order-------')

    restart = input('Would you like to run program again (y for yes): ')
    if restart == 'y':
        main()
    else:
        exit()
main()
