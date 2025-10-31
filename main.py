import re

# Defining the number of rounds needed
number_of_rounds = 10

# S-Box
s_box = [
    [ "63", "7C", "77", "7B", "F2", "6B", "6F", "C5", "30", "01", "67", "2B", "FE", "D7", "AB", "76" ],
    [ "CA", "82", "C9", "7D", "FA", "59", "47", "F0", "AD", "D4", "A2", "AF", "9C", "A4", "72", "C0" ],
    [ "B7", "FD", "93", "26", "36", "3F", "F7", "CC", "34", "A5", "E5", "F1", "71", "D8", "31", "15" ],
    [ "04", "C7", "23", "C3", "18", "96", "05", "9A", "07", "12", "80", "E2", "EB", "27", "B2", "75" ],
    [ "09", "83", "2C", "1A", "1B", "6E", "5A", "A0", "52", "3B", "D6", "B3", "29", "E3", "2F", "84" ],
    [ "53", "D1", "00", "ED", "20", "FC", "B1", "5B", "6A", "CB", "BE", "39", "4A", "4C", "58", "CF" ],
    [ "D0", "EF", "AA", "FB", "43", "4D", "33", "85", "45", "F9", "02", "7F", "50", "3C", "9F", "A8" ],
    [ "51", "A3", "40", "8F", "92", "9D", "38", "F5", "BC", "B6", "DA", "21", "10", "FF", "F3", "D2" ],
    [ "CD", "0C", "13", "EC", "5F", "97", "44", "17", "C4", "A7", "7E", "3D", "64", "5D", "19", "73" ],
    [ "60", "81", "4F", "DC", "22", "2A", "90", "88", "46", "EE", "B8", "14", "DE", "5E", "0B", "DB" ],
    [ "E0", "32", "3A", "0A", "49", "06", "24", "5C", "C2", "D3", "AC", "62", "91", "95", "E4", "79" ],
    [ "E7", "C8", "37", "6D", "8D", "D5", "4E", "A9", "6C", "56", "F4", "EA", "65", "7A", "AE", "08" ],
    [ "BA", "78", "25", "2E", "1C", "A6", "B4", "C6", "E8", "DD", "74", "1F", "4B", "BD", "8B", "8A" ],
    [ "70", "3E", "B5", "66", "48", "03", "F6", "0E", "61", "35", "57", "B9", "86", "C1", "1D", "9E" ],
    [ "E1", "F8", "98", "11", "69", "D9", "8E", "94", "9B", "1E", "87", "E9", "CE", "55", "28", "DF" ],
    [ "8C", "A1", "89", "0D", "BF", "E6", "42", "68", "41", "99", "2D", "0F", "B0", "54", "BB", "16" ]
]

# Inverse S-Box for decryption
inverse_s_box = [
    ["52", "09", "6A", "D5", "30", "36", "A5", "38", "BF", "40", "A3", "9E", "81", "F3", "D7", "FB"],
    ["7C", "E3", "39", "82", "9B", "2F", "FF", "87", "34", "8E", "43", "44", "C4", "DE", "E9", "CB"],
    ["54", "7B", "94", "32", "A6", "C2", "23", "3D", "EE", "4C", "95", "0B", "42", "FA", "C3", "4E"],
    ["08", "2E", "A1", "66", "28", "D9", "24", "B2", "76", "5B", "A2", "49", "6D", "8B", "D1", "25"],
    ["72", "F8", "F6", "64", "86", "68", "98", "16", "D4", "A4", "5C", "CC", "5D", "65", "B6", "92"],
    ["6C", "70", "48", "50", "FD", "ED", "B9", "DA", "5E", "15", "46", "57", "A7", "8D", "9D", "84"],
    ["90", "D8", "AB", "00", "8C", "BC", "D3", "0A", "F7", "E4", "58", "05", "B8", "B3", "45", "06"],
    ["D0", "2C", "1E", "8F", "CA", "3F", "0F", "02", "C1", "AF", "BD", "03", "01", "13", "8A", "6B"],
    ["3A", "91", "11", "41", "4F", "67", "DC", "EA", "97", "F2", "CF", "CE", "F0", "B4", "E6", "73"],
    ["96", "AC", "74", "22", "E7", "AD", "35", "85", "E2", "F9", "37", "E8", "1C", "75", "DF", "6E"],
    ["47", "F1", "1A", "71", "1D", "29", "C5", "89", "6F", "B7", "62", "0E", "AA", "18", "BE", "1B"],
    ["FC", "56", "3E", "4B", "C6", "D2", "79", "20", "9A", "DB", "C0", "FE", "78", "CD", "5A", "F4"],
    ["1F", "DD", "A8", "33", "88", "07", "C7", "31", "B1", "12", "10", "59", "27", "80", "EC", "5F"],
    ["60", "51", "7F", "A9", "19", "B5", "4A", "0D", "2D", "E5", "7A", "9F", "93", "C9", "9C", "EF"],
    ["A0", "E0", "3B", "4D", "AE", "2A", "F5", "B0", "C8", "EB", "BB", "3C", "83", "53", "99", "61"],
    ["17", "2B", "04", "7E", "BA", "77", "D6", "26", "E1", "69", "14", "63", "55", "21", "0C", "7D"]
]

