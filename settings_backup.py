# Basic settings
rotors = ("I", "II", "III")
reflector = "UKW-B"
ringSettings = "ABC"
ringPositions = "DEF"
plugboard = "AT BS DE FM IR KN LZ OW PV XY"

# Advanced settings
rotor1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
rotor1Notch = "Q"
rotor2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
rotor2Notch = "E"
rotor3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
rotor3Notch = "V"
rotor4 = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
rotor4Notch = "J"
rotor5 = "VZBRGITYUPSDNHLXAWMJQOFECK"
rotor5Notch = "Z"

rotorDict = {"I": rotor1, "II": rotor2, "III": rotor3, "IV": rotor4, "V": rotor5}
rotorNotchDict = {
    "I": rotor1Notch,
    "II": rotor2Notch,
    "III": rotor3Notch,
    "IV": rotor4Notch,
    "V": rotor5Notch,
}

reflectorB = {
    "A": "Y",
    "Y": "A",
    "B": "R",
    "R": "B",
    "C": "U",
    "U": "C",
    "D": "H",
    "H": "D",
    "E": "Q",
    "Q": "E",
    "F": "S",
    "S": "F",
    "G": "L",
    "L": "G",
    "I": "P",
    "P": "I",
    "J": "X",
    "X": "J",
    "K": "N",
    "N": "K",
    "M": "O",
    "O": "M",
    "T": "Z",
    "Z": "T",
    "V": "W",
    "W": "V",
}
reflectorC = {
    "A": "F",
    "F": "A",
    "B": "V",
    "V": "B",
    "C": "P",
    "P": "C",
    "D": "J",
    "J": "D",
    "E": "I",
    "I": "E",
    "G": "O",
    "O": "G",
    "H": "Y",
    "Y": "H",
    "K": "R",
    "R": "K",
    "L": "Z",
    "Z": "L",
    "M": "X",
    "X": "M",
    "N": "W",
    "W": "N",
    "Q": "T",
    "T": "Q",
    "S": "U",
    "U": "S",
}

rotorANotch = False
rotorBNotch = False
rotorCNotch = False
