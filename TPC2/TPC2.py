# read the input from stdin
input_str = input("")
lower_input = input_str.lower() 

# initialize variables
on = False
total = 0
current_num = ""
current_word = ""

# loop through each character in the input string
for char in lower_input:
    current_word += char

    # check if we're in between "on" and "off"
    if on:

        # check if the character is a digit
        if char.isdigit():
            current_num += char
        else:
            # if we've encountered a non-digit character, add the current number to the total
            if current_num != "": total += int(current_num)
            current_num = ""

        # check if we've encountered "off"
        if "off" in current_word:
            on = False
            current_word = ""
        # check if we've encountered "="
        elif "=" in current_word:
            print(total)
            current_word = ""

    # check if we've encountered "on"
    elif "on" in current_word:
        on = True
        current_word = ""

    # check if we've encountered "="
    elif "=" in current_word:
        print(total)
        current_word = ""