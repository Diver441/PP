import datetime
hour = datetime.datetime.now().hour
if hour >=18 :
    Gr = "Good Evening,"
else :
    Gr = "Guten Tag,"

Name = input("What is your name? --- ", )
print (Gr, Name)