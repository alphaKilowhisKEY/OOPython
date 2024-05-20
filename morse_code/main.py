from morse_code import MorseCode

FOLDER = "morsed"

mc = MorseCode()
morse_code_dict = mc.load_morse_code_dict("morse_dict.json")

user_input = input("Input the text to translate to the Morse Code: ")
file_name = input("Name the file: ")
mc.save_morse_code_audio(user_input, FOLDER, f"{file_name}.wav", morse_code_dict)
