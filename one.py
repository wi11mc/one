import tkinter as tk
from tkinter import filedialog

class TextEditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Text Editor")
        self.geometry("800x600")

        self.text_area = tk.Text(self, wrap='word', bg="#1e1e1e", fg="white", insertbackground="white", selectbackground="blue")
        self.text_area.pack(fill='both', expand=True)

        self.menu_bar = tk.Menu(self)

        # File menu
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)
        self.menu_bar.add_cascade(label="File", menu=file_menu)

        # Edit menu
        edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        edit_menu.add_command(label="Cut", command=self.cut_text)
        edit_menu.add_command(label="Copy", command=self.copy_text)
        edit_menu.add_command(label="Paste", command=self.paste_text)
        self.menu_bar.add_cascade(label="Edit", menu=edit_menu)

        self.config(menu=self.menu_bar)

    def new_file(self):
        self.text_area.delete('1.0', tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as file:
                self.text_area.delete('1.0', tk.END)
                self.text_area.insert('1.0', file.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension='.txt')
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.text_area.get('1.0', tk.END))

    def cut_text(self):
        self.clipboard_clear()
        self.clipboard_append(self.text_area.get(tk.SEL_FIRST, tk.SEL_LAST))
        self.text_area.delete(tk.SEL_FIRST, tk.SEL_LAST)

    def copy_text(self):
        self.clipboard_clear()
        self.clipboard_append(self.text_area.get(tk.SEL_FIRST, tk.SEL_LAST))

    def paste_text(self):
        self.text_area.insert(tk.INSERT, self.clipboard_get())

if __name__ == "__main__":
    app = TextEditor()
    app.mainloop()
