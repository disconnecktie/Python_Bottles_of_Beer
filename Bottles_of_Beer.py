def bottles_of_beer():
    try:
        bottles = []
        no_of_bottles = input("How many bottles are on the wall?")
        no_of_bottles = (int(no_of_bottles)) + 1
    except ValueError:
            print("Please enter an actual number!")
    else:
        if no_of_bottles >= 1:
            for i in range(1,no_of_bottles):
                bottles.append(i)

            bottles = bottles[::-1]
            for i in bottles:
                if i > 2:
                    print("%s bottles of beer on the wall, %s bottles of beer on the wall, %s bottles of beer!" % (i, i, i))
                    print("Take one down pass it around, %s bottles of beer on the wall!" % (i-1))
                elif i == 2:
                    print("%s bottles of beer on the wall, %s bottles of beer on the wall, %s bottles of beer!" % (i, i, i))
                    print("Take one down pass it around, %s bottle of beer on the wall!" % (i-1))
                else:
                    print("%s bottle of beer on the wall, %s bottle of beer on the wall, %s bottle of beer!" % (i, i , i))
                    print("Take it down, and pass it around, no more bottles of beer on the wall!")
        else:
            print("Please enter a number greater than 0!")
