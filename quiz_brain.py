#TODO ask question, check if answer is correct, check if were end of quiz
#brings up the question and asks the user true or false
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number] #tap into the list and get hold of item at the current question number
        self.question_number += 1
        user_answer = input(f"Q1: {self.question_number}: {current_question.text} (True/False)")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
        else:
            print("WAH WAH Wrong!")
        print(f"The correct answer is {correct_answer}!\nCurrent score is {self.score}/{self.question_number}")

