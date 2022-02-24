# CTI-110
# P2HW2 - Score Avg
# Michael Mayfield
# 24FEB2022
#
score1 = float(input('Enter score #1: '))
score2 = float(input('Enter score #2: '))
score3 = float(input('Enter score #3: '))
score4 = float(input('Enter score #4: '))
score5 = float(input('Enter score #5: '))
score6 = float(input('Enter score #6: '))
score7 = float(input('Enter score #7: '))
scores = [score1, score2, score3, score4, score5, score6, score7]
lowest_score = min(scores)
scores.remove(min(scores))
modified_list = scores
scores_average = sum(modified_list) / len(modified_list)
print('\n--------------------Results--------------------')
print('Lowest Score: ', lowest_score)
print('Modified List: ', modified_list)
print('Scores Average:" ',(f'{scores_average:.2f}'))
print('-----------------------------------------------')
