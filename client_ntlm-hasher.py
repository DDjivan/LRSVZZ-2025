from impacket.ntlm import compute_lmhash, compute_nthash
from getpass import getpass
from time import sleep

def ntlm_hasher(sInput:str) -> str :
    nt_hash = compute_nthash(sInput)
    # print("\nNTLM hash of your password:")
    return nt_hash.hex()


def nice_password_hasher() -> None :
    sInput = getpass("Enter your password: ")
    # sInput = "your_password_here"

    print(           "Enter your password: "+'*'*len(sInput), end="", flush=True)
    sleep(1)

    sHash = ntlm_hasher(sInput)

    print("")
    print("")
    print("Hashed password: ")
    print(sHash)

if __name__ == "__main__":
    nice_password_hasher()

