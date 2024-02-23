import os
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QScrollArea, QPushButton, QHBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class DisplayWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Captured Pokémon")
       

        self.captured_images = self.fetch_captured_images()
        self.current_index = 0  

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.init_ui()
        
    def init_ui(self):
        main_layout = QVBoxLayout()

        button_layout = QHBoxLayout()

        self.image_label = QLabel()
        main_layout.addWidget(self.image_label)
        
        self.pokemon_name_label = QLabel()
        main_layout.addWidget(self.pokemon_name_label)
        self.pokemon_name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        next_button = QPushButton("Next")
        next_button.setFixedSize(160, 60)  
        next_button.setStyleSheet("QPushButton:hover {background-color: red; color:black;} QPushButton { margin: 2px; border: 2px solid red; border-radius: 10px; color:white; background-color:black;}")
    
        
        previous_button = QPushButton("Previous")
        previous_button.setFixedSize(160, 60)  
        previous_button.setStyleSheet("QPushButton:hover {background-color: red; color:black;} QPushButton { margin: 2px; border: 2px solid red; border-radius: 10px; color:white; background-color:black;}")
       
        next_button.clicked.connect(self.show_next_image)
        previous_button.clicked.connect(self.show_previous_image)

        button_layout.addWidget(next_button)
        button_layout.addWidget(previous_button)

        self.central_widget.setLayout(main_layout)

        main_layout.addLayout(button_layout)

        self.central_widget.setLayout(main_layout)

        self.display_image(self.current_index)

    def display_image(self, index):
        if 0 <= index < len(self.captured_images):
            image_path = self.captured_images[index]
            pixmap = QPixmap(image_path)
            self.image_label.setPixmap(pixmap)

            pokemon_name = os.path.splitext(os.path.basename(image_path))[0]
 
            self.pokemon_name_label.setText(f"Name: {pokemon_name}")

    def show_next_image(self):
        self.current_index += 1
        if self.current_index >= len(self.captured_images):
            self.current_index = 0  
        self.display_image(self.current_index)

    def show_previous_image(self):
        self.current_index -= 1
        if self.current_index < 0:
            self.current_index = len(self.captured_images) - 1  
        self.display_image(self.current_index)

    def fetch_captured_images(self):
        captures_directory = 'captures'
        if os.path.exists(captures_directory) and os.path.isdir(captures_directory):
    
            image_files = [os.path.join(captures_directory, filename) for filename in os.listdir(captures_directory) if filename.endswith('.png')]
            return image_files
        else:
            return []

if __name__ == "__main__":
    app = QApplication([])
    window = DisplayWindow()
    window.show()
    app.exec()