import os
import json
import yaml
import dicttoxml
import xml.etree.cElementTree as ET
import xmltodict

print("Konwerter xml, json, yml")
a = input("Podaj nazwę pliku (Przykład: nazwa_pliku.xml): ")
a = os.path.abspath(a)

if os.path.exists(a):
    if not os.path.isfile(a):
        print("Podana ścieżka nie odnosi się do pliku.")
    else:
        nazwa_pliku, rozszerzenie = os.path.splitext(a)
# KONWERTER Z XML DO YAML ORAZ JSON JEST JUŻ GOTOWY
        if rozszerzenie.lower() == '.xml':
            try:
                tree = ET.parse(a)
                print("Poprawna składnia pliku XML.")
                b = input("Podaj rozszerzenie pliku, na które mam przekonwertować (yaml, json): ")
                if b == 'yaml':
                    yaml_file = f"{nazwa_pliku}.yaml"
                    xml_root = tree.getroot()
                    xml_dict = xmltodict.parse(ET.tostring(xml_root))
                    with open(yaml_file, 'w') as plik_yaml:
                        yaml.dump(xml_dict, plik_yaml)
                    print(f"Plik XML został przekonwertowany na YAML i zapisany jako {yaml_file}.")
                elif b == 'json':
                    json_file = f"{nazwa_pliku}.json"
                    xml_root = tree.getroot()
                    xml_dict = xmltodict.parse(ET.tostring(xml_root))
                    with open(json_file, 'w') as plik_json:
                        json.dump(xml_dict, plik_json)
                    print(f"Plik XML został przekonwertowany na JSON i zapisany jako {json_file}.")
                else:
                    print("Niepoprawne rozszerzenie pliku.")
            except ET.ParseError as error:
                print("Błąd składni pliku XML:\n", error)
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
                else:
                    print("Niepoprawne rozszerzenie pliku.")
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
                else:
                    print("Niepoprawne rozszerzenie pliku.")
            except json.JSONDecodeError as blad:
                print("Błąd w składni pliku JSON:\n",blad)
        else:
            print("Nieobsługiwany format pliku.")
else:
    print("Podana ścieżka pliku nie istnieje.")


