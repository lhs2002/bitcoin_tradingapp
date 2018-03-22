import sys
from cs50 import get_string

if (len(sys.argv) == 2):

    k = int(sys.argv[1])

    if (k >= 0):

        #Prompt plaintext
        message = get_string("plaintext: ")

        #Encrypt plaintext
        print("ciphertext: ", end="")
        for c in message:
            if c.isupper():

                #convert character to ascii code and shift
                a = (((ord(c) - 65 + k) % 26) + 65)

                #convert ascii code of shifted char into char to print
                print(f"{chr(a)}", end="")

            elif c.islower():

                b = (((ord(c) - 97 + k) % 26) + 97)
                print(f"{chr(b)}", end="")

            else:
                print(f"{c}", end="")


        print("")
    else:
        print("Key must be a non-negative integer.")

else:
    print("Usage: ./caesar k")
    exit(1)



