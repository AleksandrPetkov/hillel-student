import random

hidden_number = random.randint(1, 10)
user_number = int(input('Please enter your number from 1 to 10: '))
while True:
    if user_number == hidden_number:
        print('Congratulations, you guessed the number!!!')
        break
    if user_number != hidden_number:
        choice = input('Do you want to try again, enter yes/no:')
        if choice == 'no':
            print('Goodbye!')
            break
        if choice == 'yes':
            choice_2 = input('Do you want continue to guess or computer can try to guess your number,'
                             'enter "i" - you want to continue, "c" - computer try to guess:')
            if choice_2 == 'i':
                user_number = int(input('Please enter your number from 1 to 10: '))

            if choice_2 == 'c':
                comp_number = random.randint(1, 10)
                comp_range = [*range(1, 11)]
                mid = len(comp_range) // 2
                low = 0
                high = len(comp_range)
                print('Am I guess your number, enter yes/no?', mid)
                user_answer = input()
                if user_answer == 'yes':
                    print('I am guess your number!!!')
                    break
                if user_answer == 'no':
                    user_answer_2 = input('Is your number less or bigger than mine, enter less/bigger:')
                    while comp_range[mid] != comp_number and low <= high:
                        if user_answer_2 == 'bigger':
                            low = mid + 1
                        else:
                            high = mid - 1
                        mid = (low + high) // 2
                        if low > high:
                            print('No value')
                        else:
                            print('Am I guess your number, enter yes/no?', mid)
                            user_answer = input()
                            if user_answer == 'yes':
                                print('I am guess your number!!!')
                                print('Goodbye!!!')
                                break
                            else:
                                user_answer_2 = input('My number was less or bigger than your, enter less/bigger:')




