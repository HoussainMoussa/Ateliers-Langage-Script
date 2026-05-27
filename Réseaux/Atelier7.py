import struct

def main():
    brut = b"\x00\x00\x00\x2A"

    big_endian    = struct.unpack("!I", brut)[0]
    little_endian = struct.unpack("<I", brut)[0]
    inverse       = struct.unpack("!I", brut[::-1])[0]

    print("Big-endian           :", big_endian)
    print("Little-endian        :", little_endian)
    print("Octets inversés + BE :", inverse)
    print("Valeurs 2 et 3 égales:", little_endian == inverse)

if __name__ == "__main__":
    main()


# !!!!!! Réponse !!!!!!

#Les valeurs 2 et 3 sont identiques car lire des octets en little-endian revient à inverser leur ordre puis les lire en big-endian.
#Dans les deux cas, les octets sont interprétés de la même manière, ce qui donne exactement le même nombre.

#Voici le résultat de l'éxécution

#Big-endian           : 42
#Little-endian        : 704643072
#Octets inversés + BE : 704643072
#Valeurs 2 et 3 égales: True
