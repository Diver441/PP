Game_str: str
Test_num: int
Num_1: int
Num_2 = 0
while True:
    Inp_str = input("Please, input a number: ")
    
    if not Inp_str.isnumeric():
        if Inp_str.lower() == "stop":
            Inp_str = input("Please confirm the command, or input the number: ")
    if not Inp_str.isnumeric():
        if Inp_str.lower() == "stop":
            print ()
            print("Program exits now, Good Beye!")
            print ()
            break
        else:     
            print ("This is not a number!")
    else:
        Num_1 = int(Inp_str)    
        if Num_1 <= Num_2:
            print ()
            print ("Your game ends Here!!! Ha-Ha-Ha")
            print ()
            break  
        else:
            print ("Go on!")
            Num_2 = Num_1
