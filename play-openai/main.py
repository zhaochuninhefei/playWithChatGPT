# This is a sample Python script.
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def testGpt():
    print("testGpt...")

    question = "Who is the second best player in NBA history?"
    print("question: " + question)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who is the best player in NBA history?"},
            {"role": "assistant", "content": "Michael Jordan"},
            {"role": "user", "content": question}
        ]
    )

    print(response)

    print("")
    print("answer:" + response["choices"][0]["message"]["content"])

def askAndAnwser():
    while True:
        question = input("我: ")

        if question.lower() == "quit":
            break

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ]
        )

        print()
        print("openAI API:" + response["choices"][0]["message"]["content"])
        print()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # testGpt()
    askAndAnwser()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
