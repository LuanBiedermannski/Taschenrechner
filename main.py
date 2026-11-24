def addieren(a, b):
    return a + b

def subtraktion(a, b):
    return a - b

 
def multiplikation(a, b):
    return a * b
 
def division(a, b):
    if b == 0:
        return "Fehler: Division durch 0"
    return a / b
 
def main():
    print("Taschenrechner")
    print("1 fuer Addition")
    print("2 fuer Subtraktion")
    print("3 fuer Multiplikation")
    print("4 fuer Division")
 
    wahl = input("Wahl eingeben: ")
 
    match wahl:
        case "1":
            print("Resultat: {}".format(addieren(2, 3)))
        case "2":
            print("Resultat: {}".format(subtraktion(5, 3)))
        case "3":
            pass
        case "4":
            pass
            pass
        case "3":
            print("Resultat: {}".format(multiplikation(4, 3)))
        case "4":
            print("Resultat: {}".format(division(10, 2)))
        case _:
            print("Falsche Auswahl, das Programm wird beendet.")
 
if __name__ == "__main__":
    main()