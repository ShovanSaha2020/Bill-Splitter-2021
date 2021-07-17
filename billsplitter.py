# write your code here
import random

friends_list = []
print("Enter the number of friends joining (including you):")
friends_number = int(input())
if friends_number <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(friends_number):
        friends_list.append(input())
    # friends_and_guests = dict.fromkeys(friends_list, 0)
    # print(friends_and_guests)

    print("Enter the total bill value:")
    total_bill = float(input())

    # bill_per_person = round((total_bill / friends_number), 2)

    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    answer = input()
    if answer == 'Yes':
        lucky_winner = random.choice(friends_list)
        print(f"{lucky_winner} is the lucky one!")
        bill_per_person = round((total_bill / (friends_number - 1)), 2)
        friends_and_guests = dict.fromkeys(friends_list, bill_per_person)
        friends_and_guests[lucky_winner] = 0
        print(friends_and_guests)
    elif answer == 'No':
        print("No one is going to be lucky")
        bill_per_person = round((total_bill / friends_number), 2)
        friends_and_guests = dict.fromkeys(friends_list, bill_per_person)
        print(friends_and_guests)
