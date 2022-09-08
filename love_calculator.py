
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

count_true = 0
count_love = 0

for letter in name1.upper():
    if letter in 'TRUE':
        count_true += 1
    if letter in 'LOVE':
        count_love += 1

for letter in name2.upper():
    if letter in 'TRUE':
        count_true += 1
    if letter in 'LOVE':
        count_love += 1

score = int(str(count_true) + str(count_love))

if score < 10 or score > 90:
    print("Your score is {}, you go together like coke and mentos.".format(score))
elif 40 <= score <= 50:
    print("Your score is {}, you are alright together.".format(score))
else:
    print("Your score is {}.".format(score))
