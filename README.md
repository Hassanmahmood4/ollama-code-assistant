🧠 AI Code Assistant (Local LLM with Ollama + Gradio)

A privacy-friendly AI Code Assistant that helps developers understand, debug, refactor
and document code using locally hosted Large Language Models via Ollama. No cloud APIs, 
no data leaving your machine.


✨ Features
	•	🔍 Explain code (Python-focused, works for other languages too)
	•	🐛 Find bugs & potential issues
	•	🛠 Refactor code for readability & performance
	•	📝 Auto-generate docstrings and comments
	•	⚡ Fast local inference using lightweight models (e.g., phi3)
	•	🔁 Switch between multiple local LLMs (speed vs quality)
	•	🌐 Clean web UI built with Gradio


🖥️ Demo

<img width="1081" height="638" alt="image" src="https://github.com/user-attachments/assets/2c0aa57b-2a2e-4dee-9e01-ecb32ead7456" />



🧰 Tech Stack
	•	Python 3.9+
	•	Ollama (local LLM server)
	•	Gradio (web UI)
	•	Requests (HTTP client)


🚀 Getting Started

1️⃣ Install Ollama

Download and install Ollama:
👉 https://ollama.com

Pull a fast model (recommended):

ollama pull phi3

Other supported models (optional):

ollama pull llama3
ollama pull gemma3:1b

Make sure Ollama is running (it usually runs as a background service on macOS).


2️⃣ Clone the Repository

git clone https://github.com/<your-username>/ollama-code-assistant.git
cd ollama-code-assistant



3️⃣ Set Up Python Environment

python3 -m venv .venv
source .venv/bin/activate

Install dependencies:

pip install -r requirements.txt


4️⃣ Run the App

python app.py

The app will automatically open in your browser at:

http://127.0.0.1:7860


⚙️ Configuration

You can change the default model in app.py:

MODEL_NAME = "phi3"   # fast
# or
MODEL_NAME = "llama3" # higher quality, slower

You can also limit output length for faster responses:

"options": {
    "num_predict": 250
}



📁 Project Structure

ollama-code-assistant/
├── app.py              # Gradio app + Ollama integration
├── requirements.txt   # Python dependencies
├── README.md          # Project documentation
└── .gitignore


🧠 How It Works (High-Level)
	1.	User pastes code into the web UI
	2.	The app builds a task-specific prompt
	3.	Prompt is sent to Ollama’s local LLM API
	4.	The model generates a response
	5.	The response is displayed in the UI

All processing happens locally on your machine.

🛣️ Roadmap / Future Improvements
	•	⚡ Streaming responses (typewriter effect)
	•	📄 Upload .py or .js files directly
	•	🧪 Generate unit tests
	•	🧠 Multi-file context support
	•	💾 Save conversation history
	•	🧩 VS Code plugin integration


🤝 Contributing

Contributions are welcome!
Feel free to open issues or submit pull requests for improvements and new features.


🙌 Acknowledgements
	•	Ollama for enabling local LLMs
	•	Gradio for the simple and elegant UI
