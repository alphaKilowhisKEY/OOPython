import json
from pydub import AudioSegment
from pydub.generators import Sine
import os

# Timing configuration for Morse code
DOT_DURATION = 100  # milliseconds
DASH_DURATION = 3 * DOT_DURATION
SYMBOL_SPACE_DURATION = DOT_DURATION
LETTER_SPACE_DURATION = 3 * DOT_DURATION
WORD_SPACE_DURATION = 7 * DOT_DURATION

# Audio configuration
FREQUENCY = 600  # Frequency of the tone for Morse code
SAMPLE_RATE = 44100  # Sample rate for audio


class MorseCode():

    def load_morse_code_dict(self, filename):
        with open(filename, 'r') as file:
            return json.load(file)

    def text_to_morse(self, text, morse_code_dict):
        morse_code = []
        for char in text.upper():
            if char == ' ':
                morse_code.append(' ')
            elif char in morse_code_dict:
                morse_code.append(morse_code_dict[char])
        return ' '.join(morse_code)

    def morse_to_audio(self, morse_code):
        audio = AudioSegment.silent(duration=0)  # Start with an empty audio segment
        for symbol in morse_code:
            if symbol == '.':
                tone = Sine(FREQUENCY).to_audio_segment(duration=DOT_DURATION)
                audio += tone + AudioSegment.silent(duration=SYMBOL_SPACE_DURATION)
            elif symbol == '-':
                tone = Sine(FREQUENCY).to_audio_segment(duration=DASH_DURATION)
                audio += tone + AudioSegment.silent(duration=SYMBOL_SPACE_DURATION)
            elif symbol == ' ':
                audio += AudioSegment.silent(duration=LETTER_SPACE_DURATION)
        audio = audio + AudioSegment.silent(duration=WORD_SPACE_DURATION)
        return audio

    def save_morse_code_audio(self, text, folder, filename, morse_code_dict):

        if not os.path.exists(folder):
            os.makedirs(folder)
        
        morse_code = self.text_to_morse(text, morse_code_dict)
        audio = self.morse_to_audio(morse_code)
        
        file_path = os.path.join(folder, filename)
        audio.export(file_path, format='wav')
        print(f"File saved to {file_path}")