# RCON values that will be used in the key expansion
rcon = [
    ["01", "00", "00", "00"],
    ["02", "00", "00", "00"],
    ["04", "00", "00", "00"],
    ["08", "00", "00", "00"],
    ["10", "00", "00", "00"],
    ["20", "00", "00", "00"],
    ["40", "00", "00", "00"],
    ["80", "00", "00", "00"],
    ["1B", "00", "00", "00"],
    ["36", "00", "00", "00"]
]

# The matrix that will be used in MixColumns function for encryption
mix_columns_helper = [
    ["02", "03", "01", "01"],
    ["01", "02", "03", "01"],
    ["01", "01", "02", "03"],
    ["03", "01", "01", "02"]
]

# The matrix that will be used in MixColumns function for decryption
inverse_mix_columns_helper = [
    ["0E", "0B", "0D", "09"],
    ["09", "0E", "0B", "0D"],
    ["0D", "09", "0E", "0B"],
    ["0B", "0D", "09", "0E"]
]


# main function and also the main menu of the program, This is the first thing the user will see.
# He has to choose an option to proceed, 1 to encrypt, 2 to decrypt, and 3 to exit. If the user chose any other inputs, he will get an "invalid input" response
def main():
    # keep the program runnning
    while True:
        # prints the main title
        print("~~~~~ Advanced Encryption Standard ~~~~~")

        # asks the user for what he wants to do with the program
        user_option = input("Choose your option:\n1. Encrypt\n2. Decrypt\n3. Exit\n\nYour Option (Choose the number or the name of the option): ").strip().lower()
        
        # check his answer to see if its one of the options or an invalid input. And then proceed with the next step
        match user_option:
            case "1" | "encrypt":
                encryption()
            case "2" | "decrypt":
                decryption()
            case "3" | "exit":
                print("program closed")
                break
            case _: # _ means any other input
                print("Invalid Input")
                continue


