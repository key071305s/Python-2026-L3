user_favorite_color = ["red", "blue", "green", "black", "white", "yellow"]
user = input("What is your favorite color? ")
ck = user.lower()
check = True
count = 1
for col in user_favorite_color:
    if col == ck:
        print(f"Your color is at index {count} in my list")
        check = False
        break
    count += 1
if check:
    print("Sorry, I could not find your color")
        

