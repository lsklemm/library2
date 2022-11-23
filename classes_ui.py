from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.popup import Popup
from kivymd.uix.textfield import MDTextField
from kivy.uix.textinput import TextInput
from kivymd.uix.tooltip import MDTooltip
from kivy.uix.button import Button
from kivy.factory import Factory
from kivy.uix.widget import Widget

import random

class ScreensManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Application:
    def __init__(self):
        pass


class WindowNotifications(Popup, Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class WindowChooseRole(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def enterAsReader(self):
        pass
    def enterAsWorker(self):
        pass

# Работник
class WindowWelcomeReader(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def enter(self):
        pass
    def registration(self):
        pass

class WindowEnterReader(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def enter(self, number, password):
        pass
    def turn_back(self):
        pass
    def set_login(self, login):
        pass
    def set_password(self, password):
        pass




class WindowRegistrationReader(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def registration(self, number, name, password):
        pass
    def set_password(self, password):
        pass
    def set_login(self, login):
        pass
    def set_name(self, name):
        pass

    def generate_number(self):
        reader_number = '1001'
        generated_number = random.randrange(100, 1000)
        self.ids.login_reader.text = str(reader_number) + str(generated_number)

class WindowMenuReader(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def goToPersonalAccount(self):
        pass
    def goToLibrary(self):
        pass
    def exit(self):
        pass

class WindowPersonalAccountReader(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
class WindowNotificationsReader(Popup, Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class WindowLibraryReader(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def search(self):
        pass

class WindowFinishedBooksReader(Popup, Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class WindowAddedBooksReader(Popup, Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class WindowLikedBooksReader(Popup, Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class WindowBookReader(Popup, Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def addIntoLikedBooks(self, number):
        pass
    def read(self, number):
        pass
    def addBook(self, numer):
        pass


class WindowExitReader(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)



# Читатель
class WorkerLibrary:
    pass



class WindowWelcomeWorker(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def enter(self):
        pass
    def registration(self):
        pass

class WindowEnterWorker(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def enter(self, number, password):
        pass
    def set_login(self, login):
        pass
    def set_password(self, password):
        pass




class WindowRegistrationWorker(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def registration(self, number, name, password):
        pass
    def set_login(self, login):
        pass
    def set_name(self, name):
        pass
    def set_password(self, password):
        pass
    def generate_number(self):
        reader_number = '1111'
        generated_number = random.randrange(100, 1000)
        self.ids.login_worker.text = str(reader_number) + str(generated_number)

class WindowMenuWorker(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class WindowPersonalAccountWorker(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
class WindowNotificationsWorker(Popup, Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class WindowIssuanceOfBooksWorker(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
class WindowCollectingOfBooksWorker(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class WindowRequestForTakingBookWorker(Popup, Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def giveBook(self):
        pass
    def delay(self):
        pass

class WindowRequestForReturnBookWorker(Popup, Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def takeBook(self):
        pass

class WindowExitWorker(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)





class TooltipButton(Button, MDTooltip):
    pass