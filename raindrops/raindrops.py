def convert(number):
    #Conditions
    sound_types = {3 : 'Pling', 5: 'Plang', 7: 'Plong'}
    #Making the sound
    sound = ''.join([sounds for cond, sounds in sound_types.items() if number%cond == 0])
    return sound or str(number)
