import random
tup=("rock","paper","scissor")
game=True
usercount=0
comptcount=0
tie=0
while game:
    compt=random.choice(tup)
    user=input("Enter your move:")    
    if user not in tup:
        print("Enter valide move")
    else:
        if user==compt:
            print(f"computer choice:- {compt}")
            print("Game Tie")
            tie+=1
        elif user=="stone" and compt=="scissor":
            print(f"computer choice:- {compt}")
            print("You won")
            usercount+=1
        elif user=="paper" and compt=="rock":
            print(f"computer choice:- {compt}")
            print("You won")
            usercount+=1
        elif user=="scissor" and compt=="paper":
            print(f"computer choice:- {compt}")
            print("You won")
            usercount+=1
        else:
            print(f"computer choice:- {compt}")
            print("YOu loose")
            comptcount+=1
        print(f"user-count:-{usercount} computer:-{comptcount} tie:-{tie}")
        out=input("Do you want to quit (Y/N):")
        if(out=="Y" or out =="y"):
            game=False
    