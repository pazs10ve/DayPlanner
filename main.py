from weather_service import WeatherService
from dining_recommender import DiningRecommender

def main():
    """
    Main function to run the Day Planner application.
    """
    city = input("Enter the city you are in: ")

    # 1. Get weather and dining type suggestion
    weather_service = WeatherService()
    weather_data = weather_service.get_weather(city)
    dining_suggestion = weather_service.suggest_dining_type(weather_data)

    print(f"\nWeather in {city}: {weather_data['description']}")
    print(f"Dining suggestion for today: {dining_suggestion} dining.")

    # 2. Get dining plan if outdoor is recommended
    if dining_suggestion == 'outdoor':
        dining_recommender = DiningRecommender()
        dining_plan = dining_recommender.get_dining_plan(city)
        print(dining_plan)
    else:
        print("\nSince indoor dining is recommended, we suggest exploring local indoor markets or ordering in from a highly-rated local restaurant.")

if __name__ == "__main__":
    main()
