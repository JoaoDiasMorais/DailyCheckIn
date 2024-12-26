def Name():
    name = input("What's your name?")
    print("Hi "+name+". How are you doing,good or bad?")
    answer=input()
    if answer=="good":
        print("That's great to hear.")
    else:
        print("I hope you start feeling better soon.")
        
Name()