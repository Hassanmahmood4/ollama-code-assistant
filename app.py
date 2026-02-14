import requests
import gradio as gr

OLLAMA_URL = "http://localhost:11434/api/generate"

SYSTEM_PROMPTS = {
    "Explain Code": "Explain the following code clearly and simply:",
    "Find Bugs": "Review the following code and point out potential bugs or issues:",
    "Refactor Code": "Refactor the following code to improve readability and performance:",
    "Add Docstrings": "Add proper docstrings and comments to the following code:"
}

AVAILABLE_MODELS = [
    "phi3",
    "gemma3:1b",
    "llama3.2",
    "llama3"
]

def query_ollama(task, code, model_name):
    prompt = f"{SYSTEM_PROMPTS[task]}\n\n{code}"
    payload = {
        "model": model_name,
        "prompt": prompt,
        "stream": False,
        "options": {
            "num_predict": 250
        }
    }

    response = requests.post(OLLAMA_URL, json=payload, timeout=300)
    response.raise_for_status()
    return response.json().get("response", "")

def run_assistant(task, code, model_name):
    if not code.strip():
        return "⚠️ Please paste some code to analyze."
    try:
        return query_ollama(task, code, model_name)
    except Exception as e:
        return f"❌ Error communicating with Ollama: {e}"

with gr.Blocks(title="AI Code Assistant (Ollama + Gradio)") as demo:
    gr.Markdown("# 🧠 AI Code Assistant (Local with Ollama)")
    gr.Markdown("Paste your code, choose a task, and pick a model (speed vs quality).")

    with gr.Row():
        code_input = gr.Code(label="Your Code", language="python")
        output = gr.Textbox(label="AI Response", lines=20)

    with gr.Row():
        task = gr.Radio(
            choices=list(SYSTEM_PROMPTS.keys()),
            value="Explain Code",
            label="Choose Task"
        )
        model_name = gr.Dropdown(
            choices=AVAILABLE_MODELS,
            value="phi3",
            label="Choose Model (Speed vs Quality)"
        )

    run_btn = gr.Button("Run Assistant 🚀")
    run_btn.click(run_assistant, inputs=[task, code_input, model_name], outputs=output)

if __name__ == "__main__":
    print("🚀 Launching AI Code Assistant at http://127.0.0.1:7860")
    demo.launch(inbrowser=True, server_port=7860)