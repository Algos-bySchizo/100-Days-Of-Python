class QuizBrain():
    def __init__(self, q_list):
        self.question_no=0 
        self.question_list=q_list
    
    def next_question(self):
        current_question=self.question_list[self.question_no]
        input(f"Q.{self.question_no+1}: {current_question.text} (True/False): ")
