#Install torch
! pip install torch

#Import necessary libraries
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class Chatbot:
    def __init__(self, model_name="facebook/blenderbot-400M-distill"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        self.conversation_history = []

    def generate_response(self, input_text):
        history_string = "\n".join(self.conversation_history)
        inputs = self.tokenizer.encode_plus(history_string, input_text, return_tensors="pt")
        outputs = self.model.generate(**inputs, max_new_tokens=60)
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
        self.conversation_history.append(input_text)
        self.conversation_history.append(response)
        return response

    def chat(self):
        print("Type 'exit' to end the conversation.")
        while True:
            input_text = input("> ")
            if input_text.lower() == 'exit':
                print("Conversation ended.")
                break
            response = self.generate_response(input_text)
            print(response)

# Example usage
if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.chat()

