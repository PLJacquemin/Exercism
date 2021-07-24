def roman(number):
    #I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000
    ara_num = "%04d"%number
    rom_num = []
    rom_uni = ["M","C","X","I"]
    rom_fif = ["","D","L","V"]
    for n in range(len(ara_num)):
        rom_num.append(int(ara_num[n])*rom_uni[n])
    for r in range(1,len(rom_num)):
        if len(rom_num[r]) == 9:
            rom_num[r] = rom_uni[r]+rom_uni[r-1]
        elif len(rom_num[r]) > 4:
            rom_num[r] = rom_fif[r]+rom_uni[r]*(len(rom_num[r])-5)
        elif len(rom_num[r]) == 4:
            rom_num[r] = rom_uni[r]+rom_fif[r]
    return ''.join(num for num in rom_num)
