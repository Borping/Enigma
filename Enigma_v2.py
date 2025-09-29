alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

rotor1 = "DMTWSILRUYQNKFEJCAZBPGXOHV"
rotor2 = "HQZGPJTMOBLNCIFDYAWVEUSRKX"
rotor3 = "UQNTLSZFMREHDPXKIBVYGJCWOA"

r1_pos = 0     # showing "A"
r2_pos = 0     # showing "A"
r3_pos = 0     # showing "A"

def invert_wiring(w):
	inv = [""] * 26
	for i, ch in enumerate(w):
		# forward:  index i (A=0..Z=25)  ->  letter ch
		# inverse:  letter ch           ->  index i
		inv[ord(ch) - ord('A')] = chr(i + ord('A'))
	return "".join(inv)

rotor1_inv = invert_wiring(rotor1)
rotor2_inv = invert_wiring(rotor2)
rotor3_inv = invert_wiring(rotor3)


def reflect(input):
    reflect_table = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ZYXWVUTSRQPONMLKJIHGFEDCBA")
    output = input.translate(reflect_table)
    return output

def reflect_cycle(char, *_):
    reflected = reflect(char)
    return reflected

def rotor1_cycle(input_char, forward, pos):
    if forward:
        # step 3 : find input char's position and shift it +1 (T+1=U) + # step 4: find the index of the new char (U = 20)
        shift_in = (alpha.find(input_char) + pos) % 26
        print(f"shift_in: {shift_in}")

        # step 5: index into our rotor at that position (pos20 = a)
        rotor_char = rotor1[shift_in]
        print(f"rotor_char: {rotor_char}")

        # step 6: shift out -1 from our new character (a - 1 = z)
        shift_out = alpha[(alpha.find(rotor_char) - pos) % 26]
        print(f"shift_out: {shift_out}")

        return shift_out

    else:
        # step 8. shift our new char +1 (a + 1 = b) + # step 9. find the index of the new char (b = 1)
        shift_in_reverse = (alpha.find(input_char) + pos) % 26
        print(f"shift_in_reverse: {shift_in_reverse}")

        # step 10. index into the inverse of our rotor at that position (pos1 = w)
        inverse_rotor_char = rotor1_inv[shift_in_reverse]
        print(f"inverse_rotor_char: {inverse_rotor_char}")

        # step 11. shift out -1 = v
        shift_out_reverse = alpha[(alpha.find(inverse_rotor_char) - pos) % 26]
        print(f"shift_out_reverse: {shift_out_reverse}")

        return shift_out_reverse

def rotor2_cycle(input_char, forward, pos):
    if forward:
        # step 3 : find input char's position and shift it +1 (T+1=U) + # step 4: find the index of the new char (U = 20)
        shift_in = (alpha.find(input_char) + pos) % 26
        print(f"shift_in: {shift_in}")

        # step 5: index into our rotor at that position (pos20 = a)
        rotor_char = rotor2[shift_in]
        print(f"rotor_char: {rotor_char}")

        # step 6: shift out -1 from our new character (a - 1 = z)
        shift_out = alpha[(alpha.find(rotor_char) - pos) % 26]
        print(f"shift_out: {shift_out}")

        return shift_out

    else:
        # step 8. shift our new char +1 (a + 1 = b) + # step 9. find the index of the new char (b = 1)
        shift_in_reverse = (alpha.find(input_char) + pos) % 26
        print(f"shift_in_reverse: {shift_in_reverse}")

        # step 10. index into the inverse of our rotor at that position (pos1 = w)
        inverse_rotor_char = rotor2_inv[shift_in_reverse]
        print(f"inverse_rotor_char: {inverse_rotor_char}")

        # step 11. shift out -1 = v
        shift_out_reverse = alpha[(alpha.find(inverse_rotor_char) - pos) % 26]
        print(f"shift_out_reverse: {shift_out_reverse}")

        return shift_out_reverse

def rotor3_cycle(input_char, forward, pos):
    if forward:
        # step 3 : find input char's position and shift it +1 (T+1=U) + # step 4: find the index of the new char (U = 20)
        shift_in = (alpha.find(input_char) + pos) % 26
        print(f"shift_in: {shift_in}")

        # step 5: index into our rotor at that position (pos20 = a)
        rotor_char = rotor3[shift_in]
        print(f"rotor_char: {rotor_char}")

        # step 6: shift out -1 from our new character (a - 1 = z)
        shift_out = alpha[(alpha.find(rotor_char) - pos) % 26]
        print(f"shift_out: {shift_out}")

        return shift_out

    else:
        # step 8. shift our new char +1 (a + 1 = b) + # step 9. find the index of the new char (b = 1)
        shift_in_reverse = (alpha.find(input_char) + pos) % 26
        print(f"shift_in_reverse: {shift_in_reverse}")

        # step 10. index into the inverse of our rotor at that position (pos1 = w)
        inverse_rotor_char = rotor3_inv[shift_in_reverse]
        print(f"inverse_rotor_char: {inverse_rotor_char}")

        # step 11. shift out -1 = v
        shift_out_reverse = alpha[(alpha.find(inverse_rotor_char) - pos) % 26]
        print(f"shift_out_reverse: {shift_out_reverse}")

        return shift_out_reverse

def machine_keypress(input):
    global r1_pos, r2_pos, r3_pos

    path = [rotor1_cycle, rotor2_cycle, rotor3_cycle]

    # reverse_path = list(reversed(path))
    r1_pos = (r1_pos + 1) % 26 # shift rotor 1 each keypress

    if r2_pos == 4:
        r2_pos = (r2_pos + 1) % 26
        r3_pos = (r3_pos + 1) % 26
        print("e") # showing E
    if r1_pos == 16:
        print("q") # showing Q
        r2_pos = (r2_pos + 1) % 26

    positions = [r1_pos, r2_pos, r3_pos]

    # forward pass
    out = input.upper()
    for i, cycle in enumerate(path):
        out = cycle(out, True, positions[i])

    out = reflect_cycle(out)
    
    # backward pass
    path = [rotor1_cycle, rotor2_cycle, rotor3_cycle]
    for i, cycle in enumerate(reversed(path)):
        out = cycle(out, False, positions[-1 - i])  # <-- note positions[-1 - i]

    return out

def translate(message):
    translation = []
    for char in message:
        translation.append(machine_keypress(char))
    decoded = "".join(translation)
    return decoded


print(translate("RXHHYMLKNKHGMXWFMLJ"))
