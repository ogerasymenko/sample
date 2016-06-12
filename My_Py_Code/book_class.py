__author__ = 'sashko'


class Books:
    arr = []
    feeds = []

    def __init__(self, title, author, category, year, quantity):
        self.title = title
        self.author = author
        self.category = category
        self.year = year
        self.quantity = quantity

    def add_feedback(self):
        name = input('Input your name: ')
        feedback = input('Input your feedback: ')
        Books.arr.append(name)
        Books.feeds.append(feedback)
        print()

    def all_feedbacks(self):
        if len(Books.arr) == 0:
            print('=' * 19)
            print('{0: <19} {1}'.format('Feedback\'s:', 'No feedback left yet.'))
            print('=' * 19)
        else:
            print('=' * 19)
            print('{0: <19}'.format('Feedback\'s:'))

            def myfunc(value_1, value_2):
                print('User {0} write next feedback: {1}'.format(value_1, value_2))

            x = list(map(myfunc, Books.arr, Books.feeds))
            print('=' * 19)
        print()

    def sale_book(self):
        items = self.quantity
        if items == 0:
            print('Sold out!')
            print('=' * 19)
        elif items > 0:
            print('{0} {1} {2}'.format('You can buy:', items, 'pcs.'))
            quantity = int(input('How many copies you want to buy? '))
            print()

            if 0 < quantity <= items:
                print('Thank for buying', quantity, 'books!')
                print('=' * 19)
            elif quantity > items:
                print('{0: <19} {1} {2}'.format('You can buy only:', items, 'pcs.'))
                print('=' * 19)
            else:
                print('Incorrect input')
                print()

            items -= quantity
            self.quantity = items
        return self.quantity

    def book_title(self):
        return self.title

    def print_info(self):
        print('{0: <19} {1}'.format('Title:', self.title))
        print('{0: <19} {1}'.format('Author:', self.author))
        print('{0: <19} {1}'.format('Category:', self.category))
        print('{0: <19} {1}'.format('Publication year:', self.year))

        if self.quantity == 0:
            print('{0: <19} {1}'.format('Available quantity:', 'Sold out!'))
        elif self.quantity > 0:
            print('{0: <19} {1}'.format('Available quantity:', self.quantity))

        if len(Books.arr) == 0:
            print('{0: <19} {1}'.format('Latest feedback:', 'No feedback left yet.'))
        else:
            username = " ".join(Books.arr[-1:])
            feedback = " ".join(Books.feeds[-1:])
            print('{0: <19} {1} {2} {3}'.format('Latest feedback:', username, 'wrote:', feedback))

        print()

book_1 = Books('Amazon in Action', 'Steve Sampler', 'IT', '2016', 5)
book_2 = Books('MongoDB in Action', 'Johny Walker', 'IT', '2015', 3)

all_books = [book_1, book_2]


def menu_list():
    print('Books list:')
    print()
    for i in all_books:
        print(all_books.index(i) + 1, '. ', i.title, '.', sep='')
        i.print_info()


def select_book():
    number = int(input('Select book: '))
    index = number - 1
    print('{0}{1} {2}{3}'.format(number, '.', all_books[index].book_title(), '.', sep=''))
    all_books[index].print_info()
    all_books[index].sale_book()


def feedback_selected():
    number = int(input('Select book: '))
    index = number - 1
    print('{0}{1} {2}{3}'.format(number, '.', all_books[index].book_title(), '.', sep=''))
    all_books[index].print_info()
    all_books[index].all_feedbacks()


def new_feedback_selected():
    number = int(input('Select book: '))
    index = number - 1
    print('{0}{1} {2}{3}'.format(number, '.', all_books[index].book_title(), '.', sep=''))
    all_books[index].print_info()
    all_books[index].add_feedback()

while True:
    print('1. Show all books')
    print('2. Exit')

    choice = input('> ')
    print()
    if choice == '1':
        x = True
        while x:
            menu_list()
            print('1. Buy a book')
            print('2. Show feedback\'s')
            print('3. Add feedback')
            print('4. Back')

            choice = input('> ')
            print()

            if choice == '1':
                select_book()

            elif choice == '2':
                feedback_selected()

            elif choice == '3':
                new_feedback_selected()

            else:
                x = False

    else:
        break