# This is the encryption function, it uses all the neccessary building blocks (functions) that I've made so far
# And encrypt the plaintext
def encryption():
    # Encryption steps in AES:
    # Asks for the plaintext and key as hex form
    # Convert them into 4*4 matrices
    # Apply the Key Expansion
    # Apply AddRoundKey on the 2 matrices
    # Start the rounds
    # From round 1 to the one before the last one (For example, if we are running 10 rounds, then 1 to 9)
    # Apply SubBytes
    # Apply ShiftRows
    # Apply MixColumns
    # Apply AddRoundKey
    # Final Round
    # Apply SubBytes
    # Apply ShiftRows
    # AddRoundKey
    # And we got the ciphertext

    # Getting the plaintext and the key as hex using this function that asks the user for plaintext/ciphertext and key
    # Validates the data entered by the user, and return the values
    plaintext, key = get_message_and_key_in_hex("plaintext")
    
    # Converting the plaintext to a 4*4 matrix
    plaintext_matrix = data_to_4_by_4_matrix(plaintext)

    # Printing the plaintext matrix
    print("Plaintext State:")
    print_4_by_4_matrix(plaintext_matrix)

    # Converting the initial key into a 4*4 matrix
    key_matrix = data_to_4_by_4_matrix(key)

    # Printing the initial key matrix
    print("Key[0]:")
    print_4_by_4_matrix(key_matrix)

    # Key Expansion, and putting all the keys in a keys dictionary
    keys_dictionary = key_expansion(key)

    # Converting the first key into a 4*4 matrix
    first_key_as_matrix = data_to_4_by_4_matrix(keys_dictionary[0])

    # Printing Key[0] as a matrix
    print("Initial Key (Key[0]):")
    print_4_by_4_matrix(first_key_as_matrix)

    # Applying AddRoundKey
    state = add_round_key(plaintext_matrix, first_key_as_matrix)

    # Printing the new state
    print("State after the Initial Add Round Key:")
    print_4_by_4_matrix(state)

    # Starting with round 1
    active_round = 1

    # Going from round 1 till the one before the last
    while active_round < number_of_rounds:
        # Printing the the active round number
        print(f"Round {active_round}")
        
        # Applying the S-Box
        # The SubBytes function I made takes a list of bytes, and convert the content of it based on the provided S-Box table
        # For that reason, I can't give it the whole state, I have to give it 1 row at a time, then combine them into a state again
        
        # defining a temporary state
        temp_state1 = []

        # Looping through the state
        for i in range(4):
            # Apply the SubBytes 1 row at a time
            sub_byted_row = sub_bytes(state[i], s_box)

            # And append the resulted row into the temp state
            temp_state1.append(sub_byted_row)

        # Putting the new Sub_Byte state in the main variable
        state = temp_state1

        # Printing the result
        print("State after SubBytes:")
        print_4_by_4_matrix(state)

        # Applying ShiftRows
        # I didn't make a function that takes a full state and shift it
        # I made a function that shifts a single row
        # So I'll loop through the state, and use that function for each row
        
        # defining a temporary state
        temp_state2 = []

        # looping through the state
        for i in range(4):
            # Shift each row with the right amount
            # So if i = 0, we will shift row 0 with 0. which is correct as the first row will not have any shifts
            # i = 1, shift row 1 with 1, and so on
            # Then store the result in a variable
            shifted_row = shift_bytes(state[i], i)

            # And append the shifted row into the temp state
            temp_state2.append(shifted_row)

        # Putting the new shifted state in the main variable
        state = temp_state2

        # Printing the new State
        print("State after ShiftRows: ")
        print_4_by_4_matrix(state)

        # Apply MixColumns
        state = mix_columns(state, mix_columns_helper)

        # Print the result
        print("State after MixColumns:")
        print_4_by_4_matrix(state)

        # Apply AddRoundKey
        # First we need to convert the needed key into a 4*4 matrix as they are all stored as normal texts
        needed_key_as_a_matrix = data_to_4_by_4_matrix(keys_dictionary[active_round])

        # Printing that key as a matrix
        print(f"Key {active_round} (Key[{active_round}]):")
        print_4_by_4_matrix(needed_key_as_a_matrix)

        # Applying the AddRoundKey using the key matrix
        state = add_round_key(state, needed_key_as_a_matrix)

        # Printing the new state
        print(f"State after AddRoundKey {active_round}:")
        print_4_by_4_matrix(state)

        # Incrementing the round counter by 1
        active_round += 1

    # Doing the final round
    print(f"Round {active_round}")
    
    # Applying SubBytes
    # Same process I did before
    # Initializing a new temp variable
    temp_state3 = []

    # Looping through the state
    for i in range(4):
        # Apply the SubBytes 1 row at a time
        sub_byted_row = sub_bytes(state[i], s_box)

        # And append the resulted row into the temp state
        temp_state3.append(sub_byted_row)

    # Putting the new Sub_Byte state in the main variable
    state = temp_state3

    # Printing the the result
    print("State after SubBytes:")
    print_4_by_4_matrix(state)

    # Apply ShiftRows:
    # Same process I did before
    # Initializing a new temp variable
    temp_state4 = []

    # Looping through the state
    for i in range(4):
        # Apply the Shift Row 1 row at a time
        shifted_row = shift_bytes(state[i], i)

        # Append the new value
        temp_state4.append(shifted_row)

    # Store the result in the main variable
    state = temp_state4

    # Printing the result
    print("State after ShiftRows:")
    print_4_by_4_matrix(state)

    # Applying the final AddRoundKey using the same process
    # First we need to convert the needed key into a 4*4 matrix
    needed_key_as_a_matrix = data_to_4_by_4_matrix(keys_dictionary[active_round])

    # Printing that key as a matrix
    print(f"Key {active_round} (Key[{active_round}]):")
    print_4_by_4_matrix(needed_key_as_a_matrix)

    # Applying the AddRoundKey using the key matrix
    state = add_round_key(state, needed_key_as_a_matrix)

    # Printing the result
    print("State after AddRoundKey:")
    print_4_by_4_matrix(state)

    # Printing the ciphertext
    print("Ciphertext:")
    print_4_by_4_matrix(state)


