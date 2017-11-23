def CalculateScore(trajecten):
    m = 0
    t = len(trajecten)
    p = 0


    for traject in trajecten:
        m += traject[1]
        for i in len(traject[0]):
            if traject[0][i] in kritiek:
                if i == 0 or i == len(traject[0]):
                    p += 1
                elif traject[0][i+1] in kritiek:
                    p += 1
                else:
                    p += 2
    score = p*10000 - (t*20 + m/100000)
    return score