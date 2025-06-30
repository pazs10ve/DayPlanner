# Tourist Day Planner

Welcome to the Tourist Day Planner, a proof-of-concept web application designed to help tourists get a quick and personalized one-day plan for any city. Based on the current weather, the app provides a recommendation for indoor or outdoor activities and suggests a complete dining plan powered by the Google Gemini API.


## ✨ Features

- **Dynamic Weather Check:** Fetches real-time weather data for the specified city.
- **Smart Suggestions:** Recommends staying indoors or outdoors based on the weather conditions.
- **AI-Powered Dining Plan:** Generates a full-day dining plan (Breakfast, Lunch, Dinner) using the Google Gemini API, complete with restaurant names and addresses.
- **Sleek & Modern UI:** A visually appealing, responsive interface built with React and modern CSS.
- **RESTful Backend:** A robust backend built with Python and FastAPI to serve the frontend application.

## 🛠️ Tech Stack

- **Frontend:**
  - React
  - TypeScript
  - Vite
  - Axios
  - CSS with modern design principles (Flexbox, Grid, Responsive Media Queries)

- **Backend:**
  - Python
  - FastAPI
  - Uvicorn (for serving the app)
  - Google Gemini API (for AI-powered recommendations)

## 🚀 Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

- Python 3.8+
- Node.js v16+
- A Google Gemini API Key

### Backend Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/pazs10ve/DayPlanner.git
    cd DayPlanner
    ```

2.  **Create a virtual environment and install dependencies:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3.  **Set up your environment variables:**
    Create a file named `.env` in the root directory and add your Gemini API key:
    ```
    GEMINI_API_KEY=your_gemini_api_key_here
    ```

4.  **Run the backend server:**
    ```bash
    python app.py
    ```
    The backend will be running at `http://localhost:8000`.

### Frontend Setup

1.  **Navigate to the frontend directory:**
    ```bash
    cd frontend
    ```

2.  **Install the dependencies:**
    ```bash
    npm install
    ```

3.  **Run the frontend development server:**
    ```bash
    npm run dev
    ```
    The frontend will be running at `http://localhost:5173` (or another port if 5173 is busy).

## Usage

Once both the backend and frontend servers are running, open your browser and navigate to the frontend URL. Enter the name of a city, click "Get Plan," and see your personalized day plan appear!