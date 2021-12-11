from sys import stdin, stdout
def main():
    magassag = int(stdin.readline())
    hely = 1
    elotti = 0
    elottielotti = 0
    for i in range(magassag):
        elottielotti = elotti
        elotti = hely
        hely = 2*elotti + elottielotti
    stdout.write((str(hely % 20201114)) + "\n")

main()