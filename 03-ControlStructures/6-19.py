question_1 = input("SURVEY Are you interested in computer science? (y/n): ")
question_2 = input("Do you like playing computer games? (y/n): ")
question_3 = input("Do you have an Instagram account? (y/n): ")

if question_1 == "y":
    question_1 = True
elif question_1 == "n":
    question_1 = False

if question_2 == "y":
    question_2 = True
elif question_2 == "n":
    question_2 = False

if question_3 == "y":
    question_3 = True
elif question_3 == "n":
    question_3 = False

print(f"Interested in computer science: {'Yes' if question_1 else 'No'}")
print(f"Playing computer games: {'Yes' if question_2 else 'No'}")
print(f"Has an Instagram account: {'Yes' if question_3 else 'No'}")

