import openai
import gradio as gr

openai.api_key="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"

def generate_openai_response(prompt):
    completions =openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "user", "content": prompt}
    ]
    )
    message = completions.choices[0].message.content
    return message.strip()

def chatbot(input_text, conversation_history=[]):
    response_text = generate_openai_response(input_text)
    conversation_history.append((input_text, response_text))
    return conversation_history, conversation_history

gr.Interface(fn = chatbot,
             inputs = ["text",'state'],
             outputs = ["chatbot",'state'],
             title="GPT-3.5 turbo Chatbot",
             description="Talk to an AI chatbot powered by OpenAI's GPT-3.").launch(debug = True)