import sys
import tkinter as tk


class ListaApp:
    def __init__(self, output_string):
        self.output_string = output_string

        self.window = tk.Tk()
        self.window.title("Unfollowers List")

        scrollbar = tk.Scrollbar(self.window)
        scrollbar.pack(side="right", fill="y")

        self.text = tk.Text(self.window, wrap="word",
                            yscrollcommand=scrollbar.set)
        self.text.pack(side="left", fill="both", expand=True)

        scrollbar.config(command=self.text.yview)
        self.text.insert("1.0", self.output_string)

    def run(self):
        self.window.mainloop()


if __name__ == '__main__':
    # Retrieve the output string from the command line arguments
    output_string = sys.argv[1]

    # Launch the Tkinter app
    app = ListaApp(output_string)
    app.run()
