from question_model import Question
from data import question_data

question_bank = []
for new_q in question_data:
    question_bank.append(Question(text=new_q["text"],answer=new_q["answer"]))