class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
    def  stil_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        true_false = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(true_false, current_question.answer)

    def check_answer(self, true_false, correct_answer):
        if true_false.lower() == correct_answer.lower():
            self.score += 1
            print("you got it right")
        else:
            print("that's wrong.")
        print(f"the correct output was: {correct_answer}.")
        print(f"your current score is: {self.score}/{self.question_number}.")
        print("\n")



