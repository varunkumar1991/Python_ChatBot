from openai import OpenAI

openAI_key = "type key here"

messages = []

client = OpenAI(
    api_key = openAI_key,
)

def completion(message):
    global messages
    messages.append(
        {
            "role" : "user",
            "content" : message,
        }
    )

    chat_completion = client.chat.completions.create( messages=messages, 
                        model="gpt-5.2"
                        )
    message = {
        "role": "assistant",
        "content": chat_completion.choices[0].message.content
    }
    messages.append(message)
    print(f"Sara: {message["content"]}")
    
if __name__ == "__main__":
    print(f"Sara: Hi I am Sara, Your personal assistant. Hom may I help you today?\n")
    while True:
        print("User: ",end=" ")
        user_question = input()
        completion(user_question)