from question_module import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    q_1 = Question(item["text"], item["answer"])
    question_bank.append(q_1)

quiz = QuizBrain(question_bank)


while quiz.stil_has_questions():
    quiz.next_question()

print("you've completed the quiz")
print(f"your final score was: {quiz.score}/{quiz.question_number}")
