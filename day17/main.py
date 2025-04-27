import html
import requests


class QuizItem:
    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def is_correct(self, answer):
        """
        docstring
        """
        return answer == self.correct_answer


class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def run(self):
        for index, item in enumerate(self.questions):
            print(f"Question {index + 1}/{len(self.questions)}")
            answer = input(item.question)
            if item.is_correct(answer):
                print("You got it right")
                self.score += 1
            else:
                print("That's incorrect")
            print(f"Your current score is {self.score}")
        print(f"You got {self.score} score")


def load_question():
    url = "https://opentdb.com/api.php?amount=10&type=boolean"
    response = requests.get(url)

    if (response.status_code == 200):
        body = response.json()
        return [QuizItem(html.unescape(item["question"]), item["correct_answer"]) for item in body["results"]]
    else:
        print("error call")
        return []


if __name__ == "__main__":

    game = QuizGame(questions=load_question())
    game.run()
