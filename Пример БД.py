'''
Таблица "Книги":
Поля: id, название, автор, год издания, уникальный номер (ISBN), доступность (в библиотеке/выдана).

Таблица "Читатели":
Поля: имя, ID читателя.

Таблица реестр записей:
Поля: id записи, id книги, id читателя, дата когда взяли книгу, дата когда вернули книгу.

'''

import sqlite3

def make_data_base():
    con = sqlite3.connect('library.db')
    cur = con.cursor()
    # Создаем таблицу "Книги"
    cur.execute('''
    CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER,
    isbn TEXT UNIQUE,
    isAvialable BOOLEAN
    )    
    ''')
    # Создаем таблицу "Читатели"
    cur.execute('''
    CREATE TABLE IF NOT EXISTS readers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
    )
    ''')
    # Создаем таблицу "Реестр записей (реестр выдачи и возврата книг)"
    cur.execute('''
    CREATE TABLE IF NOT EXISTS borrow_records(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER,
    reader_id INTEGER,
    borrow_date DATE,
    return_date DATE,
    FOREIGN KEY (book_id) REFERENCES books(id) ON DELETE CASCADE,
    FOREIGN KEY (reader_id) REFERENCES readers(id) ON DELETE CASCADE
    )    
    ''')
    con.commit()
    con.close()


