list = [1, 4 , 5, -1, 10]

def extrac_even(list):
    result =[]
    for i in list:
        if i%2 == 0:
            result.append((i))
    return result


print(extrac_even(list))
        

    


