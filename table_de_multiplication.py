choix = "o"

while choix == "o":
    nombre = input("Entrer le chiffre de la table à afficher: ")
    limite = input("Entrer la valeur max jusqu'ou l'opération doit être effectuée: ")

    if nombre != "" and limite != "":
        if (nombre and limite).isdigit:
            for i in range(int(limite)+1):
                print(f"{i} x {nombre} = {i*int(nombre)}")
        else:
            print("\nVeuillez rentrer uniqument des nombres s'il vous plait!")
    else:
        print("\n!!! Veuillez rentrez des nombres valides s'il vous plait.")

    choix = input(""" 
    Voulez-vous recommencer ?
    Veuillez rentrer votre choix: 
    - o pour oui 
    - n pour non
    Votre choix : 
    """)

    if choix == "O" or choix == "o":
        choix = "o"
    else:
        choix = ""
        print("Merci pour votre visite!")