# make_data_base()
def inserts_tests_data():
    books_list = [
        ["Война и мир", "Лев Толстой", 1869, "978-5171185054"],
        ["Преступление и наказание", "Федор Достоевский", 1866, "978-5170855392"],
        ["Мастер и Маргарита", "Михаил Булгаков", 1967, "978-5699823574"],
        ["Анна Каренина", "Лев Толстой", 1877, "978-5171209781"],
        ["Идиот", "Федор Достоевский", 1869, "978-5170842927"],
        ["Тихий Дон", "Михаил Шолохов", 1940, "978-5170579496"],
        ["Доктор Живаго", "Борис Пастернак", 1957, "978-5170909835"],
        ["Мертвые души", "Николай Гоголь", 1842, "978-5171094783"],
        ["Обломов", "Иван Гончаров", 1859, "978-5171126934"],
        ["Отцы и дети", "Иван Тургенев", 1862, "978-5170860570"],
        ["Евгений Онегин", "Александр Пушкин", 1833, "978-5171173389"],
        ["Герой нашего времени", "Михаил Лермонтов", 1840, "978-5171109678"],
        ["Двенадцать стульев", "Илья Ильф, Евгений Петров", 1928, "978-5171142873"],
        ["Золотой теленок", "Илья Ильф, Евгений Петров", 1931, "978-5171142874"],
        ["Белая гвардия", "Михаил Булгаков", 1925, "978-5171109692"],
        ["Пикник на обочине", "Аркадий и Борис Стругацкие", 1972, "978-5171087594"],
        ["Человек-невидимка", "Герберт Уэллс", 1897, "978-5171094677"],
        ["Замок", "Франц Кафка", 1926, "978-5170986232"],
        ["451 градус по Фаренгейту", "Рэй Брэдбери", 1953, "978-5171002979"],
        ["Над пропастью во ржи", "Джером Сэлинджер", 1951, "978-5170905998"]
    ]
    names_list = [
        "Иванов Иван Иванович",
        "Петров Петр Петрович",
        "Сидорова Мария Александровна",
        "Кузнецов Николай Николаевич",
        "Смирнова Елена Владимировна",
        "Федоров Михаил Сергеевич",
        "Попова Ольга Игоревна",
        "Васильев Дмитрий Андреевич",
        "Алексеева Анна Викторовна",
        "Николаев Сергей Павлович",
        "Егорова Татьяна Алексеевна",
        "Морозов Алексей Борисович",
        "Волкова Екатерина Михайловна",
        "Соловьев Игорь Константинович",
        "Зайцева Оксана Дмитриевна",
        "Михайлов Андрей Валентинович",
        "Орлова Наталья Романовна",
        "Григорьев Владимир Евгеньевич",
        "Романова Марина Николаевна",
        "Борисов Евгений Ильич"
    ]
    con = sqlite3.connect('library.db')
    cur = con.cursor()

    for i in names_list:
        cur.execute('''
        INSERT INTO readers (name) VALUES (?)
        ''', (i,))
    for i in books_list:
        cur.execute('''
        INSERT INTO books(  name , author, year, isbn, isAvialable)
        VALUES(?, ?, ?, ?, ?)
        ''', (i[0], i[1], i[2], i[3], True))
    con.commit()
    con.close()

    # inserts_tests_data()
    def add_reader(name):
        con = sqlite3.connect('library.db')
        cur = con.cursor()
        cur.execute('''
        INSERT INTO readers (name) VALUES (?)
        ''', (name,))
        con.commit()
        con.close()

    # add_reader('Великанова Марфа Васильевна')

    def add_book(name, author, year, isbn):
        con = sqlite3.connect('library.db')
        cur = con.cursor()
        cur.execute('''
        INSERT INTO books (name,author,year,isbn,isAvialable) 
        VALUES (?,?,?,?,?)
        ''', (name, author, year, isbn, True))
        con.commit()
        con.close()

    # add_book('Гарри Поттер и философский камень','Дж. К. Роулинг',1997,'978-3-16-148410-0')
    import random
    from datetime import datetime

    def add_barrow_record(book_id, reader_id):
        con = sqlite3.connect('library.db')
        cur = con.cursor()
        cur.execute('''
        SELECT isAvialable FROM books WHERE id = ?
        ''', (book_id,))
        book_av = cur.fetchall()
        if len(book_av) == 0:
            print(f'Книга с id {book_id} не найдена!')
            cur.close()
            return
        if book_av[0][0] == False:
            print(f'Книга с id {book_id} не доступна для выдачи!')
            cur.close()
            return
        borrow_date = datetime.now().strftime('%Y-%m-%d')
        cur.execute('''
        INSERT INTO borrow_records (book_id, reader_id, borrow_date)
        VALUES (?, ?, ?)
        ''', (book_id, reader_id, borrow_date))
        cur.execute('''
        UPDATE books 
        SET isAvialable = ?
        WHERE id = ?
        ''', (False, book_id))
        con.commit()
        con.close()

    # make_data_base()
    # inserts_tests_data()
    # for i in range(0,10):
    #     add_barrow_record(random.randint(0,20),random.randint(0,20))
    def return_book(book_id):
        con = sqlite3.connect('library.db')
        cur = con.cursor()
        cur.execute('''
        SELECT id FROM borrow_records WHERE book_id = ?
        ''', (book_id,))
        record_id = cur.fetchall()[0][0]
        return_date = datetime.now().strftime('%Y-%m-%d')
        cur.execute('''
        UPDATE borrow_records
        SET return_date = ?
        WHERE id = ?
        ''', (return_date, record_id))
        cur.execute('''
            UPDATE books 
            SET isAvialable = ?
            WHERE id = ?
            ''', (True, book_id))
        con.commit()
        con.close()

    # return_book(11)

    def display_all_borrow_records():
        con = sqlite3.connect('library.db')
        cur = con.cursor()
        cur.execute('''
        SELECT br.id, b.name, r.name, br.borrow_date, br.return_date
        FROM borrow_records br
        JOIN books b ON br.book_id = b.id
        JOIN readers r ON br.reader_id = r.id
        ORDER BY br.id
        ''')
        records = cur.fetchall()
        print(f'{'Реестр записи выдачи и возврата книг:':^110}')
        print(f'{'Книга':<40} {'Читатель':<40} {'Дата выдачи':<15} {'Дата возврата':<15}')
        print('-' * 110)
        for i in records:
            book_name = i[1]
            reader_name = i[2]
            borrow_date = i[3]
            return_date = i[4] if i[4] else 'Не возвращена'

            print(f'{book_name:<40} {reader_name:<40} {borrow_date:<15} {return_date:<15}')
        con.close()

    # display_all_borrow_records()

    def list_of_book_to_return():
        con = sqlite3.connect('library.db')
        cur = con.cursor()
        cur.execute('''
        SELECT br.id, b.name, r.name, br.borrow_date, br.return_date
        FROM borrow_records br    
        JOIN books b ON br.book_id = b.id
        JOIN readers r ON br.reader_id = r.id
        WHERE return_date IS NULL
        ORDER BY br.id
        ''')
        records = cur.fetchall()
        print(f'{'Список книг, которые должны вернуть:':^110}')
        print(f'{'Книга':<40} {'Читатель':<40} {'Дата выдачи':<15} {'Дата возврата':<15}')
        print('-' * 110)
        for i in records:
            book_name = i[1]
            reader_name = i[2]
            borrow_date = i[3]
            return_date = i[4] if i[4] else 'Не возвращена'
            print(f'{book_name:<40} {reader_name:<40} {borrow_date:<15} {return_date:<15}')
            con.close()

        # list_of_book_to_return()
        def books_in_stock():
            con = sqlite3.connect('library.db')
            cur = con.cursor()
            cur.execute('''
                SELECT name, author, year FROM books
                WHERE isAvialable = 1
                ''')
            books = cur.fetchall()
            print(f'{'Список книг в наличии:':^110}')
            print(f"{'Книга':<40} {'Автор':<40} {'Год написания':<15}")
            print('-' * 110)
            for i in books:
                book_name = i[0]
                author = i[1]
                year = i[2]
                print(f'{book_name:<40} {author:<40} {year:<15}')
            con.close()

        list_of_book_to_return()
        books_in_stock()
        print('Вернем книгу с id 17')
        return_book(17)
        books_in_stock()
stroka=''
print('Добро пожаловать!')
while stroka != "7":
    if stroka == '1':
        # name, author, year, isbn
        book_name = input('Введите название книги: ')
        author = input('Введите автора: ')
        year = input('Введите год написания книги: ')
        isbn = input('Введите номер ISBN: ')
        add_book(book_name, author, year, isbn)
    elif stroka == '2':
        reader_name = input('Введите имя читателя: ')
        add_reader(reader_name)
    elif stroka == '3':
        book_id=input('Введите id книги: ')
        reader_id=input('Введите id читателя: ')
        add_barrow_record(book_id,reader_id)
    elif stroka == '4':
        return_book_id=input('Введите id книги для возвращения: ')
        return_book(return_book_id)
    elif stroka == '5':
        books_in_stock()
    elif stroka == '6':
        list_of_book_to_return()

    print('Выберите действие:')
    print('1. Добавить книгу')
    print('2. Добавить читателя')
    print('3. Взять книгу')
    print('4. Вернуть книгу')
    print('5. Посмотреть список книг в наличии')
    print('6. Посмотреть список книг, которые должны вернуть')
    print('7. Выход')
    stroka = input('Введите значение: ')