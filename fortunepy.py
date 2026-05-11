#FortunePy (A Fortune Library for Python, And Linux)


import ollama
import os
DashThing = "-" * 50
logo = """
          .?77777777777777$.            
          777..777777777777$+           
         .77    7777777777$$$           
         .777 .7777777777$$$$           
         .7777777777777$$$$$$           
         ..........:77$$$$$$$           
  .77777777777777777$$$$$$$$$.=======.  
 777777777777777777$$$$$$$$$$.========  
7777777777777777$$$$$$$$$$$$$.========= 
77777777777777$$$$$$$$$$$$$$$.========= 
777777777777$$$$$$$$$$$$$$$$ :========+.
77777777777$$$$$$$$$$$$$$+..=========++~
777777777$$..~=====================+++++
77777777$~.~~~~=~=================+++++.
777777$$$.~~~===================+++++++.
77777$$$$.~~==================++++++++: 
 7$$$$$$$.==================++++++++++. 
 .,$$$$$$.================++++++++++~.  
         .=========~.........           
         .=============++++++           
         .===========+++..+++           
         .==========+++.  .++           
          ,=======++++++,,++,           
          ..=====+++++++++=.            
                ..~+=...     
"""
# Thank you @xero (github gists)!
def OllamaGen(temp,model):
    #options={'temperature': 0},
        response = ollama.generate(
        model = model,
        temperature = temp,
        prompt = "Give a user a fortune, ONLY the fortune. nothing else."
        options={
            'num_predict': 100,  # Limits the response to 100 tokens
            'temprature': temp
            }
        )
    return response
def fortune():
    return os.popen("fortune").read() # i could of used this in getuser.py lol
def aiFortune(temp=1, AImodel="gpt-oss:120b-cloud"):
    response = OllamaGen(temp=temp,AImodel)

    stripped = response["response"].strip()
    return stripped
def ASCIIFortune():
    return os.popen("fortune|figlet").read() # Piping fortune & FIGlet = this.
def aiASCIIFortune(temp=1, AImodel="gpt-oss:120b-cloud"):
    response = OllamaGen(temp=temp,model=AImodel)

    stripped = response["response"].strip()
    return os.popen(f'figlet "{stripped}"').read() # Yes, i know using "" works. fight me.




if __name__ == "__main__":
    print(logo)
    print(os.popen(f'figlet "FortunePy"').read())
    print("(A Fortune Library for Python, And Linux)")
    print("TEMP FIX")
    print("\n")
    print("\n")
    print(DashThing)
    print("Avaliable Functions: \n")
    print("fortunepy.fortune(): output a fortune")
    print("fortunepy.aiFortune(temp,AIModel): an LLM generates a fortune for you! (if you have a bad system, use ollama's cloud models!")
    print("fortunepy.ASCIIFortune(): output a fortune in ASCII Text.")
    print("fortunepy.aiASCIIFortune(temp,AIModel): The same as aiFortune(), just in ASCII Text.")
    print("""Code Example!
import fortunepy

print(fortunepy.fortune())
""")
    print(DashThing)
