from math import gcd


def RSA(p: int, message: str, q: int):
    # calculate n
    n = p * q

    t = (p - 1) * (q - 1) #Euler's totient function (t)

    # select randomly public key, e , with e and t to be "prime intre ele" :D
    for i in range(2, t):
        if gcd(i, t) == 1:
            e = i
            break

    print(f"Public key is {e}")

    # select private key, d
    j = 0
    while True:
        if (j * e) % t == 1:  # d = e^(-1) % t |/d <=> 1 = d*e % t
            d = j
            break
        j += 1

    print(f"Private key is {d}")

    # converting string message to integer
    m = [ord(char) for char in message]  # this line turns the message into integer
    print(f"String message to integer using ascii table {m}")
    if all(char == 32 or (char >= 65 and char <= 90) or (char >= 97 and char <= 122) for char in
           m):  # checks if the character is either space, big letter or small letter
        # encryption using the public key, e
        ct = [(char ** e) % n for char in m]
        print(f"Encrypted message is {ct}")

        # decryption using the private key, d
        decryptedMessage = ''.join(
            [chr((char ** d) % n) for char in ct])  # joins the list of decrypted characters into a single string
        print(f"Decrypted message is {decryptedMessage}")
    else:
        print(f"Invalid text")


RSA(p=29, q=31, message="hello World")
