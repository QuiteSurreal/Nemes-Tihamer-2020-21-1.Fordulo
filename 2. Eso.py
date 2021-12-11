from sys import stdin, stdout
def main():
    eso = []
    hanynap = int(stdin.readline())
    intervallum = 0
    maxintervallum = 0
    inteleje = 0
    intvege = 0
    esett = 0
    eso.append(list(map(int, stdin.readline().split())))
    for i in range(hanynap):
        intervallum = 1
        esett = 1
        if eso[0][i] <= 0:
            continue
        for j in range(i+1, hanynap):
            if eso[0][j] > 0:
                intervallum += 1
                esett += 1
                if esett/intervallum >= 0.5:
                    if intervallum > maxintervallum:
                        maxintervallum = intervallum
                        inteleje = i+1
                        intvege = j+1
            else:
                intervallum += 1
    stdout.write(str(inteleje) + " " + str(intvege) + "\n")

main()