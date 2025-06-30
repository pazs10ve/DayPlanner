from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from weather_service import WeatherService
from dining_recommender import DiningRecommender

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

weather_service = WeatherService()
dining_recommender = DiningRecommender()

@app.get("/planner/{city}")
def get_day_plan(city: str):
    """
    Provides a day plan for a tourist in a given city, including weather and dining suggestions.
    """
    try:
        weather_data = weather_service.get_weather(city)
        dining_suggestion = weather_service.suggest_dining_type(weather_data)

        response = {
            "city": city,
            "weather": weather_data['description'],
            "dining_suggestion": dining_suggestion,
            "dining_plan": None
        }

        if dining_suggestion == 'outdoor':
            dining_plan = dining_recommender.get_dining_plan(city)
            response["dining_plan"] = dining_plan
        else:
            response["dining_plan"] = "Since indoor dining is recommended, we suggest exploring local indoor markets or ordering in from a highly-rated local restaurant."

        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
