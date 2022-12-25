# LineBot_Weather_and_Constellation_Forecast
## Content
1. [About the project](#Abouttheproject)
2. [Environment](#Environment) 
3. [Technics](#Technics) 
4. [Getting Started](#GettingStarted) 
5. [Feature](#Feature)
6. [FSM](#FSM) 
7. [State](#State) 
8. [Demo](#Demo) 
  
## About the project

This is a line bot that you can ask it some things like the weather forecast for parts of Taiwan and today's horoscope forecast. And the information of it got was from the website.

## Environment
- Python 3.7.9

## Technics
- line bot : Built by the official LINE Messaging API.
- Backend : Built the backend with Flask to handle the webhook.
- FSM : Create FSM with pytransitions for the users state management.
- Scraping : Use crawlers to get the required information from the website.
- Imgur & Opendrive : Use to store the image and vedio

## Getting Started
- Type the command "主選單" to start Line bot
- Main menu
- ![](https://i.imgur.com/V7CeyyI.jpg) 

## Feature 
* You can select a category. Then you will be transited to the desired state and get the information you want.
    * Weather forecast
* ![](https://i.imgur.com/B3ME1ro.png)
    * Horoscope divination
* ![](https://i.imgur.com/TK6wryt.png)

## FSM
- ![](https://i.imgur.com/JtsVktX.png)

## State
- user : It is the initial state, no message will appear, you can use text "主選單" to send to the main menu.
- main menu : In this state, you can choose what function to do.
- weather menu : You will get information of weather and temperature. It is triggered from main menu.
- predict menu : You will get information of horoscope, blood type or divination. It is triggered from main menu.
- weather : Get imformation of weather in the specific area.
- temp : Get imformation of temperature in the specific area.
- song : Get some music about the weather.
- pray : Get about praying for rain.
- star menu : Choose what you want to know about constellations.
- blood menu : Choose what you want to know about blood type.
- divination menu : Choose what you want to know about the type of divination.
- leave : After printing the goodbye and best wishes message, go back to user.

## Demo
![](https://i.imgur.com/DapY3n1.png)  

![](https://i.imgur.com/HjTJl13.png)  

![](https://i.imgur.com/IS9ycrt.png)  

![](https://i.imgur.com/fpDHgwx.png)  

![](https://i.imgur.com/xCqojo2.png)  

![](https://i.imgur.com/ONFwqDq.png)  

![](https://i.imgur.com/r4c8cE9.png)  

![](https://i.imgur.com/HD4aAt5.png)  

![](https://i.imgur.com/Y1JUt6G.png)  

![](https://i.imgur.com/i1EqvCj.jpg)

![](https://i.imgur.com/f3uwUbj.png)  


![](https://i.imgur.com/ZoyUOJx.jpg)








