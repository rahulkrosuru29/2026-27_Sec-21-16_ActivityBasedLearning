#Answer Evaluation using strinng functions
print("Question: What is the programming language used for this code?")
correct_answer = "python"
student_answer = input("Enter your answer: ")

if student_answer.lower() == correct_answer:
    print("Correct Answer")
else:
    print("Wrong Answer")