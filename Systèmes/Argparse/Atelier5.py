import argparse
import sys


def parser_arguments():
    parser = argparse.ArgumentParser(description="Convertisseur de température")

    parser.add_argument("valeur", type=float)
    parser.add_argument("--from", choices=["celsius", "fahrenheit", "kelvin"], dest="depuis")
    parser.add_argument("--to", choices=["celsius", "fahrenheit", "kelvin"], dest="vers")
    parser.add_argument("--precision", type=int, default=2)

    args = parser.parse_args()

    if args.depuis is None or args.vers is None:
        print("Erreur : --from et --to sont obligatoires", file=sys.stderr)
        sys.exit(1)

    return args


def vers_celsius(valeur, depuis):
    if depuis == "celsius":
        return valeur
    if depuis == "fahrenheit":
        return (valeur - 32) * 5 / 9
    if depuis == "kelvin":
        return valeur - 273.15


def depuis_celsius(celsius, vers):
    if vers == "celsius":
        return celsius
    if vers == "fahrenheit":
        return celsius * 9 / 5 + 32
    if vers == "kelvin":
        return celsius + 273.15


def convertir(valeur, depuis, vers):
    celsius = vers_celsius(valeur, depuis)
    return depuis_celsius(celsius, vers)


def afficher(valeur, depuis, vers, resultat, precision):
    print(f"{valeur:.{precision}f} {depuis} = {resultat:.{precision}f} {vers}")


def main():
    args = parser_arguments()
    resultat = convertir(args.valeur, args.depuis, args.vers)
    afficher(args.valeur, args.depuis, args.vers, resultat, args.precision)


if __name__ == "__main__":
    main()

#Exemples de l'éxécution

#python3 argparse/atelier5.py 0 --from celsius --to kelvin
#0.00 celsius = 273.15 kelvin
#python3 argparse/atelier5.py 100 --from celsius --to fahrenheit
#100.00 celsius = 212.00 fahrenheit
#argparse/atelier5.py 500 --from kelvin --to fahrenheit
#500.00 kelvin = 440.33 fahrenheit

#python3 argparse/atelier5.py 100
#Erreur : --from et --to sont obligatoires


