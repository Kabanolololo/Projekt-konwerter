import os
import json
import yaml

def ymltojson(a):
    with open(a) as file:
        data = yaml.safe_load(file)
    json_file = os.path.splitext(a)[0] + ".json"
    with open(json_file, "w") as file:
        json.dump(data, file, indent=4)
    print("Plik YAML został pomyślnie przekonwertowany na JSON i zapisany jako:", json_file)


print("Konwerter xml, json, yml")
a = input("Podaj nazwę pliku (Przykład: nazwa_pliku.xml): ")

a = os.path.abspath(a)

#warunki sprawdzające poprawność wybranych rozszerzeń

if os.path.exists(a):
    if not os.path.isfile(a):
        print("Podana ścieżka nie odnosi się do pliku.")
    else:
        nazwa_pliku, rozszerzenie = os.path.splitext(a)
        if rozszerzenie.lower() == '.xml':
            print("Wybrałeś plik XML.")
        elif rozszerzenie.lower() == '.yml':
            print("Wybrałeś plik YAML.")
        elif rozszerzenie.lower() == '.json':
            try:
                with open(a) as plik:
                    info = json.load(plik)
                print("Składnia pliku z rozszerzeniem JSON jest poprawna.")
            except json.JSONDecodeError as blad:
                print("Błąd w składni pliku JSON:\n",blad)
        else:
            print("Nieobsługiwany format pliku.")
#dodać wiecej warunków
        b = input("Podaj rozszerzenie pliku, na który mam skonwertować (wpisz: yml , json , xml ): ")
        if b == 'json':
            ymltojson(a)
        #if b == 'yml':
        #if b == 'json':
        else:
            print("Nieprawidłowe rozszerzenie pliku")

else:
    print("Podana ścieżka pliku nie istnieje.")
