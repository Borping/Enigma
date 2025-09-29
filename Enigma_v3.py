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

def make_plugboard(pairs):
	# for example - ["AQ","WS","ED"]
	m = {}
	for p in pairs:
		a, b = p[0].upper(), p[1].upper()
		m[ord(a)] = ord(b)
		m[ord(b)] = ord(a)
	return str.maketrans(m)

PLUGBOARD = make_plugboard(["AJ","SO","XD"])

def plug(char):
	return char.translate(PLUGBOARD)

def reflect(input):
    reflect_table = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "EJMZALYXVBWFCRQUONTSPIKHGD") # Army/Air Force (Enigma I) reflector
    output = input.translate(reflect_table)
    return output

def reflect_cycle(char):
    reflected = reflect(char)
    return reflected

def rotor_cycle(input_char, forward, pos, wiring, inv_wiring):
	# normalize once
	i = alpha.find(input_char.upper())

	if forward:
		# forward: shift-in -> map -> shift-out
		shift_in = (i + pos) % 26
		rotor_char = wiring[shift_in]
		shift_out = alpha[(alpha.find(rotor_char) - pos) % 26]
		return shift_out
	else:
		# backward: shift-in -> inverse map -> shift-out
		shift_in_rev = (i + pos) % 26
		inverse_rotor_char = inv_wiring[shift_in_rev]
		shift_out_rev = alpha[(alpha.find(inverse_rotor_char) - pos) % 26]
		return shift_out_rev


def machine_keypress(ch):
	global r1_pos, r2_pos, r3_pos

	r1_pos = (r1_pos + 1) % 26
	if r2_pos == 4:
		r2_pos = (r2_pos + 1) % 26
		r3_pos = (r3_pos + 1) % 26
	if r1_pos == 16:
		r2_pos = (r2_pos + 1) % 26

	positions = [r1_pos, r2_pos, r3_pos]

	# rotor configs (wiring, inverse, position) — rightmost last
	rotors = [
		(rotor1, rotor1_inv, positions[0]),
		(rotor2, rotor2_inv, positions[1]),
		(rotor3, rotor3_inv, positions[2]),
	]

	# forward pass (left->right)
	out = plug(ch.upper())
	
	for wiring, inv_wiring, pos in rotors:
		out = rotor_cycle(out, True, pos, wiring, inv_wiring)

	# reflector
	out = reflect_cycle(out)

	# backward pass (right->left, same positions in reverse)
	for wiring, inv_wiring, pos in reversed(rotors):
		out = rotor_cycle(out, False, pos, wiring, inv_wiring)

	out = plug(out)
	return out

def translate(message):
    translation = []
    for char in message:
        translation.append(machine_keypress(char))
    decoded = "".join(translation)
    return decoded

print(translate("WGCONVIJQPPKGFTAVL"))