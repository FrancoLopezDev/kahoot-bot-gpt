import openai
from setup import *

openai.api_key = user_key

# Adjust temperature to either increase or decrease the randomness of ChatGPT's responses. 0.0-2.0
# Adjust max_tokens to increase or decrease the length of resposnes
def ChatGPT_conversation(conversation):
    response = openai.ChatCompletion.create(
        model=model_select, messages=conversation, max_tokens=50, temperature=0.1
    )
    conversation.append(
        {
            "role": response.choices[0].message.role,
            "content": response.choices[0].message.content,
        }
    )
    return conversation


def completed_assistant(
    prompt,
    conversation=[
        {"role": "system", "content": "You answer trivia questions"},
        {
            "role": "user",
            "content": "I will provide questions in the following format: Question: example question. Possible Answers: 1. example answer, 2. example Answer, 3. example answer, 4. example answer",
        },
        {
            "role": "user",
            "content": "You are to answer every question with the number corresponding to the correct answer. Only give the number of the answer, nothing else. Never respond with anything other than a number. If you don't know the answer, simply guess a number based on the answers",
        },
        {
            "role": "user",
            "content": "This is an example: Question: How long does it take sunlight to reach the Earth?. 1. 8 minutes, 2. 1 minute, 3. 36 minutes, 4. 4 hours. And you would respond with the number 1",
        },
    ],
):
    conversation.append({"role": "user", "content": prompt})
    conversation = ChatGPT_conversation(conversation)
    return conversation[-1]["content"]
