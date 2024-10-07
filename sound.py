import winsound

# Play a simple beep sound
frequency = 1000  # Set Frequency To 1000 Hertz
duration = 500    # Set Duration To 500 ms == 0.5 second

winsound.Beep(32767, 500)
def play_happy_birthday():
    notes = [
        ('G4', 500), ('G4', 500), ('A4', 1000), ('G4', 1000), ('C5', 1000), ('B4', 2000),
        ('G4', 500), ('G4', 500), ('A4', 1000), ('G4', 1000), ('D5', 1000), ('C5', 2000),
        ('G4', 500), ('G4', 500), ('G5', 1000), ('E5', 1000), ('C5', 1000), ('B4', 1000), ('A4', 1000),
        ('F5', 500), ('F5', 500), ('E5', 1000), ('C5', 1000), ('D5', 1000), ('C5', 2000)
    ]
    
    frequencies = {
        'C5': 523, 'D5': 587, 'E5': 659, 'F5': 698, 'G4': 392, 'G5': 784, 'A4': 440, 'B4': 494
    }
    
    for note, duration in notes:
        winsound.Beep(frequencies[note], duration)

play_happy_birthday()