# 🤖 AI-Study Notes Generator

<p align="center">
  <img src="screenshots/Home_screen.png" alt="Study AI Banner" width="100%" style="border: 2px solid #1a1a1a; border-radius: 8px; box-shadow: 4px 4px 0px 0px #1a1a1a;"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Powered%20By-Ollama%20%2B%20Gemma%203-lightgrey?style=for-the-badge&logo=cpu&logoColor=white&color=262626" alt="Ollama + Gemma 3"/>
  <img src="https://img.shields.io/badge/UI-Custom%20Streamlit-red?style=for-the-badge&logo=streamlit&logoColor=white&color=171717" alt="Custom Streamlit UI"/>
  <img src="https://img.shields.io/badge/Privacy-100%25%20Local%20%26%20Private-green?style=for-the-badge&logo=shield&logoColor=white&color=404040" alt="Privacy First"/>
</p>

---

## 📖 Introduction

**Study AI** is an intelligent, local-first notes synthesis engine designed for serious researchers and students. By combining the processing power of **Ollama** and the efficiency of **Gemma 3 (1B)** with a custom **glassmorphic matte-black** design interface, Study AI provides academic-grade study guides instantly, completely on your local machine.

---

## ✨ Key Features

*   **🔒 Local-First Privacy**: Your inputs never leave your computer. Processing is done entirely locally using Ollama, making it secure for sensitive research.
*   **🎨 Premium Glassmorphism UI**: Beautiful monochromatic dark-mode styling with frosted-glass containers, glowing input borders, and sleek silver-to-white gradients.
*   **🤖 Custom Robot Logo**: Features a custom-coded responsive SVG robot branding logo embedded directly in the dashboard header.
*   **⚡ Real-Time Synthesis**: Distills complex academic subjects into structured study guides (Definitions, Key Points, Examples, Summaries) in seconds.
*   **📝 Markdown Compiler**: Automatically parses and compiles the LLM’s markdown output into clean, structured HTML layouts.
*   **📥 One-Click Export**: Download your synthesized notes instantly as raw text files for easy sharing or importing.

---

## 📸 visual Walkthrough

### 🚀 Home Dashboard
The custom dark dashboard with matte-grey accents and the custom SVG robot logo branding:
![Home Screen](screenshots/Home_screen.png)

### ⚙️ Synthesizing State
Real-time loading feedback while Gemma 3 processes the subject:
![Generating Notes](screenshots/Generating_Notes.png)

### 📚 Note Results & Download
Markdown-compiled notes displayed inside a custom glass container, ready to download:
![Results Screen](screenshots/Results.png)

---

## 🛠️ Installation & Setup

Get Study AI running locally on your machine in just a few minutes.

### 1. Prerequisites
Ensure you have **Python 3.10+** and **Ollama** installed on your system.

*   Download Ollama: [ollama.com/download](https://ollama.com/download)
*   Start Ollama and download the Gemma 3 model:
    ```bash
    ollama pull gemma3:1b
    ```

### 2. Clone and Setup
```bash
# Clone the repository
git clone https://github.com/vedantdubey19/Study_AI.git
cd Study_AI

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install the required dependencies
pip install -r requirements.txt
```

### 3. Run the Application
Start the Streamlit server with telemetry disabled to load the dashboard:
```bash
streamlit run streamlit_app.py --browser.gatherUsageStats false
```
The application will launch automatically in your browser at **`http://localhost:8501`**.

---

## 🧩 Technical Architecture

Study AI connects your local Streamlit frontend with your local Ollama daemon using a client-side python API request. 

```
┌─────────────────┐      Local HTTP Request       ┌────────────────┐
│   Study AI UI   │ ────────────────────────────> │ Ollama Daemon  │
│ (Streamlit App) │ <──────────────────────────── │   (Gemma 3)    │
└─────────────────┘        Markdown Stream        └────────────────┘
```

### Prompt Specification
The LLM is prompted using a structured instruction set to guarantee academic consistency:
```json
{
  "model": "gemma3:1b",
  "messages": [
    {
      "role": "user",
      "content": "Write concise study notes about {topic}.\n\nFormat:\n1. Definition\n2. Key Points\n3. Examples\n4. Summary\n\nKeep the notes easy to understand."
    }
  ]
}
```

---

## 📂 Project Structure

```
Study_AI/
├── screenshots/               # Application UI screenshots
│   ├── Home_screen.png
│   ├── Generating_Notes.png
│   └── Results.png
├── streamlit_app.py           # Core application code & styling
├── requirements.txt           # Python library dependencies
├── README.md                  # Project documentation
└── .gitignore                 # Excluded git configuration files
```

---

## 👥 Author

*   **Vedant Dubey** - [@vedantdubey19](https://github.com/vedantdubey19)

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
