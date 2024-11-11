# Developing a Conversational Chatbot

This project implements a simple chatbot using the `transformers` library from Hugging Face. The chatbot leverages a pre-trained model to generate conversational responses based on user input.

## Overview

The `Chatbot` class is designed to provide a conversational agent that can interact with users in a natural language format. It uses the `facebook/blenderbot-400M-distill` model from Hugging Face's `transformers` library. The chatbot maintains a history of the conversation to generate contextually relevant responses.

### Features
- **Natural Language Processing**: Utilizes a pre-trained sequence-to-sequence language model.
- **Conversation History**: Maintains a history of the conversation to provide context-aware responses.
- **Interactive Chat**: Provides an interactive chat interface for user interaction.
  

### 2. Requirements
- Python 3.7+
- torch
- transformers

### 3. Installation
Install the necessary libraries:
```bash
pip install torch transformers
python
Copy code
from chatbot import Chatbot
chatbot = Chatbot()
chatbot.chat()
5. Model Architecture
The chatbot is based on a Seq2Seq architecture with self-attention mechanisms for context management.

6. Results and Limitations
The chatbot performs well for general queries but struggles with complex or domain-specific topics.

7. Future Work
Fine-tuning on domain-specific datasets
Multilingual support
Improved context management for long conversations
8. Acknowledgments
This project was developed as part of a study on conversational AI using Large Language Models. Special thanks to Facebook AI for the BlenderBot model.



 
