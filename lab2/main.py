import tkinter as tk
from tkinter import filedialog
import json


class UIConstructor:
    def __init__(self):
        self.metadata_file = None
        self.elements = []

        self.root = tk.Tk()
        self.root.title("UI Constructor")
        self.create_menu()
        self.entry = None

    def create_menu(self):
        self.menu_bar = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Open Metadata File", command=self.select_metadata_file)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.root.config(menu=self.menu_bar)

    def select_metadata_file(self):
        self.metadata_file = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if self.metadata_file:
            self.clear_form()
            self.load_metadata()
            self.create_elements()
            self.root.update()

    def clear_form(self):
        for widget in self.root.winfo_children():
            widget.destroy()

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
            elif element_type == 'entry':
                self.create_entry(element)

    def create_form(self, element):
        self.root.geometry(f"{element['width']}x{element['height']}")

    def create_label(self, element):
        label = tk.Label(self.root, text=element['text'])
        label.place(x=element['x'], y=element['y'], width=element['width'], height=element['height'])

    def create_button(self, element):
        button = tk.Button(self.root, text=element['text'])
        button.place(x=element['x'], y=element['y'], width=element['width'], height=element['height'])

    def create_entry(self, element):
        self.entry = tk.Entry(self.root)
        self.entry.place(x=element['x'], y=element['y'], width=element['width'], height=element['height'])

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    constructor = UIConstructor()
    constructor.run()
