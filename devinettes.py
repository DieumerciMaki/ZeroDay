# Module pour des nombres aleatoires
import random

# Genere un nombre entre 1 et 100
nombre_secret = random.randint(1, 10)
essais = 0
max_essais = 5
score = 0

print("Yo bruh, devine le nombre entre 1 et 10 ! T'as", max_essais, "essais max. ")

# Tant que le joueur a des essais
while essais < max_essais:
    # Ask au joueur de saisir un nombre
    try:
        devine = int(input("Ton guess ?"))
        essais += 1 # Incremente le compteur d'essais

        # Verifie si le geuss est correctus
        if devine == nombre_secret:
            score = 10 - (essais * 1)
            print(f"GG man ! T'as trouve en {essais} essais ! T'es Him")
            print(f"Ton score : {score}/10")
            # Message du score related
            if score >= 8 :
                print("T'es Him for real man")
            elif score >= 6:
                print("pas mal, gingimbre!")
            else:
                print("Mon gaaa faut taffer")
            break
        elif devine < nombre_secret:
            print("Trop bas man, try again. ")
        else:
            print("Trop haut,redescends !")

        # Les essais restants
        print(f"Man il te reste {max_essais - essais} essais. ")

    except ValueError:
        print("Brooo, mets un Vrai nombre, pas des lettres !")
# Si le joueur depasse les essais
if essais >= max_essais and devine != nombre_secret :
    print(f"Game over, man man ! Le nombre etait {nombre_secret}. Tas echouer my gee")