print ('Follow the prompts to check or receive weather information')
checkWeather = input ('Would you like to check the weather? (y/n)')
if checkWeather == 'n':
    city = input ('Which city would you like to check the weather for?')
    print (city)
elif checkWeather == 'y':
    email = input ('What email address would you like to receive weather notifications?')
    confirmEmail = input ('You would like to receive weather notifications at') + email + (' . /n')
    confrimEmailNotif = input ('Is that correct? (y/n)')
    
    

# email = input('What is your email address?')
# print('You entered: ' + email)