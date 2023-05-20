import os
import json
import yaml
import dicttoxml
import xml.etree.cElementTree as ET
import xmltodict
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QPushButton, QFileDialog, QMessageBox
from PyQt5.QtGui import QColor, QFont

class ConverterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Konwerter XML JSON YAML")
        self.setGeometry(100, 100, 475, 200)

        self.file_label = QLabel(self)
        self.file_label.setGeometry(20, 20, 360, 20)
        self.file_label.setText("Wybierz plik do konwersji:")

        self.file_path = QLabel(self)
        self.file_path.setGeometry(20, 40, 360, 20)

        self.file_button = QPushButton(self)
        self.file_button.setGeometry(20, 70, 100, 30)
        self.file_button.setText("Wybierz plik")
        self.file_button.clicked.connect(self.select_file)

        self.format_label = QLabel(self)
        self.format_label.setGeometry(20, 120, 360, 20)
        self.format_label.setText("Wybierz format docelowy:")

        self.format_combo = QComboBox(self)
        self.format_combo.setGeometry(20, 140, 100, 30)
        self.format_combo.addItem("yaml")
        self.format_combo.addItem("json")
        self.format_combo.addItem("xml")

        self.convert_button = QPushButton(self)
        self.convert_button.setGeometry(140, 140, 100, 30)
        self.convert_button.setText("Konwertuj")
        self.convert_button.clicked.connect(self.convert_file)

        self.label = QLabel(self)
        self.label.setText("Jeśli coś nie będzie się chciało skonwertować lepiej wrzucić to do tego samego folderu co konwerter")
        self.label.setGeometry(20, 180, 500, 20)  # Zmieniona geometria dla etykiety
        self.label.setFont(QFont("Arial", 7))
        self.label.setStyleSheet("color: red")
    def select_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Wybierz plik", "", "Pliki XML (*.xml);;Pliki JSON (*.json);;Pliki YAML (*.yml)")
        self.file_path.setText(file_path)

    def convert_file(self):
        file_path = self.file_path.text()
        file_format = self.format_combo.currentText()
        if not os.path.exists(file_path):
            QMessageBox.critical(self, "Błąd", "Podana ścieżka pliku nie istnieje.")
            return
        if not os.path.isfile(file_path):
            QMessageBox.critical(self, "Błąd", "Podana ścieżka nie odnosi się do pliku.")
            return

        file_name, file_ext = os.path.splitext(file_path)
        file_ext = file_ext.lower()
        if file_ext == '.xml':
            self.convert_xml(file_name, file_format)
        elif file_ext == '.yml':
            self.convert_yaml(file_name, file_format)
        elif file_ext == '.json':
            self.convert_json(file_name, file_format)
        else:
            QMessageBox.critical(self, "Błąd", "Nieobsługiwany format pliku.")

    def convert_xml(self, file_path, file_format):
        try:
            tree = ET.parse(file_path + '.xml')
            xml_root = tree.getroot()
            xml_dict = xmltodict.parse(ET.tostring(xml_root))
            if file_format == 'yaml':
                converted_file = file_path + '.yaml'
                with open(converted_file, 'w') as file:
                    yaml.dump(xml_dict, file)
                QMessageBox.information(self, "Sukces", f"Plik XML został przekonwertowany na YAML i zapisany jako {converted_file}.")
            elif file_format == 'json':
                converted_file = file_path + '.json'
                with open(converted_file, 'w') as file:
                    json.dump(xml_dict, file)
                QMessageBox.information(self, "Sukces", f"Plik XML został przekonwertowany na JSON i zapisany jako {converted_file}.")
            else:
                QMessageBox.critical(self, "Błąd", "Niepoprawne rozszerzenie pliku.")
        except ET.ParseError as error:
            QMessageBox.critical(self, "Błąd", f"Błąd składni pliku XML:\n{error}")

    def convert_yaml(self, file_path, file_format):
        try:
            with open(file_path + '.yml') as file:
                yaml_data = yaml.safe_load(file)
            if file_format == 'json':
                converted_file = file_path + '.json'
                with open(converted_file, 'w') as file:
                    json.dump(yaml_data, file)
                QMessageBox.information(self, "Sukces",
                                        f"Plik YAML został przekonwertowany na JSON i zapisany jako {converted_file}.")
            elif file_format == 'xml':
                converted_file = file_path + '.xml'
                xml_data = dicttoxml.dicttoxml(yaml_data)
                with open(converted_file, 'w') as file:
                    file.write(xml_data.decode())
                QMessageBox.information(self, "Sukces",
                                        f"Plik YAML został przekonwertowany na XML i zapisany jako {converted_file}.")
            else:
                QMessageBox.critical(self, "Błąd", "Niepoprawne rozszerzenie pliku.")
        except yaml.YAMLError as error:
            QMessageBox.critical(self, "Błąd", f"Błąd w składni pliku YAML:\n{error}")

    def convert_json(self, file_path, file_format):
        try:
            with open(file_path + '.json') as file:
                json_data = json.load(file)
            if file_format == 'yaml':
                converted_file = file_path + '.yaml'
                with open(converted_file, 'w') as file:
                    yaml.dump(json_data, file, default_flow_style=False)
                QMessageBox.information(self, "Sukces",
                                        f"Plik JSON został przekonwertowany na YAML i zapisany jako {converted_file}.")
            elif file_format == 'xml':
                converted_file = file_path + '.xml'
                xml_data = dicttoxml.dicttoxml(json_data)
                with open(converted_file, 'w') as file:
                    file.write(xml_data.decode())
                QMessageBox.information(self, "Sukces",
                                        f"Plik JSON został przekonwertowany na XML i zapisany jako {converted_file}.")
            else:
                QMessageBox.critical(self, "Błąd", "Niepoprawne rozszerzenie pliku.")
        except json.JSONDecodeError as error:
            QMessageBox.critical(self, "Błąd", f"Błąd w składni pliku JSON:\n{error}")


if __name__ == "__main__":
    app = QApplication([])
    window = ConverterWindow()
    window.show()
    app.exec_()
