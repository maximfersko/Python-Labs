import tkinter as tk
import json

class UIConstructor:
    def __init__(self, metadata_file):
        self.metadata_file = metadata_file
        self.elements = []

        self.root = tk.Tk()
        self.root.title("UI Constructor")

    def load_metadata(self):
        try:
            with open(self.metadata_file, 'r') as file:
                metadata = json.load(file)
                self.elements = metadata['elements']
        except FileNotFoundError:
            print("Metadata file not found.")
        except json.JSONDecodeError:
            print("Invalid metadata file format.")

    def create_elements(self):
        for element in self.elements:
            element_type = element['type']
            if element_type == 'form':
                self.create_form(element)
            elif element_type == 'label':
                self.create_label(element)
            elif element_type == 'button':
                self.create_button(element)

    def create_form(self, element):
        self.root.geometry(f"{element['width']}x{element['height']}")

    def create_label(self, element):
        label = tk.Label(self.root, text=element['text'])
        label.place(x=element['x'], y=element['y'], width=element['width'], height=element['height'])

    def create_button(self, element):
        button = tk.Button(self.root, text=element['text'])
        button.place(x=element['x'], y=element['y'], width=element['width'], height=element['height'])

    def run(self):
        self.load_metadata()
        self.create_elements()
        self.root.mainloop()

if __name__ == "__main__":
    metadata_file = "metadata.json"
    constructor = UIConstructor(metadata_file)
    constructor.run()
