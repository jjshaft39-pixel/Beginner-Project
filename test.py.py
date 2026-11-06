name = input("What's ya name?: ")
print(f"Wow!! {name} is a  very nice name")
age = input("How old are you?: ")
age_input = int(age)
bot_age = 18
age_difference = age_input - bot_age
age_difference2 = bot_age - age_input
if age_input < bot_age:
    print(f"Oops, turns out I'm {age_difference2} years older than you!!")
else:
    print(f"Oh, nice ... looks like someone is the eldest over here!!")
Colors = "Blue"
color = input("What's ya favorite color?: ")
if color == Colors:
    print("Hehehe, you've really got good taste when it comes to colours")
else:
    print(f"Ugh {color} is an awful to choose!!")  
Statement = "Yes"
Introduction = input("So do you mind if we get to know each other more?: ")
if Introduction == Statement:
    print("Superb")
else:
    print("Aww that's so bad")
Art_3_Boys = ["Barrack", "John", "Jeremiah", "Joshua", "Desire", "Darious", "Daniel", "Mohammed", "Adamu", "Ibrahim", "Clement", "Emmanuel", "Enoch", "Isaac"]
Class = input("What class were you in?: ")
print("Oh, nice ... I could possibly mention some of your classmates")
answer = "Yes"
condition = input("Do you mind if I give it a try?: ")
if condition == answer:
    print("Art 3 students:")
for Spartans in Art_3_Boys:
    print(Spartans)
print("Above are the names of Art 3 Boys!!")
intentions = input("So what you got on ya mind now?: ")
print("Oh, okay ... that's cool")
food = input("What's ya favorite food?: ")
print(f"Cool, I also love {food}!!")