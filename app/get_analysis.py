import requests

def request_log_analysis(query: str, window: int = 60):
    url = "http://127.0.0.1:8000/analyze"
    
    # Matching the AnalysisRequest Pydantic model in your FastAPI app
    payload = {
        "question": query,
        "time_window_minutes": window
    }
    
    print(f"🚀 Analyzing logs for: '{query}'...")
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status() # Raises an error for 4xx or 5xx responses
        
        data = response.json()
        print("\n✨ AI Analysis Results:")
        print("-" * 30)
        print(data)
        print("-" * 30)
        
        
    except requests.exceptions.HTTPError as err:
        print(f"❌ Analysis failed: {err}")

if __name__ == "__main__":
    # Example: Asking the AI about a specific problem
    request_log_analysis(
        query="What is the biggest threat to our system stability right now?",
        window=60
    )