import os
import json
import yaml
import dicttoxml
import xml.etree.cElementTree as ET
print("Konwerter xml, json, yml")
a = input("Podaj nazwę pliku (Przykład: nazwa_pliku.xml): ")
a = os.path.abspath(a)

if os.path.exists(a):
    if not os.path.isfile(a):
        print("Podana ścieżka nie odnosi się do pliku.")
    else:
        nazwa_pliku, rozszerzenie = os.path.splitext(a)
        if rozszerzenie.lower() == '.xml':
            print("Wybrałeś plik XML.") #usuń to potem
# KONWERTER Z YML DO XML ORAZ JSON JEST JUŻ GOTOWY
        elif rozszerzenie.lower() == '.yml':
            try:
                with open(a) as plik:
                    info = yaml.safe_load(plik)
                print("Składnia pliku z rozszerzeniem YAML jest poprawna.")
                b = input("Podaj rozszerzenie pliku, na które mam przekonwertować (json, xml): ")
                if b == 'json':
                    json_file = f"{nazwa_pliku}.json"
                    with open(json_file, 'w') as plik_json:
                        json.dump(info, plik_json)
                    print(f"Plik YAML został przekonwertowany na JSON i zapisany jako {json_file}.")
                elif b == 'xml':
                    xml_file = f"{nazwa_pliku}.xml"
                    xml_data = dicttoxml.dicttoxml(info)
                    with open(xml_file, 'w') as plik_xml:
                        plik_xml.write(xml_data.decode())
                    print(f"Plik YAML został przekonwertowany na XML i zapisany jako {xml_file}.")
            except yaml.YAMLError as blad:
                print("Błąd w składni pliku YAML:\n", blad)
# KONWERTER Z JSON DO XML ORAZ YAML JEST JUŻ GOTOWY
        elif rozszerzenie.lower() == '.json':
            try:
                with open(a) as plik:
                    info = json.load(plik)
                print("Składnia pliku z rozszerzeniem JSON jest poprawna.")
                b = input("Podaj roszerzenie pliku, na który mam przekonwertować (yml , xml): ")
                if b == 'yml':
                    yml_file = f"{nazwa_pliku}.yml"
                    with open(yml_file, 'w') as plik_yml:
                        yaml.dump(info, plik_yml, default_flow_style=False)
                    print(f"Plik JSON został przekonwertowany na YAML i zapisany jako {yml_file}.")
                elif b == 'xml':
                    xml_file = f"{nazwa_pliku}.xml"
                    xml_data = dicttoxml.dicttoxml(info)
                    with open(xml_file, 'w') as plik_xml:
                        plik_xml.write(xml_data.decode())
                    print(f"Plik JSON został przekonwertowany na XML i zapisany jako {xml_file}.")
            except json.JSONDecodeError as blad:
                print("Błąd w składni pliku JSON:\n",blad)
        else:
            print("Nieobsługiwany format pliku.")
else:
    print("Podana ścieżka pliku nie istnieje.")


