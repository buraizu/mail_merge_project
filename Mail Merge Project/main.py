#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Letters/starting_letter.txt", mode="r") as starting_letter:
    # print(starting_letter.readlines())
    names = open("Input/Names/invited_names.txt")
    starting_letter_list = starting_letter.readlines()
    for name in names:
        scrubbed_name = name.replace("\n", "")
        new_file = open(f"Output/ReadyToSend/{scrubbed_name}.txt", mode="w")
        for line in starting_letter_list:
            new_file.write(line.replace("[name]", scrubbed_name))
        new_file.close()
