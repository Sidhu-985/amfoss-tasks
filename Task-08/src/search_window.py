import requests
import os
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QApplication, QMessageBox
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt 
from display_window import DisplayWindow  

class SearchWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.background = QLabel(self)
        self.background.setPixmap(QPixmap('../assets/landing.jpg'))
        self.background.setGeometry(0, 0, 850, 500)

        self.setFixedSize(850, 500)

        self.textbox = QLineEdit(self)
        self.textbox.setGeometry(50, 50, 280, 40)

        label1 = QLabel("Enter the name", self)
        label1.setGeometry(50, 5, 600, 70)

        enter_button = QPushButton("Search", self)
        enter_button.setGeometry(50, 300, 160, 43)
        enter_button.setStyleSheet("QPushButton:hover {background-color: red; color:black;} QPushButton { margin: 2px; border: 2px solid red; border-radius: 10px; color:white; background-color:black;}")

        capture_button = QPushButton("Capture", self)
        capture_button.setGeometry(50, 350, 160, 43)
        capture_button.setStyleSheet("QPushButton:hover {background-color: red; color:black;} QPushButton { margin: 2px; border: 2px solid red; border-radius: 10px; color:white; background-color:black;}")

        display_button = QPushButton("Display", self)
        display_button.setGeometry(50, 400, 160, 43)
        display_button.setStyleSheet("QPushButton:hover {background-color: red; color:black;} QPushButton { margin: 2px; border: 2px solid red; border-radius: 10px; color:white; background-color:black;}")
        
        self.pokemon_name_label = QLabel(self)
        self.pokemon_name_label.setGeometry(300, 100, 200, 30)

        self.pokemon_abilities_label = QLabel(self)
        self.pokemon_abilities_label.setGeometry(300, 150, 200, 30)

        self.pokemon_types_label = QLabel(self)
        self.pokemon_types_label.setGeometry(300, 200, 200, 30)

        self.pokemon_stats_label = QLabel(self)
        self.pokemon_stats_label.setGeometry(300, 250, 200, 100)

        self.pokemon_artwork_label = QLabel(self)
        self.pokemon_artwork_label.setGeometry(500, 100, 200, 200)

        enter_button.clicked.connect(self.fetch_pokemon_data)

        capture_button.clicked.connect(self.capture_pokemon)
        
        display_button.clicked.connect(self.open_display_window)

        self.pokemon_name = ""
        self.pokemon_abilities = []
        self.pokemon_types = []
        self.pokemon_stats = {}
        self.pokemon_artwork_url = ""
 
        self.captured_pokemon =  []

    def fetch_pokemon_data(self):
       
        self.background.hide()

        pokemon_name = self.textbox.text()
        if pokemon_name:
             url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
             response = requests.get(url)

             if response.status_code == 200:
           
                pokemon_data = response.json()

                self.pokemon_name = pokemon_data['name']
                self.pokemon_abilities = [ability['ability']['name'] for ability in pokemon_data['abilities']]
                self.pokemon_types = [type_data['type']['name'] for type_data in pokemon_data['types']]
                self.pokemon_stats = {stat['stat']['name']: stat['base_stat'] for stat in pokemon_data['stats']}
                self.pokemon_artwork_url = pokemon_data['sprites']['other']['official-artwork']['front_default']

                self.pokemon_name_label.setText(f"Name: {self.pokemon_name}")
                self.pokemon_abilities_label.setText(f"Abilities: {', '.join(self.pokemon_abilities)}")
                self.pokemon_types_label.setText(f"Types: {', '.join(self.pokemon_types)}")

                stats_text = "\n".join([f"{stat_name}: {stat_value}" for stat_name, stat_value in self.pokemon_stats.items()])
                self.pokemon_stats_label.setText(f"Stats:\n{stats_text}")

                try:
      
                    pixmap = QPixmap()
                    pixmap.loadFromData(requests.get(self.pokemon_artwork_url).content)

                    if not pixmap.isNull():
                        
                        label_size = self.pokemon_artwork_label.size()
                        scaled_pixmap = pixmap.scaled(
                            label_size, 
                            aspectMode=Qt.KeepAspectRatio, 
                            mode=Qt.SmoothTransformation
                        )

                        self.pokemon_artwork_label.setPixmap(scaled_pixmap)
                    else:
                        print("Failed to load Pokémon artwork.")
                except Exception as e:
                    print(f"Failed to load artwork image: {e}")
             else:
                 print("Pokémon not found.")
        else:
           print("Please enter a Pokémon name.")

    def capture_pokemon(self):
        if self.pokemon_artwork_url:
            response = requests.get(self.pokemon_artwork_url)

            if response.status_code == 200:
               
                capture_path = os.path.join('captures', f"{self.pokemon_name}.png")
  
                os.makedirs('captures', exist_ok=True)
                
                with open(capture_path, "wb") as image_file:
                    image_file.write(response.content)
                print("Pokémon captured!")

                QMessageBox.information(self, "Pokemon Captured", f"{self.pokemon_name} is captured!")

                self.captured_pokemon.append({
                    'name': self.pokemon_name,
                    'image': f"{self.pokemon_name}.png",
                    'stats': [f"{stat_name}: {stat_value}" for stat_name, stat_value in self.pokemon_stats.items()],
                    'abilities': self.pokemon_abilities
                })
            else:
                print("Failed to capture Pokémon image.")
                
    def open_display_window(self):
        if self.captured_pokemon:  
           self.display_window = DisplayWindow()
           self.display_window.show()

if __name__ == "__main__":
    app = QApplication([])
    window = SearchWindow()
    window.show()
    app.exec()