# This is the decryption function, it uses all the neccessary building blocks (functions) that I've made so far
# And decrypt the ciphertext
def decryption():
    # Decryption Steps in AES
    # Ask for the ciphertext and key as hex form
    # Convert them into 4*4 matrices
    # Apply the Key Expansion
    # Apply AddRoundKey on the 2 matrices
    # Start the rounds
    # From round 1 to the one before the last one
    # Apply InverseShiftRows
    # Apply InverseSubBytes
    # Apply AddRoundKey
    # Apply InverseMixColumns
    # Final Round
    # Apply InverseShiftRows
    # Apply InverseSubBytes
    # Apply AddRoundKey
    # And we got the plaintext
    # Another different thing in the decryption is that we use the keys from the last to the first
    # So for example, if we are running 10 rounds, in encryption, we use them from key[0] to key[10]
    # But in decryption, we use them from key[10] to key[0]
    

    # Getting the ciphertext and the key as hex using this function that asks the user for plaintext/ciphertext and key
    # Validates the data entered by the user, and return the values
    ciphertext, key = get_message_and_key_in_hex("ciphertext")
    
    # Converting the ciphertext to a 4*4 matrix
    ciphertext_matrix = data_to_4_by_4_matrix(ciphertext)

    # Printing the ciphertext matrix
    print("Ciphertext State:")
    print_4_by_4_matrix(ciphertext_matrix)

    # Converting the initial key into a 4*4 matrix
    key_matrix = data_to_4_by_4_matrix(key)

    # Printing the initial key matrix
    print("Key[0]:")
    print_4_by_4_matrix(key_matrix)

    # Key Expansion, and putting all the keys in a keys dictionary
    keys_dictionary = key_expansion(key)

    # As we are going backwards with the keys, then we need a key counter
    # And to make the key flexible with any number of rounds, it should be equal to the maximum number of rounds
    # For example, if we have only 1 round to go through.. then we only have 2 key
    # Then we need to access Key[1] first in the initial AddRoundKey
    # Then in the end, we need to access Key[0]
    key_needed = number_of_rounds

    # Converting the last key into a 4*4 matrix
    last_key_as_matrix = data_to_4_by_4_matrix(keys_dictionary[key_needed])

    # Printing the last Key as a matrix
    print(f"Initial Key (Key[{key_needed}]):")
    print_4_by_4_matrix(last_key_as_matrix)

    # Applying AddRoundKey
    state = add_round_key(ciphertext_matrix, last_key_as_matrix)

    # Printing the new state
    print("State after the Initial Add Round Key:")
    print_4_by_4_matrix(state)

    # Starting with round 1
    active_round = 1

    # decrementing the key counter by 1 as we already used the last one
    key_needed -= 1

    # Going from round 1 till the one before the last
    while active_round < number_of_rounds:
        # Printing the active round number
        print(f"Round {active_round}")

        # Apply InverseShiftRows
        # Just like the ShiftRows function can't take a full state, the InverseShiftRows can't too
        # I'll follow the same process I used in encryption which is to loop through the state one row at a time
        # And do InverseShiftRow on each row then put the values in a temp state

        # Defining the temp state
        temp_state1 = []

        # Looping through the state
        for i in range(4):
            # Inverse shift each row with the right amount
            # So if i = 0, we will inverse shift row 0 with 0, which is correct as the first row doesn't have any shifts
            # If i = 1, inverse shift by 1, and so on
            # Then store the result in a variable
            inverse_shifted_row = inverse_shift_bytes(state[i], i)

            # Append the inverse shifted row into the temp state
            temp_state1.append(inverse_shifted_row)

        # Putting the values of temp state1 in the main state variable
        state = temp_state1

        # Printing the new state
        print("State after InverseShiftRow:")
        print_4_by_4_matrix(state)

        # Apply InverseSubBytes
        # The same function I made for the normal SybBytes, can work with the InverseSubBytes
        # I just need to give it the inverse S-Box table to work
        # And just like I mentioned earlier, the SubBytes function can't work with full states
        # So I'll do the InverseSubBytes one row at a time, then combine all the rows into a new temp state

        # Defining a temp state
        temp_state2 = []

        # Looping through the state
        for i in range(4):
            # Apply the InverseSubBytes one row at a time
            inverse_sub_byte_row = sub_bytes(state[i], inverse_s_box)

            # Append the result to the temp state
            temp_state2.append(inverse_sub_byte_row)

        # Putting the values of temp_state2 to the main state variable
        state = temp_state2

        # Printing the result
        print("State after InverseSubBytes:")
        print_4_by_4_matrix(state)

        # Apply AddRoundKey
        # First, we need to convert the needed key into a 4*4 matrix as all the keys are stored as normal hex texts
        needed_key_as_matrix = data_to_4_by_4_matrix(keys_dictionary[key_needed])

        # Printing that key as a matrix
        print(f"Key {key_needed} (Key[{key_needed}]):")
        print_4_by_4_matrix(needed_key_as_matrix)

        # Applying AddRoundKey using the needed key
        state = add_round_key(state, needed_key_as_matrix)

        # Printing the new state
        print(f"State after AddRoundKey {i}:")
        print_4_by_4_matrix(state)

        # Apply InverseMixColumns
        # The MixColumns function I made is usable in the decryption too
        # The only difference is to give it the inverse_mix_columns_helper matrix instead of the normal one
        state = mix_columns(state, inverse_mix_columns_helper)

        # Print the result
        print("State after InverseMixColumns:")
        print_4_by_4_matrix(state)

        # Incrementing the round counter by 1
        active_round += 1

        # Decrementing the key counter by 1
        key_needed -= 1

    # Doing the final round
    print(f"Round {active_round}")

    # Apply InverseShiftRows
    # Same process I did before
    # Initializing the temp state
    temp_state3 = []

    # Looping through the state
    for i in range(4):
        # Apply the InverseShiftRow one row at a time
        inverse_shifted_row = inverse_shift_bytes(state[i], i)

        # Append the result into the temp state
        temp_state3.append(inverse_shifted_row)

    # Put the result in the main state variable
    state = temp_state3

    # Printing the result
    print("State after InverseShiftRows:")
    print_4_by_4_matrix(state)

    # Apply InverseSubBytes
    # Same process I did before
    # Initializing a new temp state
    temp_state4 = []

    # Looping through the state
    for i in range(4):
        # Apply InverseSubBytes one row at a time
        inverse_sub_byte_row = sub_bytes(state[i], inverse_s_box)

        # Append the result in the temp state
        temp_state4.append(inverse_sub_byte_row)

    # Put the final result in the main state
    state = temp_state4

    # Printing the result
    print("State after InverseSubytes:")
    print_4_by_4_matrix(state)

    # Apply the final AddRoundKey
    # Same process as I did before
    # First we need to convert the needed key into a 4*4 matrix
    needed_key_as_matrix = data_to_4_by_4_matrix(keys_dictionary[key_needed])

    # Printing that key as a matrix
    print(f"Key {active_round} (Key[{key_needed}]):")
    print_4_by_4_matrix(needed_key_as_matrix)

    # Apply AddRoundKey with the needed key matrix
    state = add_round_key(state, needed_key_as_matrix)

    # Printing the result
    print("State after AddRoundKey:")
    print_4_by_4_matrix(state)

    # Printing the plaintext
    print("Plaintext:")
    print_4_by_4_matrix(state) 



