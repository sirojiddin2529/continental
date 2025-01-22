from models.room import Room
from models.user import User
from models.book import Book
from pprint import pprint
def menu():
    print("""
Buyruqlar ketmaketligi: 
Ruyxatdan o`tish: 1
Dasturga kirish:  2
Chiqish: 3
        """)
    
def book_user(rooms: Room, user_book: User):
    
   
    while True:
        print("""
Buyruqlar ketmaketligi: 
Xonalar haqida ma`lumotni olish: 1
Xonani band qilish:  2
Orqaga: 3
Dasturdan chiqish: 4
        """)
        number = input("Buyruqni kiriting: ")
        if number == '1':
            print("Xonalar ruyxati: ")
            for xona in rooms:
                print(f"Xona nommiri: {xona['number']}\nXonalar soni: {xona["size"]}\nXona narxi: {xona["price"]}\nXona turi: {xona["type"]}\n")
        
        elif number == '2':
            while True:
                number_room = input("Bant qilmoqchi bo`lgan xona nomirini kiriting: ")
                for xona in rooms:
                    if str(number_room) == str(xona["number"]):
                        print("Sizning tanlovingiz juda ajoyib bo`ldi\n")
                        return Book(user_book, xona)
                print("Siz kiritkan nommir bron qilingan, iltimos boshqa nomirni tanlang!\n")
        elif number == '3':
            break
        elif number == '4':
            print("Bizni hizmatimizdan foydalanganingizdan hursandmiz :)\n")
            exit()  
        else:        
            print("Siz noto`g`ri buyrug kiritdingiz\n")
            