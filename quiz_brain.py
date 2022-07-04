

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_question = input(f"Q.{self.question_number} {current_question.question}. Please type your answer ('True' or "
                              f"'False':) ")

        self.chek_answer(user_question, current_question.correct_answer)

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def chek_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That`s wrong.")
        print(f"Right answer is {correct_answer}!")
        print(f"Your score is {self.score}/{self.question_number}")
        print("\n")

