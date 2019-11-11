weight = input("Weight:")
units = input("(L)lbs and (K) for kgs:")
if units in ["L","l"]:
    weight = int(weight) * 0.45
    print(f"You are {weight}kg weight")
if units in ["K","k"]:
    weight = int(weight) * 2.2
    print(f"You are {weight} lbs weight")