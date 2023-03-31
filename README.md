# savant

# Hello, there! This project uses the 'requests' module to scrape the web for the desired data. The data comes from Baseball Savant and it represents 
# available hitting data from 2015-2022. My goal was to create a model to fairly accurately predict the result of a batted ball event (BBE) for a given 
# launch angle (LA) and exit velocity (EV). However, the way they have the data presented, it is only available by displaying results based solely on 
# LA or EV. In order to (eventually) produce a model predicting outcomes based on two variables, I needed to develop a method to concatenate the 
# information into a single file where a single data point could be isolated from just knowing the LA and EV of the event.  

# Below are some definitions explaining some of the acronyms and baseball jargon utilized in my project.

# BATTED BALL EVENT (BBE) --- any swing which results in contact occuring that produces a result
# EXIT VELOCITY --- the speed at which the baseball leaves the bat after contact (in MPH)
# LAUNCH ANGLE --- the angle at which the baseball leaves the bat after contact (in degrees)
# WEIGHTED ON-BASE AVERAGE (wOBA) --- wOBA is a version of on-base percentage that accounts for how a player reached base -- instead of simply 
#                                     considering whether a player reached base. The value for each method of reaching base is determined by how much 
#                                     that event is worth in relation to projected runs scored (example: a double is worth more than a single). 
