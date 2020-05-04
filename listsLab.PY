# I, Gregory Carroll, student number 000101968, certify that all code
# submitted is my own work; that I have not copied it from any other source.
# I also certify that I have not allowed my work to be copied by others.



def wordlist_1():
    my_list = []
    my_list.sort()

    
    word_list = input("please enter your words: ")
    while word_list != "quit":
        my_list.append(str(word_list))
      
        word_list = input("please enter your words: ('Quit' to exit) ").lower()

    for x in sorted(my_list):
        print(x)




def times_lists():

    n = int(input("input a number between [3,9]: "))
    if n < 3 or n > 9:
        print("That is not between [3,9], try again.")
        times_lists()
    timetable = []
    for x in range(n+1):
  
        temp = []
        for y in range(n+1):
          
            A = y * x
            temp.append(A)
        
        timetable.append(temp)
    
    print(timetable)
    

    for x in timetable:
        for y in x:
            print(str(y), end=" ")
        print("\n")

wordlist_1()           
times_lists() 
                
