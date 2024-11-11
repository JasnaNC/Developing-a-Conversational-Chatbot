# Developing a Conversational Chatbot

This project implements a simple chatbot using the `transformers` library from Hugging Face. The chatbot leverages a pre-trained model to generate conversational responses based on user input.

## Overview

The `Chatbot` class is designed to provide a conversational agent that can interact with users in a natural language format. It uses the `facebook/blenderbot-400M-distill` model from Hugging Face's `transformers` library. The chatbot maintains a history of the conversation to generate contextually relevant responses.

### 1. Features
- **Natural Language Processing**: Utilizes a pre-trained sequence-to-sequence language model.
- **Conversation History**: Maintains a history of the conversation to provide context-aware responses.
- **Interactive Chat**: Provides an interactive chat interface for user interaction.
  

### 2. Requirements
- Python 3.7+
- torch
- transformers

### 3. Installation
Install the necessary libraries:
```pip install torch transformers  ```

### 4. Model Architecture
The chatbot is based on a Seq2Seq architecture with self-attention mechanisms for context management. It maintains a conversation history to provide coherent responses across multiple conversation turns.

### 5. Results and Limitations
The chatbot performs well for general queries but may struggle with complex or domain-specific topics. The model’s responses are based on pre-existing data and do not update with new information.
