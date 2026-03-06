def dompier_music(switches):
    
    freq_dict = {
        261: "C4", 294: "D4", 329: "E4", 349: "F4",
        392: "G4", 440: "A4", 494: "B4", 523: "C5", 0: "REST"
    }

    decimal_list = []
    notes_list = []

    for item in switches:
        total = 0
        count = len(item) - 1

        for char in item:
            total += int(char) * (2 ** count)
            count -= 1

        decimal_list.append(total)

    for decimal in decimal_list:
        notes_list.append(freq_dict.get(decimal))

    return notes_list