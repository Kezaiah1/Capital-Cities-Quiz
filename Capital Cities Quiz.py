#1. Defining my Quiz data
def get_Capital_Cities_Quiz_data():
    print("Hey there! Welcome to the Capital Cities Quiz!\n")
    print("Here are some few instructions to note:\n")
    print("1.A variety of questions will be asked based on Capital cities of selected countries.\n")
    print("2.Right beneath the question,Type your answer and press ENTER.\n")
    print("3.Your answer will be checked and you'll receive feedback.\n")
    print("4.Your overall score and percentage will be displayed at the end.\n")
    print("Do not be worried if you do not get all answers right.Remember the goal is to HAVE FUN!\n")
    print("Let's Get Started!\n")

    return {
        "Question1": {
            "question": "What is the capital of France?",
            "answer": "Paris"
        },
        "Question2": {
            "question": "What is the capital of Germany?",
            "answer": "Berlin"
        },
        "Question3": {
            "question": "What is the capital of Italy?",
            "answer": "Rome"
        },
        "Question4": {
            "question": "What is the capital of Spain?",
            "answer": "Madrid"
        },
        "Question5": {
            "question": "What is the capital of Portugal?",
            "answer": "Lisbon"
        },
        "Question6": {
            "question": "What is the capital of Switzerland?",
            "answer": "Bern"
        },
        "Question7": {
            "question": "What is the capital of Austria?",
            "answer": "Vienna"
        }
    }


#2. Initializing the score to start with a variable initialized to 0
def initial_score():
    return 0


#3. Implementing the logic in the quiz
def start_capital_cities_quiz(quiz):
    score = initial_score() 
    for key,value in quiz.items():
        print(value["question"])
        user_answer = input("Your answer: ").capitalize()

        if user_answer == value["answer"]:
            print("⭐ Correct! ⭐")
            score += 1
        else:
            print(f"Wrong! The correct answer is {value['answer']}.")

        print(f"Current score: {score}\n")
    return score


#4. Display of final results
def show_results(score, total_quiz_questions):
    print(f"You answered {score} out of {total_quiz_questions} questions correctly.")
    score_percentage = (score / total_quiz_questions) * 100
    print(f"Your score percentage is {score_percentage:.1f}%")


#5. important funtion defines the important funtion that makes the whole process of the quiz work.
def important():
    quiz = get_Capital_Cities_Quiz_data()
    score = start_capital_cities_quiz(quiz)
    total_quiz_questions = len(quiz)
    show_results(score, total_quiz_questions)


show=important()
print(show)
