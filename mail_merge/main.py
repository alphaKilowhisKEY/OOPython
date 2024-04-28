PLACEHOLDER = "[name]"

# reading the list of names and saving into list
with open("Input/Names/invited_names.txt", mode="r") as names_file:
    names = names_file.readlines()

# reading the letter file and creating individual letters
with open("Input/Letters/starting_letter.txt", mode="r") as letter_file:
    letter = letter_file.read()

    for name in names:
        stripped_name = name.strip()
        new_letter = letter.replace(PLACEHOLDER, stripped_name)

        with open(f"./Output/ReadyToSend/for_{stripped_name}_letter.txt", mode="w") as new_file:
            new_file.write(new_letter)
