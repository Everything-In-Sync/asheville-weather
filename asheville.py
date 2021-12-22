print ('Follow the prompts to check or receive weather information ')
checkWeather = input ('Would you like to check the weather? (y/n) ')


if checkWeather == 'n':
    city = input ('Which city would you like to check the weather for? ')


elif checkWeather == 'y':
    email = input ('Which email address would you like to receive weather notifications? ')
    confirmEmail = input ('Your email address is: ' + email + 'is that correct? (y/n? ' )
