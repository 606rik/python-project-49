import random
import operator

DESCRIPTION = "What is the result of the expression?"

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}

def get_question_and_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    op = random.choice(list(OPERATORS.keys()))
    question = f"{num1} {op} {num2}"
    correct_answer = str(OPERATORS[op](num1, num2))
    return question, correct_answer
