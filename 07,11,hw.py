

class Book():
    pass

def create_book(title, author, year_of_publish, genre, no_of_pages):
    book = Book()
    book.title = title
    book.author = author
    book.year_of_publish = year_of_publish
    book.genre = genre
    book.number_of_pages = no_of_pages
    return book

# title, author, genre, year_of_publish, no_of_pages
myBook = Book()
myBook.__dict__['title'] = "Harry Potter and the Sorcerer's Stone"
myBook.__dict__['author'] = 'J.K.rowling'
myBook.__dict__['year_of_publish'] = 1999
myBook.__dict__['number_of_pages'] = 1003
myBook.__dict__['1genre'] = 'fantazy'

myBook_again = Book()
myBook_again.title = "Harry Potter and the Sorcerer's Stone"
myBook_again.author = 'J.K.rowling'
myBook_again.year_of_publish = 1999
myBook_again.genre = 'fantazy'
myBook_again.number_of_pages = 1003

my_book_fun = create_book('J.K.rowling', \
                          'Harry Potter and the Sorcerer\'s Stone'
                          , 1999, 'fantazy', 1003)
print(my_book_fun.__dict__)

book_harry = create_book('J.K.rowling', \
                          'Harry Potter and the Sorcerer\'s Stone'
                          , 1999, 'fantazy', 1003)

book_catch22 = create_book('Joseph Heller', \
                          'catch 22'
                          , 1970, 'comedy', 800)

book_winnie_z_pooh = create_book('A.A.Millen', \
                          'Winnie the Pooh'
                          , 1921, 'children', 50)

_lib = [book_harry, book_catch22, book_winnie_z_pooh]
_lib_dict = {
    #'Harry Potter and the Sorcerer\'s Stone' : harry,
    #harry.title: harry,
    'Harry Potter and the Sorcerer\'s Stone' : book_harry,
    'catch 22' : book_catch22,
    'Winnie the Pooh' : book_winnie_z_pooh
}
lend_a_book = _lib_dict.pop('catch 22')
print(lend_a_book.__dict__)
print(len(_lib_dict))

class Car:
    pass

honda = Car()
honda.color = 'red'
honda.year = 2022
honda.model = 'Civic'
