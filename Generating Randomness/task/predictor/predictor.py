import random

def remove_invalid_chars(user_input):
    for char in user_input:
        if char not in ('1', '0'):
            user_input = user_input.replace(char, '')
    return user_input


final_string = input('Print a random string containing 0 or 1:\n\n')
final_string = remove_invalid_chars(final_string)
triads_before_zero = {'000': 0,
          '001': 0,
          '010': 0,
          '011': 0,
          '100': 0,
          '101': 0,
          '110': 0,
          '111': 0
          }
triads_before_one = {'000': 0,
          '001': 0,
          '010': 0,
          '011': 0,
          '100': 0,
          '101': 0,
          '110': 0,
          '111': 0
          }
first_predicted_triad = ''
user_capital = 1000

while len(final_string) < 100:
    print('Current data length is {0}, {1} symbols left'.format(len(final_string), (100 - len(final_string))))
    print('Print a random string containing 0 or 1:\n')
    final_string += input()
    final_string = remove_invalid_chars(final_string)
print('\nFinal data string:', final_string, sep='\n')
print('\nYou have $1000. Every time the system successfully predicts your next press, you lose $1.')
print('Otherwise, you earn $1. Print "enough" to leave the game. Let\'s go!\n')
for i in range(0, len(final_string) - 3, 1):
    triad = final_string[i] + final_string[i + 1] + final_string[i+2]
    if final_string[i + 3] == '0':
        triads_before_zero[triad] += 1
    elif final_string[i + 3] == '1':
        triads_before_one[triad] += 1
user_input = input('Print a random string containing 0 or 1:\n')
while user_input != 'enough':
    user_input = remove_invalid_chars(user_input)
    while len(user_input) < 3:
        user_input = input('Print a random string containing 0 or 1:\n')
        user_input = remove_invalid_chars(user_input)
    for i in range(3):
        first_predicted_triad += str(random.randint(0, 1))
    predicted_sequence = first_predicted_triad
    for i in range(0, len(user_input) - 3, 1):
        triad_predicate = user_input[i] + user_input[i + 1] + user_input[i + 2]
        if triads_before_zero[triad_predicate] > triads_before_one[triad_predicate]:
            predicted_sequence += '0'
        elif triads_before_zero[triad_predicate] < triads_before_one[triad_predicate]:
            predicted_sequence += '1'
        else:
            predicted_sequence += str(random.randint(0, 1))
    predicted_digits_counter = 0
    for i in range(3,len(user_input), 1):
        if user_input[i] == predicted_sequence[i]:
            predicted_digits_counter += 1
    predicted_percentage = round(predicted_digits_counter / (len(user_input) - 3) * 100, 2)
    user_capital -= predicted_digits_counter
    user_capital += (len(user_input) - predicted_digits_counter - 3)
    print('prediction:')
    print(predicted_sequence)
    print('\nComputer guessed right {} out of {} symbols ({} %)'.format(predicted_digits_counter ,len(user_input) - 3, predicted_percentage))
    print('Your capital is now ${}\n'.format(user_capital))
    user_input = input('Print a random string containing 0 or 1:\n')
    first_predicted_triad =''
print('Game over!')