# get_message_and_key_in_hex is a function that gets the message whether it is a plaintext or a ciphertext, and the key in a 128-bit form.
# This function first asks for the message, do some validation on it to check if, first it's actually in hex, and second if it's the right size.
# Then it asks for the key, and do the same validation to see if it's actually in hex and in the right size.
# If they are actually hex values, the function will return these values.
# If not, the user will need to re-enter the value of the invalid variable.
# This function takes one attribute which is "plaintext_or_ciphertext". This attribute will have a string value and is used to better communicate with the user.
# If the value of this attribute is "plaintext", then the user will be prompted "Please enter the plaintext in hexadecimal form: ".
# And if the value of this attribute is "ciphertext", then the user will be prompted "Please enter the ciphertext in hexadecimal form: ".
def get_message_and_key_in_hex(plaintext_or_ciphertext):
    # Keep asking for the message until the right value is given
    while True:
        message = input(f"Please enter the {plaintext_or_ciphertext} in hexadecimal form: ")

        # validate the value of the message and return the validation result to the "response" variable
        response1 = validate_hex_128bits_input(message)

        # check the value of response1, if the value is "valid", then we got a valid value of the message, and we can proceed with the key
        # If the value of response1 was "invalid", then we will ask again.
        if response1 == "valid":
            break
        else:
            continue
    
    # Keep asking for the key until the right value is given
    while True:
        key = input("Please enter the key in hexadecimal form: ")

        # validate the value of the key and return the validation result to the "response2" variable
        response2 = validate_hex_128bits_input(key)

        # check the value of response2, if the value is "valid", then we got a valid value of the key, and we can proceed
        # If the value of response2 was "invalid", then we will ask again.
        if response2 == "valid":
            break
        else:
            continue
    
    # If the right values were given, return the message and the key to the original function
    return message, key



# This is the validation function, it takes a variable which is either the message, or the key and validates their values entered by the user.
# It checks using regular expression, if the message/key are 128-bits long, which means 32 hex characters.
# And checks if only hex characters were entered, so from 0 to 9, A/a to F/f.
# If these requirements (32 characters and hex values only) were met, then the value is valid, if not, then invalid
def validate_hex_128bits_input(variable_to_validate):
    # the regular expression's function "fullmatch" checks if a variable matches exactly what is specified
    # so here, we are expecting the variable to be 32 characters and containing only hex characters
    if re.fullmatch(r"[0-9a-f-A-F]{32}", variable_to_validate):
        return "valid" # if the variable passes the check, then it is valid
    else:
        return "invalid" # if the variable doesn't pass the check, then it is invalid



# This function takes a string of hexadecimal characters and trasform it into a 4*4 matrix
def data_to_4_by_4_matrix(data_to_convert):
    # converting the string into a list of bytes
    bytes_list = data_to_bytes_list(data_to_convert)
    
    # This is the line that convert the data from a list of bytes to a 4*4 matrix
    # AES uses column major order, so each 4 bytes from bytes_list will be a column and not a row
    # So row 0 will contain bytes 0, 4, 8, and 12. Row 1 will contain bytes 1, 5, 9, 13. Row 2 will contain bytes 2, 6, 19, 14. And finally row 3 will contain bytes 3, 7, 11, 15
    # To achieve this, I used 2 loops, an outer loop "for row in range (4)" to build each row. "range(4)" is equivalent to 3 rows as "4" is excluded
    # The inner loop col in range(4), This is to put the values in each row
    # And finally there is this equation: row + col * 4, this chooses the right byte to put in each row.
    # For example if we are in row 0,
    # col = 0 -> (0 + 0) * 4 = 0 -> Then byte 0
    # col = 1 -> (0 + 1) * 4 = 4 -> Then byte 4
    # col = 2 -> (0 + 2) * 4 = 8 -> Then byte 8
    # col = 3 -> (0 + 3) * 4 = 12 -> Then byte 12
    # That is exactly what we want it
    matrix = [[bytes_list[row + col * 4] for col in range(4)] for row in range (4)]
    
    # Finally return this matrix
    return matrix



