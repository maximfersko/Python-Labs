import tkinter as tk
from tkinter import filedialog, messagebox
import random


class MemorySimulator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Memory Simulator")

        self.data_file = None
        self.data = []

        self.page_size = 265
        self.current_page = 0

        self.create_menu()
        self.create_widgets()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Create New", command=self.create_new_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        self.root.config(menu=menubar)

    def create_widgets(self):
        self.cell_label = tk.Label(self.root, text="Cell:")
        self.cell_label.grid(row=0, column=0, padx=10, pady=10)

        self.cell_entry = tk.Entry(self.root)
        self.cell_entry.grid(row=0, column=1, padx=10, pady=10)

        self.load_button = tk.Button(self.root, text="Load", command=self.load_cell)
        self.load_button.grid(row=0, column=2, padx=10, pady=10)

        self.data_label = tk.Label(self.root, text="Data:")
        self.data_label.grid(row=1, column=0, padx=10, pady=10)

        self.data_text = tk.Text(self.root, height=10, width=30)
        self.data_text.grid(row=1, column=1, padx=10, pady=10, rowspan=2)

        self.label_label = tk.Label(self.root, text="Label:")
        self.label_label.grid(row=1, column=2, padx=10, pady=10)
        self.frame_left = tk.Frame(self.root)
        self.frame_left.grid(row=0, column=0, padx=10, pady=10)

        # Использование ttk.Button вместо tk.Button
        self.search_button = tk.Button(self.frame_left, text="Search", command=self.search_cell)
        self.search_button.grid(row=0, column=2, padx=10, pady=10)

        self.label_var = tk.StringVar()
        self.label_entry = tk.Entry(self.root, textvariable=self.label_var)
        self.label_entry.grid(row=1, column=3, padx=10, pady=10)

        self.save_button = tk.Button(self.root, text="Save", command=self.save_data)
        self.save_button.grid(row=2, column=2, padx=10, pady=10)

        self.generate_button = tk.Button(self.root, text="Generate File", command=self.generate_file)
        self.generate_button.grid(row=3, column=0, padx=10, pady=10)

        self.prev_page_button = tk.Button(self.root, text="Previous Page", command=self.prev_page)
        self.prev_page_button.grid(row=3, column=1, padx=10, pady=10)

        self.next_page_button = tk.Button(self.root, text="Next Page", command=self.next_page)
        self.next_page_button.grid(row=3, column=2, padx=10, pady=10)

        self.cell_label.grid(row=0, column=0, padx=10, pady=10)

        self.cell_entry = tk.Entry(self.root)
        self.cell_entry.grid(row=0, column=1, padx=10, pady=10)

        self.search_button = tk.Button(self.root, text="Search", command=self.search_cell)
        self.search_button.grid(row=0, column=2, padx=10, pady=10)

        self.load_button = tk.Button(self.root, text="Load", command=self.load_cell)
        self.load_button.grid(row=0, column=3, padx=10, pady=10)

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.display_page()

    def next_page(self):
        total_pages = self.get_total_pages()
        if self.current_page < total_pages - 1:
            self.current_page += 1
            self.display_page()

    def get_current_page(self):
        cell_number = self.cell_entry.get()
        if cell_number.isdigit():
            return int(cell_number) // self.page_size
        else:
            return 0

    def search_cell(self):
        cell_number = self.cell_entry.get()
        if not cell_number.isdigit() or int(cell_number) < 0 or int(cell_number) >= len(self.data):
            messagebox.showerror("Error", "Invalid cell number.")
            return

        self.data_text.delete('1.0', tk.END)
        self.data_text.insert(tk.END, self.data[int(cell_number)])

        self.cell_entry.delete(0, tk.END)
        self.cell_entry.insert(tk.END, str(cell_number))

    def get_total_pages(self):
        return (len(self.data) + self.page_size - 1) // self.page_size

    def display_page(self):
        start_index = self.current_page * self.page_size
        end_index = start_index + self.page_size
        page_data = self.data[start_index:end_index]
        self.data_text.delete('1.0', tk.END)
        self.data_text.insert(tk.END, '\n'.join(page_data))

        if self.current_page == self.get_current_page():
            self.cell_entry.grid(row=0, column=1, padx=10, pady=10)
            self.search_button.grid(row=0, column=2, padx=10, pady=10)
            self.load_button.grid(row=0, column=3, padx=10, pady=10)
        else:
            self.cell_entry.delete(0, tk.END)
            self.cell_entry.grid_remove()
            self.search_button.grid_remove()
            self.load_button.grid_remove()

    def generate_file(self):
        num_pages = int(input("Enter the number of pages: "))
        file_path = filedialog.asksaveasfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            self.data_file = file_path
            self.data = self.generate_random_data(num_pages)
            self.current_page = 0
            self.display_page()

    def generate_random_data(self, num_pages):
        data = []
        for _ in range(num_pages):
            page_data = []
            for _ in range(self.page_size):
                page_data.append('Data {}'.format(random.randint(0, 100)))
            data.extend(page_data)
        return data

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            self.data_file = file_path
            self.load_data()

    def create_new_file(self):
        file_path = filedialog.asksaveasfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            self.data_file = file_path
            self.data = [''] * self.page_size
            self.save_data()

    def load_data(self):
        try:
            with open(self.data_file, 'r') as file:
                self.data = file.read().splitlines()
            self.display_page()
        except IOError:
            messagebox.showerror("Error", "Failed to load data from file.")

    def load_cell(self):
        cell_number = self.cell_entry.get()
        if not cell_number.isdigit() or int(cell_number) < 0 or int(cell_number) >= len(self.data):
            messagebox.showerror("Error", "Invalid cell number.")
            return

        self.display_page()

    def save_data(self):
        if not self.data_file:
            messagebox.showerror("Error", "No data file selected.")
            return

        cell_number = self.cell_entry.get()
        if not cell_number.isdigit() or int(cell_number) < 0 or int(cell_number) >= len(self.data):
            messagebox.showerror("Error", "Invalid cell number.")
            return

        cell_data = self.data_text.get('1.0', tk.END).strip()
        self.data[int(cell_number)] = cell_data

        try:
            with open(self.data_file, 'w') as file:
                file.write('\n'.join(self.data))
            messagebox.showinfo("Success", "Data saved successfully.")
        except IOError:
            messagebox.showerror("Error", "Failed to save data to file.")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    simulator = MemorySimulator()
    simulator.run()
