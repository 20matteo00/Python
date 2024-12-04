# main.py
from squadre import crea_squadre
from campionato import Campionato

def visualizza_menu():
    print("1. Crea campionato")
    print("2. Visualizza calendario")
    print("3. Visualizza classifica")
    print("4. Gioca una giornata")
    print("5. Esci")

def main():
    campionato = None
    while True:
        visualizza_menu()
        scelta = input("Scegli un'opzione: ")

        if scelta == '1':
            numero_squadre = int(input("Quante squadre vuoi nel campionato? "))
            squadre = crea_squadre(numero_squadre)
            campionato = Campionato(squadre)
            campionato.genera_calendario()
            print("Campionato creato con successo!")
        
        elif scelta == '2' and campionato:
            campionato.visualizza_calendario()
        
        elif scelta == '3' and campionato:
            campionato.visualizza_classifica()
        
        elif scelta == '4' and campionato:
            campionato.gioca_giornata()
        
        elif scelta == '5':
            print("Uscita in corso...")
            break
        else:
            print("Opzione non valida o campionato non creato.")

if __name__ == "__main__":
    main()
