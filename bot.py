import openai
import time
import configparser

# Lade API-Schlüssel
config = configparser.ConfigParser()
config.read('config.ini')
openai.api_key = config['DEFAULT']['API_KEY']

    # Openai Integration
def ask_openai(question):
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": question},
            ]
        )
        return response.choices[0].message['content']

    # Funktion um eigene Frage an OpenAI zu stellen
def openai_pr(inp):
        answer = ask_openai(
            "Ich habe eine Firma namens Bugland und die baut Reinigungsroboter und einen Gartenroboter. "
            "Du sollst so tun als wärst du der Supportchat von dem Unternehmen und Tipps geben. "
            "Sag bitte nicht, dass der Support kontaktiert werden soll oder das du bei weiteren " 
            "Fragen helfen kannst. Auch bitte nicht sagen, dass detailierte Informationen "
            "helfen. Du bist ein Supportchat für ein Unternehmen, also denke daran nur sinnvolle aussagen zu tätigen" 
            "Also einfach nur die Antwort auf folgende Frage geben und bitte die einzelnen "
            "Punkte mit Gedankenstrichen klar trennen: " + inp
        )
        print("Antwort:", answer)

    # Zusammenstellung der vorgegebenen Probleme und Lösungen
def qs_1(problem_choice):
        i = 0
        while i < 4:
            i+=1
            if i == 1:
                print("Was für ein Problem hast du?")
                print("Bitte wähle aus folgenden aus:")
                print("1. Konfiguration")
                print("2. Defekt")
                print("3. Fehlermeldung")
                print("4. Fehlverhalten des Roboters")
                print("5. Sonstiges")
            elif i == 2 or i == 3:
                print("Hast du ein weiteres Problem? Wenn ja, bitte wähle aus folgenden aus, alternativ 'Exit' zum beenden:")
                print("Bitte wähle aus folgenden aus:")
                print("1. Konfiguration")
                print("2. Defekt")
                print("3. Fehlermeldung")
                print("4. Fehlverhalten des Roboters")
                print("5. Sonstiges")
            else:
                print("Tut mir leid, ich denke ich kann dir bei deinem Problem nicht weiterhelfen. Bitte kontaktiere den Support unter folgender Telefonnummer oder E-Mail.")
                print("Telefonnummer: 0123456789")
                print("E-Mail: supp.bt@bugland.de")
                time.sleep(5)
                break
        
            problem_choice = input("Bitte gib die Nummer deines Problemes an: ")
            while not (problem_choice == "1" or problem_choice == "2" or problem_choice == "3" or problem_choice == "4" or problem_choice == "5" or problem_choice.lower() == "exit" or problem_choice.lower() == "sonstiges"):
                print("Ungültige Eingabe. Überprüfe auch auf Rechtschreibung!")
                problem_choice = input("Bitte gib die Nummer deines Problemes an: ")

            if problem_choice == "1" or problem_choice.lower() == "konfiguration":
                openai_pr("Mein Roboter hat ein Konfigurationsproblem. Was soll ich nun machen?")
            elif problem_choice == "2" or problem_choice.lower() == "defekt":
                openai_pr("Ich glaub mein Roboter ist defekt. Was soll ich nun machen?")
            elif problem_choice == "3" or problem_choice.lower() == "fehlermeldung":
                openai_pr("Ich habe einen Roboter und er zeigt eine Fehlermeldung an. Was soll ich nun machen?")
            elif problem_choice == "4" or problem_choice.lower() == "fehlverhalten des roboters":
                openai_pr("Der Roboter funktioniert nicht so wie er soll. Was soll ich nun machen?")
                print("Alternativ kontaktiere den Support unter folgender Telefonnummer oder E-Mail.")
                print("Telefonnummer: 0123456789")
                print("E-Mail: supp.bt@bugland.de")
                time.sleep(5)
            elif problem_choice == "5"  or problem_choice.lower() == "sonstiges":
                problem_choice = input("Bitte schildere dein Problem: ")
                openai_pr(problem_choice)
            elif problem_choice.lower() == "exit":
                break
            else:
                print("Ungültige Eingabe")
            time.sleep(5)

    # Hauptporgramm des Chatbots        
    # Chatstart 
print("Um den Chat zu beenden 'Exit' eingeben")
pr_1 = input("Um welches BUGLAND Produkt handelt es sich? ")

    # Wenn ungültige Eingabe, dann erneut fragen
while not (pr_1.lower() == "cleanbug" or pr_1.lower() == "windowfly" or pr_1.lower() == "gardenbeetle" or pr_1.lower() == "exit" or pr_1.lower() == "sonstiges"):
        print("Ungültige Eingabe, bitte achte auf Rechtschreibung! Alternativ zum Abbrechen 'Exit' eingeben")
        print("Du hast eine andere Frage? Gib 'sonstiges' ein.")
        pr_1 = input("Bitte gib dein Produkt ein: ")

    # Chat findet solange statt, bis Nutzer 'exit' eingibt
while pr_1.lower() != "exit":

        if pr_1.lower() == "cleanbug":
            qs_1(pr_1)
            break  
        elif pr_1.lower() == "windowfly":
            qs_1(pr_1)
            break    
        elif pr_1.lower() == "gardenbeetle":
            qs_1(pr_1)
            break    
        else:
            pr_1 = input("Bitte gib deine Frage ein: ")

    # Chat beenden - wird immer ausgegeben wenn 'Exit' eingegeben wird
print("Ich hoffe ich konnte weiterhelfen.")    
print("Vielen Dank für die Nutzung unseres Chats!")