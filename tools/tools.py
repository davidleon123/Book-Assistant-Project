from book_assistant.ai_module.db_handler import load, answer_question, load_answer, display_answer, save_answer
from book_assistant.ai_module.logger import log_question

questions = ["what is a javascript closure?",
            "how do I create a timestamp with javascript?",
            "what is a list in javascript",
             "how to get started with javascript?",
             "how to use CSS with javascript?",
             "how to reverse an array?",
             ]
question = questions[1]


def main() -> None:
    print(question)
    log_question(question)
    answer = answer_question(question)
    display_answer(answer)
    save_answer(answer)
    # saved_answer = load_answer()
    # display_answer(saved_answer)
    

if __name__ == "__main__":
    main()