#FortunePy (A Fortune Library for Python, And Linux)


import ollama
import os

def fortune():
    return os.popen("fortune").read() # i could of used this in getuser.py lol
def aiFortune(temp=1, AImodel="gpt-oss:120b-cloud"):
    response = ollama.generate(
        model = AImodel,
        temperature = temp,
        prompt = "Give a user a fortune, ONLY the fortune. nothing else."
        )

    stripped = response["response"].strip()
    return stripped
def ASCIIFortune():
    return os.popen("fortune|figlet").read() # Piping fortune & FIGlet = this.
def aiASCIIFortune(temp=1, AImodel="gpt-oss:120b-cloud"):
    response = ollama.generate(
        model = AImodel,
        temperature = temp,
        prompt = "Give a user a fortune, ONLY the fortune. nothing else."
        )

    stripped = response["response"].strip()
    return os.popen(f'figlet "{stripped}"').read() # Yes, i know using "" works. fight me.




if __name__ == "__main__":
    print(os.popen(f'figlet "FortunePy"').read())
    print("(A Fortune Library for Python, And Linux)")
    print("\n")
    print("\n")
    print("Avaliable Functions: \n")
    print("fortunepy.fortune(): output a fortune")
    print("fortunepy.aiFortune(temp,AIModel): an LLM generates a fortune for you! (if you have a bad system, use ollama's cloud models!")
    print("fortunepy.ASCIIFortune(): output a fortune in ASCII Text.")
    print("fortunepy.aiASCIIFortune(temp,AIModel): The same as aiFortune(), just in ASCII Text.")
    print("""Code Example!
import fortunepy

print(fortunepy.fortune())
""")
