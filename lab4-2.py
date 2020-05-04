# I Gregory Carroll, student number 000101968, certify that all code submitted is my own work; that I have not copied it from any other source. I also certify that I have not allowed my work to be copied by others.

#GET the string input from user
#STORE value as a

a = float ( input ( "input number for a: " ) )

#GET string input from user
#STORE value as b
b = float ( input ( "input number for b: " ) )

#GET string input from user
#STORE value as c
c = float ( input ( "input number for c: " ) )

#ASSUME that B ** 2 > 4 * A * C
#CALCULATE the result of B - ( B ** 2 - 4 * A * C/2 * A )
formula_1 = b - ( b ** 2 - 4 * a * c)/(2 * a )

#CALCULATE the result of B + ( B ** 2 - 4 * A * C/2 * A )
formula_2 = b + ( b ** 2 - 4 * a * c)/(2 * a )

#STORE the outcome of both forumla_1 and formula_2
outcome = formula_1 > 0 and formula_2 > 0

#PRINT message showing if the outputs of both formulas are positive as true or false
print( "it is" + str( outcome ) + "that formula_1 and formula_2 are positive." )
