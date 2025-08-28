# 🎭 EmotiCrew – AI-Powered Mood Companion  

EmotiCrew is a **modular multi-agent AI system** built with [CrewAI](https://github.com/joaomdmoura/crewai), [LangChain](https://www.langchain.com/), and [OpenAI](https://openai.com/).  
It analyzes user emotions from text, provides **empathetic companionship**, and suggests **personalized self-care activities**.  

## ✨ Features  
- 🎭 **Mood Detection** – Understands emotional tone from user text  
- 🤝 **Companion Agent** – Offers supportive, empathetic responses  
- 🧘 **Self-Care Recommender** – Suggests simple, personalized wellness tips  
- ⚡ **Modular Architecture** – Clean code organization for easy extension  
- 🔐 **Secure Setup** – Environment variables managed via `.env`  


## 📂 Project Structure  
```
emoticrew/
│── agents/ # All AI agents
│ ├── mood_analyzer.py
│ ├── companion.py
│ └── selfcare.py
│
│── tasks/ # Task definitions
│ └── analyze_task.py
│
│── config.py # Loads API key from .env
│── main.py # Entry point
│── requirements.txt # Project dependencies
│── README.md # Project documentation
│── .env # (not committed) API keys & secrets
```
## 🚀 Getting Started  

### 1. Clone the repository  
```bash
git clone https://github.com/bharghavi007/emoticrew.git
cd emoticrew
```
### 2. Create and activate virtual environment (recommended)
```
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```
### 3. Install dependencies
```
pip install -r requirements.txt
```
### 4. Setup environment variables
Create a .env file in the root folder:
```
OPENAI_API_KEY=your_api_key_here
```
### 5. Run the project
```
python main.py
```
## 🧩 Example Output

- User Input:
```
I feel really tired and unmotivated lately. Everything feels dull.
```
- AI Crew Response:
```
1. Mood detected: Low energy, demotivated  
2. Supportive message: It's okay to feel this way sometimes. You're not alone 💙  
3. Self-care suggestion: Try a short walk outside or a quick breathing exercise to reset your energy.  
```

## 📌 Roadmap
- Add more specialized agents (Stress Analyzer, Productivity Coach)

- Web UI integration (Streamlit/Gradio)

- Database for storing user moods over time

- Docker support for easy deployment

## 🤝 Contributing

Contributions are welcome! Please fork this repo, create a new branch, and submit a pull request.

## 📜 License

This project is licensed under the MIT License – see the LICENSE
 file for details.