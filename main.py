from kivymd.app import MDApp
import os
from kivy.lang import Builder
from classes_ui import Application


class LibraryApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.application = Application()



    def build(self):
        return Builder.load_file(os.path.join(os.path.dirname(__file__), "interface.kv"))



if __name__ == '__main__':
    LibraryApp().run()
