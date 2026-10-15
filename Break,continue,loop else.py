# Break
for i in range(1, 6):
    if i == 4:
        break
    print(i)
    # continue
    for i in range(1, 6):
        if i == 3:
            continue
        print(i)
        # loop else
        for i in range(1, 4):
            print(i)
        else:
            print("Loop completed")

