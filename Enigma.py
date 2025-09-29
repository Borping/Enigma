alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rotor1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"

pos = 0     # showing "A"

def reflect(input):
    reflect_table = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ZYXWVUTSRQPONMLKJIHGFEDCBA")
    output = input.translate(reflect_table)
    return output

def invert_wiring(w):
	inv = [""] * 26
	for i, ch in enumerate(w):
		# forward:  index i (A=0..Z=25)  ->  letter ch
		# inverse:  letter ch           ->  index i
		inv[ord(ch) - ord('A')] = chr(i + ord('A'))
	return "".join(inv)

def keypress(input_char):
    # step 1 : get the input and starting pos
    global pos
    input_char = input_char.upper()
    # step 2 : shift the rotor pos (+1)
    pos = (pos + 1) % 26
    print(f"pos: {pos}")

    # step 3 : find input char's position and shift it +1 (T+1=U) + # step 4: find the index of the new char (U = 20)
    shift_in = (alpha.find(input_char) + pos) % 26
    print(f"shift_in: {shift_in}")

    # step 5: index into our rotor at that position (pos20 = a)
    rotor_char = rotor1[shift_in]
    print(f"rotor_char: {rotor_char}")

    # step 6: shift out -1 from our new character (a - 1 = z)
    shift_out = alpha[(alpha.find(rotor_char) - pos) % 26]
    print(f"shift_out: {shift_out}")

    # step 7: reflect our character into a new one (z->a)
    reflected = reflect(shift_out)
    print(f"reflected: {reflected}")

    # step 8. shift our new char +1 (a + 1 = b) + # step 9. find the index of the new char (b = 1)
    shift_in_reverse = (alpha.find(reflected) + pos) % 26
    print(f"shift_in_reverse: {shift_in_reverse}")

    # step 10. index into the inverse of our rotor at that position (pos1 = w)
    inverse_rotor_char = invert_wiring(rotor1)[shift_in_reverse]
    print(f"inverse_rotor_char: {inverse_rotor_char}")

    # step 11. shift out -1 = v
    shift_out_reverse = alpha[(alpha.find(inverse_rotor_char) - pos) % 26]
    print(f"shift_out_reverse: {shift_out_reverse}")
    return shift_out_reverse

def translate(message):
    translation = []
    for char in message:
        translation.append(keypress(char))
    decoded = "".join(translation)
    return decoded

print(translate("ADVYAPLJ"))