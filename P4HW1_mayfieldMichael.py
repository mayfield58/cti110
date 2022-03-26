# CTI-110
# P4HW1 - Score List
# Michael Mayfield
# 25MAR2022

# Pseudocode:
#user enters how many score they want to enter
#for every number of scores user inputs a vaule for the scores
#set a loop to see if input is between 0 and 100
#if incorrect ask for input again
#find the lowest vaule
#remove lowest score
#calculate average
# assign letter grade based on the average of the scores
#print the lowest score the modified list score average and letter grade.


def main():

    num_scores = int(input(f'How many scores would you like to enter?: '))

    num = 1

    score_list = []

    for score in range(num_scores):

        user_input = float(input(f'Enter score #{num}: '))

        while not 0 <= user_input <= 100:

            print(f'''INVALID score entered!
Scores should be between 0 and 100''')

        user_input = float(input(f'Enter score #{num} again: '))

        num = num + 1

        score_list.append(user_input)

    lowest_score = min(score_list)

    score_list.remove(lowest_score)

    score_avg = sum(score_list) / len(score_list)

    if score_avg < 70:
        letter_grade = 'F'
    elif score_avg < 80:
        letter_grade = 'C'
    elif score_avg < 90:
        letter_grade = 'B'
    else:
        letter_grade = 'A'

    print(f'''
-----------------Results-----------------
Lowest Score :  {lowest_score:.1f}
Modified List:  {score_list}
Score Average:  {score_avg:.2f}
Grade        :  {letter_grade}
-----------------------------------------''')


main()
