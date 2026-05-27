from datetime import date

def saisir():
    nom = input("Quel est ton prénom ? ")
    age = int(input("Quel est ton age? "))
    return nom,age

def calculer_annee(age):
    return date.today().year - age

def main():
    nom,age = saisir()
    annee_naissance = calculer_annee(age)
    print(f"Bonjour, {nom}, tu as {age} ans, donc tu es né(e) vers {annee_naissance}.")


if __name__ == "__main__":
    main()


#Résultat de l'éxécution
#Quel est ton prénom ? Lois
#Quel est ton age? 29
#Bonjour, Lois, tu as 29 ans, donc tu es né(e) vers 1997.
