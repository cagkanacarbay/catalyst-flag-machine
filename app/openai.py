import openai

openai.api_key = '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'


def ask_jesus(prompt):
    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                   messages=[{"role": "user", "content": prompt}])

    return chat_completion.choices[0].message.content


# x = ask_jesus("Hello, is there anybody in there?")