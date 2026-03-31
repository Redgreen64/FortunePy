#PyTypewriter -- A Typewriter-esk python module
import sys,time,os #Import Both.

DashThing = "-" * 50

USAGE_TABLE = [f"{DashThing}","A Typewriter-esk python module","Usage: ", """import PyTypewriter
     PyTypewriter.typew("Hello, World!")
""","Functions:","typew(text,delay) -> Types Like A Typewriter!","That's it, For now.",f"{DashThing}"]

def typew(txt :str,delay :int=0.05):
    for char in txt:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

if __name__ == "__main__":
    os.system("figlet PyTypewriter")
    print("\n Bundles with FortunePy!")
    print("\n")
    for line in USAGE_TABLE:
        typew(f"{line} \n",0.025)
