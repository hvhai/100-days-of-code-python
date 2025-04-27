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
        self.latest_question_index = 0

    def run(self):
        while self.has_more_questions():
            print(f"Question {self.latest_question_index + 1}/{len(self.questions)}")
            quiz_item = self.get_next_question()
            answer = input(quiz_item.question)
            result = self.check_answer(quiz_item, answer)
            print(result)
            print(f"Your current score is {self.score}")
        print(f"You got {self.score} scores")

    def check_answer(self, quiz_item, answer):
        if quiz_item.is_correct(answer):
            self.score += 1
            return "You got it right"
        else:
            return "That's incorrect"

    def get_next_question(self):
        quiz_item = self.questions[self.latest_question_index]
        self.latest_question_index += 1
        return quiz_item

    def has_more_questions(self):
        return self.latest_question_index < len(self.questions)


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
