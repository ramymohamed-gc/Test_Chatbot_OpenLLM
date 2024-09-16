# OpenAI Chatbot with Custom Domain

This project is a Python-based chatbot that uses a hosted OpenAI API-compatible model to respond to user inputs. It is designed to interact with a locally hosted or cloud-based model, and the domain is configured via environment variables. The chatbot provides friendly, concise, and helpful responses in real-time.

## Features
- Loads domain and API key from a `.env` file
- Uses OpenAI API for chat completions
- Interactive chat interface
- Supports friendly exit commands (`exit`, `quit`, `bye`)

## Requirements

- Python 3.x
- `openai` package
- `colorama` package
- `python-dotenv` package for loading environment variables

