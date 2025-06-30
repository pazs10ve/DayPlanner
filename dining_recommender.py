import os
from dotenv import load_dotenv
from google import genai

class DiningRecommender:
    """
    Provides dining recommendations using the Gemini API.
    """
    def __init__(self):
        load_dotenv()
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found.")
        self.client = genai.Client(api_key=api_key)

    def get_dining_plan(self, city: str) -> str:
        """
        Generates a dining plan for a given city.
        """
        try:
            # Prompt to find top foods
            food_prompt = f"What are the top 5 must-try foods for a tourist in {city}?"
            food_response = self.client.models.generate_content(
                model="gemini-2.5-flash", contents=food_prompt
            )
            top_foods = food_response.text

            # Prompt to find restaurants for these foods
            restaurant_prompt = f"For the following foods in {city}, suggest 3 top-rated restaurants for each:\n{top_foods}"
            restaurant_response = self.client.models.generate_content(
                model="gemini-2.5-flash", contents=restaurant_prompt
            )
            restaurants = restaurant_response.text

            # Prompt to create a dining plan
            plan_prompt = (
                f"Based on the following information for {city}, create a dining plan for a tourist for one day (breakfast, lunch, and dinner).\n\n"
                f"Top foods:\n{top_foods}\n\n"
                f"Recommended restaurants:\n{restaurants}\n\n"
                "The plan should be in a tabular format with the following columns: 'Time' (with values Breakfast, Lunch, Dinner), 'Food', 'Restaurant', and 'Address'. "
                "For the 'Food' column, suggest a specific dish. For the 'Restaurant' and 'Address' columns, provide the name and full address of a suitable restaurant."
                "Don't output anything else"
            )
            plan_response = self.client.models.generate_content(
                model="gemini-2.5-flash", contents=plan_prompt
            )
            
            return plan_response.text

        except Exception as e:
            return f"An error occurred: {e}"



"""
if __name__ == "__main__":
    recommender = DiningRecommender()
    city = "Paris"
    dining_plan = recommender.get_dining_plan(city)
    print(f"Dining plan for {city}:\n")
    print(dining_plan)
"""