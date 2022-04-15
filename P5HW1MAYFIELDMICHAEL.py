# The program collects scores and makes them to a list and gives the letter grade.
#13AUG2022
#CTI-110 P5HW1-Score List
# Michael Mayfield
#


def main():
    menu()
    
#creates the menu list
def menu():
    repeat = 1
    choice = 0
    scorelist = []
    while repeat != 0:
        print()
        print('----MENU----')
        print('1. Create Score List')
        print('2. Display Results')
        print('3. Exit')
        print('------------')


        choice = input("Enter a choice 1 or 2 or 3: ")
        if choice == '1':
           scorelist = listofscores()
        elif choice == '2':
            if len(scorelist) == 0:
                print('List not created!')
            else:
                calcscores(scorelist)
        elif choice == '3':
            repeat = 0
        else:
            print("Not a valid entry")
            print("Try again")
            repeat = 1
            
    print('Program Terminated!')

#asks for score entrys and sets that they should be between 0 and 100
def makelist(numscores):
    scores = []
    i = 0
    while i < numscores:
        score = int(input(f'Enter score #{i + 1}: '))
        if 0 > score or score > 100:
            print('Invalid Entry!\nEntry must be between 0 and 100!')
            i = i
        else:
            scores.append(score)   
            i += 1
    return scores

def calcscores(scorelist):
 

    #removes the lowest score
    min_score = min(scorelist)
    scorelist.remove(min_score)

    
    average = sum(scorelist)/len(scorelist)

    ## sets the number for each letter grade.
    if 100 >= average >= 90:
        lettergrade = 'A'
    elif 89 >= average >= 80:
        lettergrade = 'B'
    elif 79 >= average >= 70:
        lettergrade = 'C'
    elif 69 >= average >= 60:
        lettergrade = 'D'
    elif 59 >= average >= 0:
        lettergrade = 'F'

    #makes a list of the vaules given
    temp = [min_score,scorelist,average,lettergrade]

    #returns the vaules
    printscores(temp)



def listofscores():
    index = int(input('Enter number of scores: '))
    scorelist = makelist(index)
    return scorelist


    
def printscores(resultlist):
    
    
    
    print('Lowest score:',resultlist[0])
    print('List of scores (lowest omitted):',resultlist[1])
    print('Average:',resultlist[2])
    print('Letter Grade:',resultlist[3])
   


main()
