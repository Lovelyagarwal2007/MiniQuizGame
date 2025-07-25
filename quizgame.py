# Python Quiz Game
import requests
import random

questions = ("[(6 + 4) * 2^2 - 8] ÷ 4",
             "(5 + 3 * 2)^2 ÷ (4 + 2)",
             "60 ÷ [(4 + 2) * (3 + 1)]",
             "[(2 + 3) * (4 + 1)^2 - 10] ÷ 5",
             "[(16 ÷ 4) + (3 * 2)]^2",
             "(8 + 2) * [6 - (3 + 1)]",
             "100 ÷ [(2 * 5) + (3^2)]",
             "[(5 * 3)^2 - (6 + 3) * 2] ÷ 3",
             "[(7 + 1) * 2 + (10 - 4)]^2",
             "[(12 ÷ 3) + (2^2 + 1)] * 2")

options(("A.  12", "B.  10" "C.  09" "D.  08"),
        ("A.  20.36", "B.  20.16" "C.  20.54" "D.  20.76"),
        ("A.  2.3", "B.  2.6" "C.  2.5" "D.  2.4"),
        ("A.  22", "B.  23" "C.  25" "D.  33"),
        ("A.  100", "B.  103" "C.  98" "D.  108"),
        ("A.  22", "B.  29" "C.  20" "D.  25"),
        ("A.  5.27", "B.  5.36" "C.  5.26" "D.  5.29"),
        ("A.  68", "B.  71" "C.  65" "D.  69"),
        ("A.  484", "B.  489" "C.  481" "D.  476"),
        ("A.  13", "B.  28" "C.  35" "D.  18"))

answers = ("D", "B", "C", "B", "A", "C", "C", "D", "A", "D")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answer[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num +=1
print("------------------------")
print("        RESULTS         ")
print("------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = (score / len(questions)) * 100
print(f"Your score is: {score}%")