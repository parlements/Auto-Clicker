import pyautogui
import time
import threading

# ASCII art : TONY SPAM CLICK
ascii_art = '''


  __________  _   ____  __
 /_  __/ __ \/ | / /\ \/ /
  / / / / / /  |/ /  \  / 
 / / / /_/ / /|  /   / /  
/_/  \____/_/ |_/   /_/   
                          
        

'''

# Afficher le ASCII art
print(ascii_art)

# Définir la fonction qui effectue un clic de souris
def auto_clicker(interval=1, stop_event=None):
    """
    Clics automatiques à un intervalle spécifié (en secondes).
    :param interval: intervalle de clics en secondes
    :param stop_event: événement pour arrêter l'auto-clicker
    """
    while True:
        if stop_event and stop_event.is_set():
            print("Auto-clicker c arrêté.")
            break
        pyautogui.click()  # Effectue un clic à la position actuelle de la souris
        time.sleep(interval)  # Attend avant de cliquer à nouveau

# Fonction pour démarrer l'auto-clicker dans un thread
def start_auto_clicker(interval=1):
    stop_event = threading.Event()
    click_thread = threading.Thread(target=auto_clicker, args=(interval, stop_event))
    click_thread.daemon = True  # Permet au thread de se fermer lorsque le programme principal se ferme
    click_thread.start()
    return stop_event

# Exemple d'utilisation
if __name__ == "__main__":
    print("lauto clicker a demareer https://t.me/fiche2internet .")
    
    while True:
        try:
            interval = float(input("Entrez l'intervalle entre chaque clic (en secondes) : "))
            if interval <= 0:
                print("sa doit etre + que O dsl.")
                continue
            break
        except ValueError:
            print("entre un nombre frrot.")
    
    stop_event = start_auto_clicker(interval)
    
    try:
        while True:
            time.sleep(1)  # Garder le programme en cours d'exécution
    except KeyboardInterrupt:
        stop_event.set()  # Arrêter l'auto-clicker lorsque l'utilisateur appuie sur Ctrl + C
        print("L'auto-clicker a été arrêté.")
        print("Programme terminé.")

print("DONATIONSPoufuVa3HXS1gGwFJQadzHBTZtG bitcoin : Zpub6yLeM9ndEKZEZna8kw9gdFgFAs3LJJXw6VbKbWgwNP5v3ZwCjXQ6jJrxqChbRxcDvRzFSBc2YxMrxxCefCM3UAKRQvFur4aCEQKgBkzvMM2 : litecoin : Lgd18C2")

