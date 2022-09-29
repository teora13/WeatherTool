# WeatherTool

:sunny: Depending on the selected city, shows the weather and date there in real time 

Desktop app works conjunction with [tkinter](https://docs.python.org/3/library/tkinter.html) module.

Main modules: 
* tkinter - to create the root of application 
* requests - to get requests form [openweathermap](https://openweathermap.org/)

to get and show the full information about current date and time in selected city:
* TimezoneFinder
* pytz
* datetime


Application works through [openweathermap](openweathermap.org) API key. After inserting the required city in search field, app finds information about current weather and gives timezone data there. The application takes latitude and longitude from json and forms its day and time in the information field.

![weather_tool](https://github.com/teora13/WeatherTool/blob/main/weather_tool.gif)


In case of incorrect input, app shows an error and clean up Information Field.

![error](https://github.com/teora13/WeatherTool/blob/main/error.gif)

