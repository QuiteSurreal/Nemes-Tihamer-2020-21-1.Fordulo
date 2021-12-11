from sys import stdin, stdout
def main():
    hossz = int(stdin.readline())
    sorozat = []
    leghosszabb = []
    hely = 1
    for i in range(hossz):
        while hely != 1:
            if hely <= hossz:
                sorozat.append(hely)
                hely = paros_paratlan(hely)
            else:
                sorozat = []
                break
        sorozat.append(hely)
        hely = 1+i
        if len(sorozat) > len(leghosszabb):
            leghosszabb = sorozat
        sorozat = []
    stdout.write(str(len(leghosszabb)) + "\n")

def paros_paratlan(x):
    if x % 2 == 0:
        x = x / 2
    else:
        x = x * 3 + 1
    return int(x)

main()