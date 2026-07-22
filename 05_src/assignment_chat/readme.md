### Movie and Weather Assistant

* This project implements a chatbot with a friendly tone. It provides three services: current Toronto weather (Open-Meteo API),  movie recommendations by topic using ChromaDB, and function calling to select the appropriate service based on the user’s request.

* The movie dataset contains a reproducible sample of 500 films from the TMDB dataset. The Gradio interface keeps the conversation history during the session. 

* Guardrails block requests about cats or dogs, horoscopes or zodiac signs, Taylor Swift, and attempts to reveal or modify the system prompt.

# selected chatbot: 
### Weather Service
The chatbot uses the Open-Meteo API to retrieve weather data. The API does not require authentication and supports HTTPS and CORS.
Free weather API — forecasts to archives, no sign-up