# This function takes a string of hexadecimal characters and break it into a list of bytes
def data_to_bytes_list(data_to_convert):
    # This is the conversion line. I defined a list of strings, were each string will contain a byte (2 hex characters).
    # The way it works, is that we are looping inside matrix_to_print in a way (that I will explain) that gets 2 characters at a time, and add it to the list.
    # How is that? let's take this chunk of code first: for i in range(0, len(matrix_to_print), 2)
    # This chunk loops through the matrix_to_print variable from the beginning to the end, but 2 steps at a time.
    # the length of matrix_to_print is 32, so we start at i = 0 in the first iteration. In the second iteration, i = 2, then i = 4, ...
    # Now let's take this chunk of code: matrix_to_print[i:i+2]
    # This slices matrix_to_print two characters at a time. as the second number in slicing is excluded. So for example if we have [0:2] this means that we are gettign the first 2 items, as 2 is excluded.
    # Combining all this together we get:
    # Let's take this as the value of matrix_to_print: 0F0E0D0C0B0A09080706050403020100
    # i = 0, we will take the slice [0:2] of matrix_to_print, which means that the first string in bytes_list will be "0F"
    # Then the loop will jump 2 indexes
    # i = 2, we will take the slice [2:4] of matrix_to_print, which means that the second string in bytes_list will be "0E"
    # And as like that, we will get a list containing 16 bytes as strings.
    bytes_list = [data_to_convert[i:i+2] for i in range(0, len(data_to_convert), 2)]

    # return the list
    return bytes_list



# This function prints a matrix matrix
def print_4_by_4_matrix(matrix_to_print):
    # for each row in the matrix
    for row in matrix_to_print:
        # print each value of each row with a space between them
        print(" ".join(row))

    # Adding extra spaces for better user experience
    print("\n\n")



# This function will handle the key expansion. It will generate all the keys and return all the generated keys in a dictionary
def key_expansion(key):
    # A list that will contains all the words
    words_list = []
    
    # Converting the key into a list of bytes
    bytes_list = data_to_bytes_list(key)
    
    # Dividing the list of Bytes into 4 words.
    # We are looping through the bytes_list, from the begining till the end, 4 items at a time (so 4 bytes a time)
    for i in range(0, len(bytes_list), 4):
        # The word is 4 bytes
        # If i = 0, we will get item 0, 1, 2, and 3 (not 4 as i+4 is excluded)
        word = bytes_list[i:i+4]

        # Put the word inside the words list
        words_list.append(word)

    # Initializing a round counter, starting from 1
    round_number = 1
    # Looping through the process of generating words so that we cover all the rounds
    while round_number <= number_of_rounds:
        # Get the last 4 words from the words_list to generate the next words
        start_index = (round_number - 1) * 4
        needed_words = words_list[start_index:start_index + 4]

        # Generate the 4 new words and store them in these variables
        new_w0, new_w1, new_w2, new_w3 = generate_next_4_words(needed_words, round_number)
        # Put these new words in the words list
        words_list.append(new_w0)
        words_list.append(new_w1)
        words_list.append(new_w2)
        words_list.append(new_w3)

        # Increment the round number by 1 so that we start with the next one
        round_number += 1

    # Initializing a dictionary that will store all the keys
    keys_dictionary = {}
    # Looping through words_list 4 steps at a time
    for i in range (0, len(words_list), 4):
        # This counter gives the 4 words we want for each key
        # Let's say i = 0, then items 0, 1, 2, 3 will result with 0. And these items are the 4 words that makes key[0]
        # i = 1, then items, then items 4, 5, 6, 7 will result with 1. And these items are the 4 words that makes key[1]
        # So counter basically gives the number of key we are in
        counter = i // 4

        # ''.join(word) will join all the content of a word in a single string without any spaces
        # words_list[i:i+4] gets the 4 words we want
        # Let's say i = 0, then this will give us words 0, 1, 2, and 3 (as i+4 is excluded)
        # ''.join(...) will join all the 4 strings that were made into a string without any spaces
        round_key = ''.join([''.join(word) for word in words_list[i:i+4]])

        # Put the value of the key inside it
        keys_dictionary[counter] = round_key

    # Printing the content of the dictionary
    for i in range(len(keys_dictionary)):
        print(f"Key {i}: {keys_dictionary[i]}\n\n")

    # Return the keys to the main function (encryption/decryption)
    return keys_dictionary



