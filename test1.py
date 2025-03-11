
# author: PEVE BEA
# file: test1.py
"""
    ceci est un fichier python pour e
    tester de ptits bout de code
"""

def hello(name:str = "user"):
    return f"Hello {name}" 


def main():
    continuer = True
    while continuer:
        print("bienvenue, voulez vous utiliser la fnction hello? o/n: ")
        reponse = input()
        if reponse.lower() == "o":
            name = input("Entrer un nom ")
            print(hello(name)) 
        else:
            continuer = False



main()
