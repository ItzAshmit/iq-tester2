i = 0
i = float(i)
print("Welcome to IQ TESTER ")
print("RULES - 1 don't cheat! 2 always answer with 1 letter capital and others are small")
print("So in this i will provide you some simple questions. if you answer correctly you get a point but if your answer will not correct then you will not get a single point")
m = input("Are you ready. ")
if m == "Yes":
     print("So lets begin")
     q = input(" * If a car travels at 60 miles per hour, how far will it go in 7/22 hours?. find only two decimal places ")
     if q == "19.09":
        print("correct! thats a point for you")
        i += 10
     else:
        print("naa thats wrong the correct answer is 19.09")
     u = input("* What is the opposite of 'rare'?.   ")
     if u == "Common":
        print("hmm.. i think you are smart because this is also correct ")
        i += 10
     else:
       print("noo thats one worng the correct answer is Common")
     g = input("* Is there can be a object that has a beginning but not end? Answer in Yes/No.  ")
     if g == "No":
        print("OMG that's is correct.")
        i += 10
     else:
        print("ohh that's worng the correct is No")
     c = input(" * What is the capital of France?   ")
     if c == "Paris":
       print("brother how is your gk that good")
       i += 10
     else:
       print("thats not a point for you, the correct asnwer is Paris")
     d = input("* You have a jar filled with pennies. You take out half of the pennies. Then, you put back 5 pennies. Finally, you take out half of the remaining pennies. If there are 15 pennies left in the jar, how many pennies were in the jar originally? Hint: Work backwards from the final number of pennies to determine the starting amount. Make sure only to type the numerical values*   ")
     if d == "50":
       print("don't tell me that you are all rounder in all subjects")
       i += 10
     else:
       print("I think you are not good at math. The correct answer is 50 pennies")
     z = input("* What is the square root of 144?   ")
     if z == "12":
       print("okay, you are smart! ")
       i += 10
     else:
       print("okay, you have to go to school dude!")
     x = input("* What is the chemical compound that gives blood its red color? check your spelling 2 times! ")
     if x == "Hemoglobin":
        print("ahhhh.... you scientist")
        i += 10
     else:
       print("Why did you forget to go to science class")
     t = input("* What is the only country in the world that is entirely located south of the Tropic of Capricorn?   ")
     if t == "Australia":
       print("In Gk Also!!")
       i += 10
     else:
       print("Go outside!!")
     z = input("* What is the binary representation of the decimal number 10?   ")
     if z == "1010":
       print("You have to be the son of Albert Einstein.")
       i += 10
     else:
       print("I think you can't afford a computer.")
     b = input("I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. Who am I.  ")
     if b == "Map":
      print("Really, this is the hardest i have fonded")
      i += 10
     else:
       print("okay, this is a hard one!")
     k = input("can you tell me your age to find your IQ.  ")
     k = float(k)
     print(f"your total score is {i}")
     print("so your persentage is....")
     print(f"{(i/k)*10}% out of 100")
if "No" == m:
  print("Ok bye!")
else:
    print("Restart the program then answer in Yes or No to Start again")
print("bye")
