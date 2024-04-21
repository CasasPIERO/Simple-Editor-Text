import tkinter as tk
from tkinter import filedialog, messagebox

class SimpleTextEditor():
    def __init__(self, root):
        self.root = root
        self.text_area = tk.Text(self.root)
        self.text_area.pack(fill=tk.BOTH, expand=1)
        self.current_open_file = ''

    def quit_editor(self):
        if messagebox.askokcancel("Salir", "Seguro que desea salir?"):
            self.root.destroy()

    def create_new_file(self):
        self.text_area.delete("1.0", tk.END)
        self.current_open_file=''

    def open_file(self):
        with open(filedialog.askopenfilename()) as f:
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert("1.0", f.read())
            self.current_open_file = f.name

    def save_file(self):
        if self.current_open_file:
            with open(self.current_open_file, 'w') as f:
                data = self.text_area.get("1.0", tk.END)
                f.write(data)
        else:
            with open(filedialog.asksaveasfilename(), 'w') as f:
                f.write(self.text_area.get("1.0", tk.END))
                self.current_open_file = f.name


root = tk.Tk()
root.geometry("500x500")
root.title("Simple Text Editor")

editor = SimpleTextEditor(root)

menu_bar = tk.Menu(root)
menu_options = tk.Menu(menu_bar, tearoff=0)

menu_options.add_command(label="Nuevo", command=editor.create_new_file)
menu_options.add_command(label="Abrir", command=editor.open_file)
menu_options.add_command(label="Guardar", command=editor.save_file)
menu_options.add_command(label="Salir", command=editor.quit_editor)

root.config(menu=menu_bar)
menu_bar.add_cascade(label="Archivo", menu=menu_options)

root.mainloop()