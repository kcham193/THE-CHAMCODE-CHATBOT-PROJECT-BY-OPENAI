import openai




openai.api_key= "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

system_command= '''
act as a chatbot
your name is chambulilo and you are developed  by kasim!
'''

def respond(text: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=[
            {"role": "user", "content": text},
            {"role": "system", "content": system_command},
            ]
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    while True:
        user_input = input("Human: ")
        print(f"Bot: {respond(user_input)}")