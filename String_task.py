# according to the task - we do not need numbers or any other symbols, (we cant capitalise that!) so i excluded them. 
# for best visualisation and readability the quantity of blank spaces decreased to 1    
#       a) Print out the string with only the first letter capitalized.
#       b) Print out the string in all lowercase.
#       c) Print out the string in title case. 
#       d) Print out the string in all uppercase.

Main_str: str
x: int = 0
i: int = 0
print ("Greetings, game accepts only alphabet letters and only one space, other will be ignored!")
while True:
    Erst_str = input("Please, input any string: ")
    Main_str = ""
    i=0
    x=i  
    if len(Erst_str) < 1:
        break
    else:      
        for x in range(i, len(Erst_str)):
            #print(x)
            if Erst_str[x] == " " and Erst_str[x+1] == " ":
                x += 1
            elif Erst_str[x].isalpha() or Erst_str[x] == " ":
                Main_str += Erst_str[x]
        Erst_str = ""
        i = 0
        while Main_str[i] == " ": 
            i += 1
        for x in range (i, len(Main_str)):
            if Main_str[x] == " " and Main_str[x+1] == " ":
                x += 1
            else:
                Erst_str += Main_str[x]
    
        #print ("a)", Main_str.capitalize())
        #print ("b)", Main_str.lower())
        #print ("c)", Main_str.title())
        #print ("d)", Main_str.upper())

        print ("a)", Erst_str.capitalize())
        print ("b)", Erst_str.lower())
        print ("c)", Erst_str.title())
        print ("d)", Erst_str.upper())
    

print ()   
print ("TNX 4 playing")       
print()

