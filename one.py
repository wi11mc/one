import tkinter as tk
from tkinter import filedialog

class TextEditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ONE")
        self.geometry("800x600")

        self.text_area = tk.Text(self, wrap='word', bg="#1e1e1e", fg="white", insertbackground="white", selectbackground="blue")
        self.text_area.pack(fill='both', expand=True)
        self.text_area.bind('<Key>', self.update_status_bar)

        self.status_bar = tk.Label(self, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        self.menu_bar = tk.Menu(self)

        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)
        self.menu_bar.add_cascade(label="File", menu=file_menu)

        edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        edit_menu.add_command(label="Cut", command=self.cut_text)
        edit_menu.add_command(label="Copy", command=self.copy_text)
        edit_menu.add_command(label="Paste", command=self.paste_text)
        self.menu_bar.add_cascade(label="Edit", menu=edit_menu)

        self.config(menu=self.menu_bar)

        self.update_status_bar()  # Update status bar initially

    def new_file(self):
        self.text_area.delete('1.0', tk.END)
        self.update_status_bar()

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as file:
                self.text_area.delete('1.0', tk.END)
                self.text_area.insert('1.0', file.read())
                self.update_status_bar()

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension='.txt')
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.text_area.get('1.0', tk.END))

    def cut_text(self):
        self.clipboard_clear()
        self.clipboard_append(self.text_area.get(tk.SEL_FIRST, tk.SEL_LAST))
        self.text_area.delete(tk.SEL_FIRST, tk.SEL_LAST)
        self.update_status_bar()

    def copy_text(self):
        self.clipboard_clear()
        self.clipboard_append(self.text_area.get(tk.SEL_FIRST, tk.SEL_LAST))

    def paste_text(self):
        self.text_area.insert(tk.INSERT, self.clipboard_get())
        self.update_status_bar()

    def update_status_bar(self, event=None):
        cursor_pos = self.text_area.index(tk.INSERT)
        line, column = cursor_pos.split('.')
        cursor_pos_str = f"Cursor Position: Line {line}, Column {column}"

        text_content = self.text_area.get('1.0', tk.END)
        word_count = len(text_content.split())
        char_count = len(text_content.replace('\n', ''))

        status_text = f"{cursor_pos_str} | Word Count: {word_count} | Character Count: {char_count}"
        self.status_bar.config(text=status_text)

if __name__ == "__main__":
    app = TextEditor()
    app.mainloop()
    