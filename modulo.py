import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.uix.widget import Widget
import tkinter as tk
from tkinter import filedialog


class MyGridLayout(GridLayout):
    file1GUI = StringProperty('')
    file2GUI = StringProperty('')

    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text="Select 'followers' file: "))
        self.file1_button = Button(text='Browse')
        self.file1_button.bind(on_press=self.browse_file1)
        self.add_widget(self.file1_button)

        self.file1_label = Label(text='No file selected')
        self.add_widget(self.file1_label)
        self.add_widget(Widget())

        self.add_widget(Label(text="Select 'following' file: "))
        self.file2_button = Button(text='Browse')

        self.file2_button.bind(on_press=self.browse_file2)
        self.add_widget(self.file2_button)

        self.file2_label = Label(text='No file selected')
        self.add_widget(self.file2_label)

        self.add_widget(Label())  # empty label for spacing
        self.submit = Button(text='Submit', font_size=40,
                             size_hint=(None, None), size=(180, 70))

        self.submit.bind(on_press=self.submit_button)

        # Add an empty widget to the left of the button to center it
        self.add_widget(Widget())
        self.add_widget(self.submit)
        self.add_widget(Widget())

    def browse_file1(self, instance):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file1GUI = file_path
            self.file1_label.text = self.file1GUI

    def browse_file2(self, instance):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file2GUI = file_path
            self.file2_label.text = self.file2GUI

    def submit_button(self, instance):
        try:
            if self.file1GUI and self.file2GUI:
                App.get_running_app().stop()
        except:
            pass


class MyApp(App):
    def __init__(self, on_files_selected_callback, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        self.on_files_selected_callback = on_files_selected_callback

    def build(self):
        return MyGridLayout()

    def on_stop(self):
        self.on_files_selected_callback(self.root.file1GUI, self.root.file2GUI)
