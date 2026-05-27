import argparse
import sys

def parser_arguments():
    parser = argparse.ArgumentParser(description="Mini-calculatrice CLI")

    # a + op + b en arguments positionnels
    parser.add_argument("a", type=float)
    parser.add_argument("op", choices=["+", "-", "*", "/"])
    parser.add_argument("b", type=float)

    return parser.parse_args()


def calculer(a, op, b):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            print("Erreur : division par zéro", file=sys.stderr)
            sys.exit(1)
        return a / b


def afficher(a, op, b, resultat):
    print(f"{a} {op} {b} = {resultat}")


def main():
    args = parser_arguments()
    resultat = calculer(args.a, args.op, args.b)
    afficher(args.a, args.op, args.b, resultat)

if __name__ == "__main__":
    main()


#Exemples d'éxécution

#python3 argparse/atelier1.py 3 '*' 4
#3.0 * 4.0 = 12.0
#python3 argparse/atelier1.py 4 '/' 0
#Erreur : division par zéro
#echo $?
#1



