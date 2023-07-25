import openai
from settings import constants

openai.api_key = constants["OPENAI_APIKEY"]


def ask_jesus(prompt):
    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                   messages=[{"role": "user", "content": prompt}])

    return chat_completion.choices[0].message.content


# x = ask_jesus("Hello, is there anybody in there?")