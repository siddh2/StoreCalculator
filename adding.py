# Write a python project which will keep adding a stream of number inputted by the user. The adding stops as soon as user press q key on the keyboard

sum = 0
while(True):
    userInput = input("Enter the item price or press q to quit : \n ")
    if(userInput!='q'):
        sum = sum + int(userInput)
        print(f"Order total so far: {sum}")
        
    else:
        print(f"Your Bill total is {sum}. Thanks for using our calculator")
        break
        