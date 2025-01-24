def Name():
    name = input("What's your name?")
    print("Hi "+name+". How are you doing,good or bad?")
    answer=input()
    if answer=="good":
        print("That's great to hear.")
    else:
        print("I hope you start feeling better soon.")
    response = str(input("Do you want to play a game? yes or no."))
    if response=="yes":
        print("Ok, lets play a game.")
        game = int(input("Think of a whole number from 1-10."))

        import random

        list1=[1,2,3,4,5,6,7,8,9,10]
        tries=0
        while True:
            tries=tries+1

            guess=random.choice(list1)
            print("I think that your number is ",guess)
            if guess==game:
                print("Hooray, I got it right!")
                print("It only took me",tries,"tries")
                break
            else:
                print("Oh, I got it wrong.")

    else:  
        print("Ok, maybe next time.")

Name()