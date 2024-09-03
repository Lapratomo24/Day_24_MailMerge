with open("./Input/Names/invitees.txt") as invitees:
    names = invitees.readlines()

with open("./Input/Letter/sample.txt") as letter:
    text = letter.read()

for name in names:
    stripped_name = name.strip()
    personalised_letter = text.replace("[name]", stripped_name)
    with open(f"./Output/ReadyToSend/letter_for_{stripped_name}", "w") as output:
        output.write(personalised_letter)