# This function will generate the next 4 words and return them
# It takes two arguments, needed_words and round
# needed_words is a list of all the words that will be used to calculate the new words
# round is the round number we are in, it helps for knowing which RCON value we need
def generate_next_4_words(needed_words, round):
    # The rules for calculating the words is
    # K[n]:W[i] = K[n-1]:W[i] XOR K[n]:W[i-1]
    # K[n]:W[0] = K[n-1]:W[0] XOR SubByte(K[n-1]:W3 >> 8) XOR Rcon[i]

    # Splitting the W0 calculation
    # Calculating K[n-1]:W3 >> 8 ------> Let's call it result 1
    w0_1 = shift_bytes(needed_words[3], 2)
    # Calculating SubBytes(result 1) ------> Let's call it result 2
    w0_2 = sub_bytes(w0_1, s_box)
    # Calculating result 2 XOR Rcon[i] ------> Let's call it result 3
    w0_3 = xor_bytes(w0_2, rcon[round-1])
    # Calculating result 3 XOR K[n-1]:W0
    # And just like that we have K[n]:W[0]
    w0 = xor_bytes(w0_3, needed_words[0])

    # Calculating K[n]:W[1] = K[n-1]:W[1] XOR K[n]:W[0]
    w1 = xor_bytes(needed_words[1], w0)
    # Calculating K[n]:W[2] = K[n-1]:W[2] XOR K[n]:W[1]
    w2 = xor_bytes(needed_words[2], w1)
    # Calculating K[n]:W[3] = K[n-1]:W[3] XOR K[n]:W[2]
    w3 = xor_bytes(needed_words[3], w2)

    # Returning the 4 new words
    return w0, w1, w2, w3



# This function shifts a list of bytes by a specific number of times
def shift_bytes(list_of_bytes, number_of_shifts):
    # This line is just to keep things safe.
    # For example, if we are shifting a list of 4 bytes by 5. We don't want an error
    # We will convert the number 5 to a reasonable equivalent number that matches the lenght of the list.
    # So 5 mod 4 = 1. Then we will shift by 1
    number_of_shifts = number_of_shifts % len(list_of_bytes)

    # This line do the shift, then return the new value
    # The way it works is, we are splitting the list of bytes by the correct number to shift it.
    # For example, if we have this list ["A", "B", "C", "D"], and we want to shift by 1
    # Then this list will be split up to ["B", "C", "D"], and ["A"]
    # Then we will merge them as this shape to get ["B", "C", "D", "A"]
    return list_of_bytes[number_of_shifts:] + list_of_bytes[:number_of_shifts]



# This function shifts a list of bytes by a specific number of times in reverse
def inverse_shift_bytes(list_of_bytes, number_of_shifts):
    # This line is just to keep things safe.
    # For example, if we are shifting a list of 4 bytes by 5. We don't want an error
    # We will convert the number 5 to a reasonable equivalent number that matches the lenght of the list.
    # So 5 mod 4 = 1. Then we will shift by 1
    number_of_shifts = number_of_shifts % len(list_of_bytes)

    # This line do the reverse shift, then return the new value
    # The way it works is, we are splitting the list of bytes by the correct number to reverse shift it.
    # For example, if we have this list ["A", "B", "C", "D"], and we want to reverse shift by 1
    # Then this list will be split up to  ["D"], and ["A", "B", "C"]
    # Then we will merge them as this shape to get ["D", "A", "B", "C"]
    return list_of_bytes[-number_of_shifts:] + list_of_bytes[:-number_of_shifts]



# This function will take 2 lists of bytes and XOR them byte by byte then return the new list
def xor_bytes(list_of_bytes_1, list_of_bytes_2):
    # This line does all the trick
    # First "zip(list_of_bytes_1, list_of_bytes_2)" is used to iterate through both lists at the same time, byte by byte
    # Then "int(a, 16) ^ int(b, 16)", for each pair of bytes a and b, we convert them from hex to perform the XOR operation "^"
    # "hex(int(a, 16) ^ int(b, 16))", is converting the result of the XOR to hex again
    # "hex()[2:].zfill(2)" ensures that we format the result as a 2-character string
    # Then return the result
    return [hex(int(a, 16) ^ int(b, 16))[2:].zfill(2) for a, b in zip(list_of_bytes_1, list_of_bytes_2)]



# This function will do the normal and inverse SubByte operation
# It takes two arguments, list_of_bytes which is the list of bytes we want to work with
# And the S-Box we want to use. If we want to encrypt, we use the normal S-Box
# If we want to decrypt, we use the inverse S-Box
def sub_bytes(list_of_bytes, s_box):
    # This line converts the list of bytes into the new values from the given S-Box
    # First it takes the first byte and see its position on the S-Box (row position)
    # Then it takes the second byte and see its position on the S-Box (column position)
    # Then we return the new value that we get from the intersection of row and column
    return [s_box[int(byte[0], 16)][int(byte[1], 16)] for byte in list_of_bytes]



# Add Round Key, this function will take 2 attributes
# The state matrix whether it is the plaintext or ciphertext matrix
# And the key matrix. Do the calculations then return the result in a new matrix
def add_round_key(state_matrix, key_matrix):
    # Initializing the new result matrix
    result_matrix = []

    # As I already implemented a xor function, I don't need to build a new one, so I'll use it
    # The problem is that my xor function xor lists, not whole matrixes
    # For that reason, I'll loop the matrix (as we are working with 4*4 matrixes, we will iterate 4 times)
    # And in each iteration, we will xor the corresponding list of the matrix, and put it in the result matrix
    for i in range(4):
        # Calling the xor function with the correct row to xor
        xored_row = xor_bytes(state_matrix[i], key_matrix[i])

        # Putting the result in the result matrix
        result_matrix.append(xored_row)

    # returning the result matrix
    return result_matrix


