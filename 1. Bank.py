from sys import stdin, stdout

def main():
    belepesek = []
    hanynap = 0
    hanybelepes = 0
    uresnapszam = 0
    uresnap = []
    hanynap, hanybelepes = map(int, stdin.readline().split())
    for i in range(hanybelepes):
        belepesek.append(list(map(int, stdin.readline().split())))
    nap = 1
    i = 0
    while i < len(belepesek):
        egybelepes = False
        ketbelepes = False
        if belepesek[i][1] != nap:
            uresnap.append(nap)
            uresnapszam += 1
            nap += 1
        else:
            while i < len(belepesek) and belepesek[i][1] == nap:
                if belepesek[i][0] == 1:
                    egybelepes = True
                else:
                    ketbelepes = True
                if i <= len(belepesek):
                    i += 1
            if egybelepes and ketbelepes:
                if i < len(belepesek):
                    nap += 1
                continue
            else:
                uresnap.append(nap)
                uresnapszam += 1
                if i < len(belepesek):
                    nap += 1
    if nap < hanynap:
        for i in range(hanynap - nap):
            nap += 1
            uresnapszam += 1
            uresnap.append(nap)
    seged =""
    for i in range(len(uresnap)):
        seged = seged + str(uresnap[i]) + " "
    stdout.write(str(uresnapszam) + "\n" + seged +"\n")

main()