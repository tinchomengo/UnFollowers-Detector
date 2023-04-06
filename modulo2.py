import tkinter as tk
from tkinter import filedialog


class MyApp:
    def __init__(self, on_files_selected_callback):
        self.root = tk.Tk()
        self.root.geometry("1000x250")
        self.root.title('File Selector')
        self.root.configure(bg='black')
        self.root.resizable(False, False)
        self.on_files_selected_callback = on_files_selected_callback

        self.file1_path = ''
        self.file2_path = ''

        self.file1_button = tk.Button(self.root, text="Select 'followers' file", bg='grey', fg='white', font=(
            'Arial', 12), width=25, height=2, command=self.browse_file1)
        self.file1_button.grid(row=0, column=0, padx=10, pady=10)

        self.file1_label = tk.Label(
            self.root, text='No file selected', bg='black', fg='white', font=('Arial', 12))
        self.file1_label.grid(row=0, column=1, padx=50, pady=10, sticky='W')

        self.file2_button = tk.Button(self.root, text="Select 'following' file", bg='grey', fg='white', font=(
            'Arial', 12), width=25, height=2, command=self.browse_file2)
        self.file2_button.grid(row=1, column=0, padx=50, pady=10)

        self.file2_label = tk.Label(
            self.root, text='No file selected', bg='black', fg='white', font=('Arial', 12))
        self.file2_label.grid(row=1, column=1, padx=50, pady=10, sticky='W')

        self.submit_button = tk.Button(self.root, text='Submit', bg='grey', fg='white', font=(
            'Arial', 16), width=10, height=2, command=self.submit_files)
        self.submit_button.grid(row=2, column=1, padx=10, pady=10, sticky='SW')

    def browse_file1(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file1_path = file_path
            self.file1_label.configure(text=self.file1_path)

    def browse_file2(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file2_path = file_path
            self.file2_label.configure(text=self.file2_path)

    def submit_files(self):
        if self.file1_path and self.file2_path:
            self.on_files_selected_callback(self.file1_path, self.file2_path)
            self.root.destroy()

    def run(self):
        self.root.mainloop()
