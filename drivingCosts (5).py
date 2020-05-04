# I, Gregory Ross Carroll, 000101968, certify that all code submitted is my own work; that I have not copied it from any other source. I also certify that I have not allowed my work to be copied by others.
# This program compares the effect of driving at different speeds 
# on your fuel consumption.  The user will enter the distance of 
# their drive in kilometers and the cost of gas per liter.  The 
# program will report back the cost of doing that drive at
# different speeds.
# dollarsPerL = dollars per liter
# differenceInD = difference in dollars





# milesPerG = miles per gallon
dist = float( input( "How long is your daily drive in Kilometers? " ) )
dollarsPerL = float( input("How much does gas cost per liter? "))
milesPerG = float( input( "What is your car's miles per gallon rating? " ) )

# mpg2kpl = miles per gallon converted to kilometers per hour
# 0.6 mile = 1 Kilometer, 1 US gallon = 3.78 L, approximately
# convert miles per gallon to kilometers per liter
mpg2kpl = milesPerG /0.6 / 3.78

# dist = distance
# dollarsPerDay = dollars per day
# dollarsPerL = dollars per liter
# milage tables start at 55mph, need to convert to kph
dollarsPerDay = dollarsPerL*( dist/mpg2kpl )

# dollarsAt100 = dollars spent at 100 kilometers
# calculations for diving at 100 km/h
dollarsAt100 = round( dollarsPerDay*1.03, 2 )
print( "\nIf you drive at " + str( 60*1.6 )+" km/h it will cost $"+\
str( dollarsAt100 )+" per day" )
print( "That's $"+str( round( dollarsAt100*365.4,2 ) )+" per year.\n" )

# dollarsAt120 = dollars spent at 120 kilometers
# calculations for diving at 120 km/h
dollarsAt120 = round( dollarsPerDay*1.23, 2 )
print( "If you drive at " + str(75*1.6)+" km/h it will cost $"+\
str( dollarsAt120 )+" per day" )
print( "That's $"+str(round(dollarsAt120*365.4,2 ) )+" per year.\n")

# show the difference in cost
print( "That's a difference of " +\
str( round( ( dollarsAt120 - dollarsAt100 ) * 365.4, 2 ) ) +\
" per year to drive 20 km/h faster." )

# calculate the time for the trip
# how many minutes to drive dist at 100 kph?
timeToDriveAt100 = dist * ( 60 / 100 )
# how many minutes to drive dist at 120 kph?
timeToDriveAt120 = dist * ( 60 / 120 )

# calculate and show the difference in time
timeDiff = timeToDriveAt100 - timeToDriveAt120
print( "You save " + str( timeDiff ) + " minutes per day." )
