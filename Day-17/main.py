from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
for questions in question_data:
    question_text=questions['text']
    question_answer=questions['answer']
    new_question=Question(question_text,question_answer)
    question_bank.append(new_question)
print(question_bank)

quiz=QuizBrain(question_bank)
while quiz.still_has_questions()==True:
    quiz.next_question() 
print('\n Congrats You\'ve Completed The Quiz')
print(f'Your final score is {quiz.score}/{quiz.question_no}')