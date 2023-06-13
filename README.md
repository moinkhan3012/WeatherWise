# WeatherWise
WeatherWise is an intelligent weather-based decision-making app developed using Streamlit. It leverages Langchain and OpenAI to provide personalized responses and recommendations based on the weather conditions of a given location. The app utilizes Google Custom Search Engine and the OpenWeatherMap API to enhance its functionality and deliver comprehensive weather information.

**Try the app here** [Weather Wise](https://moinkhan3012-weatherwise-weather-wise-app-crws21.streamlit.app/)
## Features:
1. **Weather-based Decision-making:** WeatherWise utilizes accurate weather data obtained through the OpenWeatherMap API to predict and provide tailored answers to user queries related to specific activities or events. Whether it's deciding to go outside, plan a picnic, or engage in outdoor sports, WeatherWise offers intelligent recommendations based on real-time weather conditions.

2. **Seamless Integration with OpenAI:** The app integrates the power of OpenAI's advanced natural language processing capabilities to understand user queries accurately. By combining weather information and AI-driven language processing, WeatherWise delivers contextual responses that help users make better decisions.

3. **Comprehensive Weather Information:** WeatherWise utilizes the OpenWeatherMap API to gather detailed weather data including temperature, precipitation, wind speed, humidity, and more. Users can access up-to-date weather information for their current location or search for weather details of other places.

4. **Enhanced Search Capabilities:** The integration of Google Custom Search Engine enables WeatherWise to provide additional information and resources related to user queries. Users can obtain relevant articles, tips, and recommendations for specific activities based on the weather conditions.

5. **User-friendly Interface:** Built on Streamlit, WeatherWise features a user-friendly interface that allows for easy navigation and interaction. Users can input their queries and receive prompt responses, making the app intuitive and accessible.


## Installation
Clone this repository:
```
git clone https://github.com/moinkhan3012/WeatherWise.git
cd WeatherWise
```

Create a virtual environment and install the packages:
```
python -m venv venv_name
source venv_name/bin/activate  # For Windows: venv_name\Scripts\activate
pip install -r requirements.txt
```
## Usage
To run the app, simply execute the following command:
```
streamlit run weather_wise_app.py
```

After running the command, you can access the app through your web browser using the provided URL on your localhost.

By leveraging the power of Langchain, OpenAI, Google Custom Search Engine, and the OpenWeatherMap API, WeatherWise aims to be a reliable and intelligent companion for users, assisting them in making well-informed decisions based on real-time weather conditions.
