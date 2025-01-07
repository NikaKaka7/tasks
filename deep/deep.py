x = input("What is the answer of...? " )

if x.strip()  == "42":
    print("Yes")
elif x.strip().lower() == "forty-two":
    print("Yes")
elif x.strip().lower() == "forty two":
    print("Yes")
else:
    print("no")
