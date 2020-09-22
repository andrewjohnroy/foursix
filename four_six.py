collection = []

def four_six(x,y):
    for i in range(x,y+1):
        if i % 4 == 0 or i % 6 == 0:
            collection.append(i)
    print(collection)

four_six(3,12)
