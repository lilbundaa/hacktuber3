def get_gender():
    print("Please enter your gender:")
    gender = input("1. Male\n2. Female\n3. Non-binary\n4. Prefer not to say\nYour choice (1/2/3/4): ")

    if gender == '1':
        confirmation = "You have chosen Male."
    elif gender == '2':
        confirmation = "You have chosen Female."
    elif gender == '3':
        confirmation = "You have chosen Non-binary."
    elif gender == '4':
        confirmation = "You prefer not to say."
    else:
        confirmation = "Invalid choice."

    return confirmation

confirmation_message = get_gender()
print(confirmation_message)
