import json

def validate_positive_integer(value):
    if isinstance(value, int) and value > 0:
        return True
    return False

def read_user(user_id: int):
    if not validate_positive_integer(user_id):
        raise ValueError("Invalid user_id")

    with open('data/users.json') as stream:
        users = json.load(stream)

    for user in users:
        if user['id'] == user_id:
            return user

    return None

def read_questions(position: int):
    if not validate_positive_integer(position):
        raise ValueError("Invalid position")

    with open('data/questions.json') as stream:
        questions = json.load(stream)

    for question in questions:
        if question['position'] == position:
            return question

def read_alternatives(question_id: int):
    if not validate_positive_integer(question_id):
        raise ValueError("Invalid question_id")

    alternatives_question = []
    with open('data/alternatives.json') as stream:
        alternatives = json.load(stream)

    for alternative in alternatives:
        if alternative['question_id'] == question_id:
            alternatives_question.append(alternative)

    return alternatives_question

def create_answer(payload):
    if not isinstance(payload, dict) or 'answers' not in payload:
        raise ValueError("Invalid payload")

    answers = []
    result = []

    with open('data/alternatives.json') as stream:
        alternatives = json.load(stream)

    for question in payload['answers']:
        if not validate_positive_integer(question.get('question_id', 0)):
            raise ValueError("Invalid question_id in answers")

        for alternative in alternatives:
            if alternative['question_id'] == question['question_id']:
                answers.append(alternative['alternative'])
                break

    with open('data/cars.json') as stream:
        cars = json.load(stream)

    for car in cars:
        if answers[0] in car.values() and answers[1] in car.values() and answers[2] in car.values():
            result.append(car)

    return result

def read_result(user_id: int):
    if not validate_positive_integer(user_id):
        raise ValueError("Invalid user_id")

    user_result = []

    with open('data/results.json') as stream:
        results = json.load(stream)

    with open('data/users.json') as stream:
        users = json.load(stream)

    with open('data/cars.json') as stream:
        cars = json.load(stream)

    for result in results:
        if result['user_id'] == user_id:
            for user in users:
                if user['id'] == result['user_id']:
                    user_result.append({'user': user})
                    break

        for car_id in result['cars']:
            for car in cars:
                if car_id == car['id']:
                    user_result.append(car)

    return user_result