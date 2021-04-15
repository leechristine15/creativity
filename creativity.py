
>>> # list of responses is declared
... responses = ['Example 1','Example 2','Example 3']  
>>> 
>>> import random
>>> # prompt the user to input their inspiration
... inspo = raw_input("This program is a creativity in and out machine. You enter a creative moment to inspire someone else, and in return, you get some creative inspiration. \nNow, reflect: What has been a creative moment for you at Harvard? Be as broad or specific as you'd like. This could be a place on campus you felt creative, people who helped tap into your flow, materials that allowed you to innovate, a quote that brought out your inner-artist, a smell that made your imagination wander...:\n")
This program is a creativity in and out machine. You enter a creative moment to inspire someone else, and in return, you get some creative inspiration. 
flect: What has been a creative moment for you at Harvard? Be as broad or specific as you'd like. This could be a place on campus you felt creative, people who helped tap into your flow, materials that allowed you to innovate, a quote that brought out your inner-artist, a smell that made your imagination wander...:    Add new inspiration input here
>>> random_response = random.randint(0,len(responses)-2)
>>> # add the inspiration to the list of responses
... responses.append(inspo)
>>> random_response = random.randint(0,len(responses)-2)
>>> # return a different inspiration to the user
... print(responses[random_response])
Example 1
>>> 