# This is the MixColumns function
# It takes 2 attributes, the plaintext/ciphertext state, and the helper matrix (It can work on encryption and decryption)
# It does all the calculation (all the calculations are explained below)
# Then returns the result as a new matrix
def mix_columns(state, helper_matrix):
    # Initialize a new empty 4*4 matrix
    result = [["00"] * 4 for _ in range(4)]

    # In AES encryption/decryption, to get each cell of the new matrix
    # We multiply the column of the state with the row of the helper_matrix (for encryption) and inverse_helper_function (for decryption)
    # For example, we want to calculate cell[0][0]
    # We multiply column 0 from the state, with row 0 from the helper_matrix/inverse_helper_function
    # If we want to calculate cell[2][3]
    # We multiply column 3 from the state with row 2 from the helper_matrix/inverse_helper_function

    # Looping through each column of the state
    # As we are working with 4*4 matrices. Then we do range(4) (from 0 to 3, as 4 is exluded)
    for col in range(4):
        # Grabbing the column and put it in a list of 4 bytes
        column = [state[row][col] for row in range(4)]

        # for each row in the helper_matrix/inverse_helper_function
        for row in range(4):
            # breaking the long calculations into smaller parts
            # For example if we are dealing with
            # (00 * 02) XOR (04 * 03) XOR (08 * 01) XOR (12 * 01)
            # We do them as
            # eq1 = 00 * 02
            # eq2 = 04 * 03
            # eq3 = 08 * 01
            # eq4 = 12 * 01
            # Finally the result will be eq1 XOR eq2 XOR eq3 XOR eq4
            eqs = []

            # looping through the 4 items that we want to do the calculations
            for i in range(4):
                # do the caclculations and store the result in the equation variable
                # So the right byte, with the right item of the helper_matrix/inverse_helper_function
                eq = galois_field_multiplication(column[i], helper_matrix[row][i])

                # Add the result of the equation to the list of equations
                eqs.append(eq)

            # Then XOR all the equations together and put it in the right cell of the new matrix
            result[row][col] = format(
                int(eqs[0], 16) ^ int(eqs[1], 16) ^ int(eqs[2], 16) ^ int(eqs[3], 16), '02X'
            )

    # Finally return this new matrix
    return result



# This is the Galois Feild Multiplication Function.
# It is the one responsible for calculating a byte * 01, 02, or 03 (for example AA * 02)
# It takes 2 arguments, the actual byte (for example, "AA")
# And the number we want to multiply it with (01, 02, and 03)
# I made this function so that we can use in the normal MixColumns and the InverseMixColumns
def galois_field_multiplication(byte, number_in_the_helper_matrix):
    # The rules of this multiplication are:
    # 01: keep the byte unchanged
    # 02: This have 2 cases
    # Case 1:
    # If the first bit of the byte on the left is 0, then we just shift the byte by 1 bit (we remove the 0 from the front, and put at the back)
    # Case 2:
    # If the first bit of the byte on the left is 1, then we remove the 1 from the front, add 0 at the back, then XOR this with 1B
    # 03: Will be divided to (byte * 01) XOR (byte * 02)

    # First, we convert these 2 arguments from hex strings to their equivalent number
    byte = int(byte, 16)
    number_in_the_helper_matrix = int(number_in_the_helper_matrix, 16)
    
    # Initializing the final result
    result_of_multiplication = 0

    # looping through each bit of the number_in_the_helper_matrix which are 8 bits
    # This is to check if we have 01, 02, or 03
    for _ in range(8):

        # If the least significant bit (The first bit on the right) is 1
        # If this is true, in the first iteration, then we are dealing with 01
        # If in the first iteration it was false, then we are dealing with 02
        # If in iteration 1 and 2 this was true, then we are dealing with 03 
        if number_in_the_helper_matrix & 1:
            # Then XOR the byte with the result
            # As the initial value of result is 0, then XORing it with the byte will result with the same byte
            # And if number_in_the_helper_matrix is 01, then this will be the final answer
            result_of_multiplication ^= byte

        # Here I am calculating in case we have *02
        # checking the values of byte with 10000000
        # This is to check if the byte starts with 1 or 0 to better know which case 0f * 02 we are dealing with
        carry = byte & 0x80

        # Shifting the byte by 1 bit as it is case 1 from * 02
        byte <<= 1

        # If there is a carry (so carry is not 00000000), so byte starts with 1, so we are dealing with case 2 of * 02
        if carry:
            # XOR byte with 1B
            byte ^= 0x1B
        
        # This is just to ensure that byte will stay in the 8 bit range
        byte &= 0xFF

        # shift the number_in_the_helper_matrix by 1 bit
        # I did this because we will start the next iteration. And as in each iteration I'm checking the last bit in number_in_the_helper_matrix,
        # I don't want to check the same bit everytime
        # This is like doing counter += 1 in a while loop
        number_in_the_helper_matrix >>= 1

    # retun the result in a Hex format
    return format(result_of_multiplication, '02X')



if __name__ == "__main__":
    main()