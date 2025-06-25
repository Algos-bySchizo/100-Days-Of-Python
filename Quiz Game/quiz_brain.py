class QuizBrain():
    def __init__(self, q_list):
        self.score=0
        self.question_no=0 
        self.question_list=q_list
    
    def next_question(self):
        current_question=self.question_list[self.question_no]
        self.question_no+=1
        user_answer=input(f"Q.{self.question_no}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return self.question_no < len(self.question_list)
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower()==correct_answer.lower():
            self.score+=1
            print('You got it right!\n')
            print(f'Your score is {self.score}')
        else:
            print('you got it wrong!\n')
        print(f'The Correct answer was: {correct_answer!r}\n')
        print(f'Current Score is {self.score}/{self.question_no}')
        print('\n')