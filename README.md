# Enigma
A Python recreation of the WWII German Enigma encryption machine. This repo documents my journey from a single-rotor prototype, to a basic 3-rotor model, finally finishing with a much more sophisticated 3-rotor model with plugboard functionality!

## Features  
- **Historically accurate**: Uses real Commercial Enigma rotor wirings and UKW-A reflector
- **Rotor stepping**: Accurate rotor stepping (right rotor steps every keypress, middle rotor can do the famous "double step")
- **Configurable machine**: Plugboard pairs and rotor starting positions are easily permeable, and rotors can be added/edited/have their orders swapped with ease
- **Generic rotor function**: One rotor function handles forward/backward logic, position offsets, and wiring tables
  
## Installation  

### Prerequisites  
- Python 3.6+

### Setup  

1. Download ```enigma_v3.py```:
- Open the file and click Raw → Save As...
- Or run:
  
   ```sh
   curl.exe -L -o "enigma_v3.py" "https://raw.githubusercontent.com/Borping/Enigma/main/Enigma_v3.py"
   ```  

2. Run the application:  
   ```sh
   python enigma_v3.py
   ```

### Visuals
- **Decryption Output**

![Output](https://i.imgur.com/3skYgKz.png)
