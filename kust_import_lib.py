import simplecrypt

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()

with open("passwords.txt") as inp:
    passwords = inp.read().splitlines()



for i in passwords:
    try:
        print(simplecrypt.decrypt(i, encrypted))
    except BaseException:
        pass

