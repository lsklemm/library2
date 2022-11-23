from classes_ui.py import *


class LibraryReader:
    def __init__(self):
         pass
     def registrateReader(self, reader):
         pass
     def authenticateReader(self, reader):
         pass
     def setReader(self, reader):
         pass
     def addBook(self,book):
         pass
     def addBookIntoLikedBooks(self, book):
         pass
     def returnBook(self, book):
         pass


class LibraryWorker:
    def __init__(self):
        pass
    def registrateWorker(self, worker):
        pass
    def authenticateWorker(self, worker):
        pass
    def setWorker(self, worker):
        pass
    def checkIncomingRequests(self):
        pass
    def approveRequest(self, request):
        pass
    def declineRequest(self, request):
        pass

class Notification:
    def __init__(self):
        self.name = ''
        self.description = ''

class Registration:
    def __init__(self):
        self.name = ''
        self.password = ''

    def registrate(self, name, password):
        pass

class RegistrationOfWorker(Registration):
    def __init__(self):
        self.ticket_number = ''
        self.status = ''
        self.rating = ''
        self.amount_of_finished_books = 0
        self.amount_of_added_books = 0
        self.list_finished_books = []
        self.list_added_books = []
        self.list_liked_books = []

    def registration(self, name, password, ticket_number, status, rating,
                     amount_of_finished_books,amount_of_added_books,list_finished_books,
                     list_added_books,list_liked_books):
        pass


class RegistrationOfReader(Registration):
    def __init__(self):
        self.card_number = ''
        self.rating = ''

    def registrate(self, name, password, card_number):
        pass

class Authentication:
    def __init__(self):
        self.password = ''
    def authenticate(self, password):
        pass

class AuthenticationOfWorker(Authentication):
    def __init__(self):
        self.card_number = ''
    def authenticate(self, password):
        pass
class AuthenticationOfReader(Authentication):
    def __init__(self):
        self.ticket_number = ''
    def authenticate(self, passwod):
        pass

class Worker:
    def __init__(self):
        self.name = ''
        self.password = ''
        self.card_number = ''
        self.rating = 0

    def checkIncomingRequests(self):
        pass
    def approveRequest(self, request):
        pass
    def declineRequest(self, request):
        pass
class Reader:
    def __init__(self):
        self.name = ''
        self.password= ''
        self.status = ''
        self.rating = ''
        self.amount_of_finished_books = 0
        self.amount_of_added_books = 0
        self.list_finished_books = []
        self.list_added_books = []
        self.list_liked_books = []

    def addBook(self, book):
        pass
    def addBookIntoLikedBooks(self, book):
        pass
    def returnBook(self, book):
        pass
class Book:
    def __init__(self):
        self.name = ''
        self.number = ''
        self.author = ''
        self.book_cover = ''
        self.publishment_year = 0
        self.description = ''
        self.acceptable_reading_time = ''
        self.amount_of_copies = 0
        self.rarity_level = 0
        self.current_reading_time = ''

class Request:
    def __init__(self):
        self.reader_ticket_number = ''
        self.reader_rating = 0
        self.book_number = ''
        self.publishment_year = 0
        self.acceptable_reading_time = ''
        self.amount_of_copies = 0
        self.real_reading_time = ''
