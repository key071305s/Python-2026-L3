def remove_dollar_sign(s):
    return s.replace("$", "")


s = input("Money: ")
print("Price: ", remove_dollar_sign(s))