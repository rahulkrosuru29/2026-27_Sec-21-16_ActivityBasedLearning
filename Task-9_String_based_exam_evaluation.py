# String Based Exam Evaluation
correct = 0
wrong = 0

answers = ["A", "B", "C", "D", "A"]

key = ["A", "B", "D", "D", "A"]

for i in range(5):

    if answers[i] == key[i]:
        correct = correct + 1

    else:
        wrong = wrong + 1

print("Correct Answers:", correct)
print("Wrong Answers:", wrong)

marks = correct * 2 - wrong

print("Final Marks:", marks)