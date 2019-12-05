count = 0
countnd = 0


while count <= 100:
    print(f"{count}, {countnd}")

    if count > 10:
        break

    count += 2
    countnd = countnd + count
    
else:                           # Else doesn't run if there's a break before while ends;
    print("else reached")
print("else reached")           # Print will run even there's a break, bc it's not part of the while.