'''
This program describes Books class, give possibility to add new book, buy a book, show books list with detail's,
show and add feedback's to selected book.
'''

__author__ = 'sashko'


class Books:
    '''
    classdocs
    '''

    # create constants with ASCII symbols for color output
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    PURPLE = '\033[95m'
    WHITE = '\033[0m'

    def __init__(self, title, author, category, year, quantity, username, feeds):
        '''
        Constructor
        '''
        self.title = title
        self.author = author
        self.category = category
        self.year = year
        self.quantity = quantity
        # user name will used on feedback output
        self.username = []
        # empty list for containing feedback's
        self.feeds = []

    # define colors
    def colors(self):
        self.BLUE = ''
        self.GREEN = ''
        self.YELLOW = ''
        self.RED = ''
        self.PURPLE = ''
        self.WHITE = ''

    # create method add_feedback
    def add_feedback(self):
        # ask user name for use it in feedback output
        name = input('Input your name: ')
        # ask to write feedback
        feedback = input('Input your feedback: ')
        # add this to the equal list
        self.username.append(name)
        self.feeds.append(feedback)
        print()

    # create method for printing all feedback's
    def all_feedbacks(self):
        # if feedback's list's are empty print 'No feedback left'
        if len(self.username) == 0:
            print('=' * 19)
            print('{0}{1: <19}{2} {3}'.format(Books.PURPLE, 'Feedback\'s:', Books.WHITE, 'No feedback left yet.'))
            print('=' * 19)
        # else print feedback's
        else:
            print('=' * 19)
            print('{0}{1: <19}{2}'.format(Books.PURPLE, 'Feedback\'s:', Books.WHITE))

            # creating function with 2 args, which will use with map function
            def myfunc(value_1, value_2):
                print('User {0} write next feedback: {1}'.format(value_1, value_2))

            # by map function take items from list's with user name and his feedback
            x = list(map(myfunc, self.username, self.feeds))
            print('=' * 19)
        print()

    # create method for sale book
    def sale_book(self):
        # how many books we have
        items = self.quantity
        if items == 0:
            print('=' * 19)
            print(Books.RED, 'Sold out!', Books.WHITE, sep='')
            print('=' * 19)
            print()
        elif items > 0:
            # print how many books available right now for sale
            print('{0} {1}{2}{3} {4}'.format('You can buy:', Books.GREEN, items, Books.WHITE, 'pcs.'))
            # fold input for correct input
            try:
                quantity = int(input('How many copies you want to buy? '))
                print()
            except ValueError:
                print('=' * 19)
                print('{0}{1}{2}'.format(Books.RED, 'Input a digit!', Books.WHITE))
                print('=' * 19)
                print()
                return
            print()

            # comparison available items with inputed quantity
            if 0 < quantity <= items:
                print('=' * 19)
                print('Thank for buying ', Books.GREEN, quantity, Books.WHITE, ' books!', sep='')
                print('=' * 19)
                print()
            elif quantity > items:
                print('=' * 19)
                print('{0: <19} {1}{2}{3} {4}'.format('You can buy only:', Books.RED, items, Books.WHITE, 'pcs.'))
                print('=' * 19)
                print()
                return self.quantity
            else:
                print('=' * 19)
                print('Incorrect input')
                print('=' * 19)
                print()

            # calculate residue
            items -= quantity
            self.quantity = items
        # return remains
        return self.quantity

    def book_title(self):
        return self.title

    # define method for print detail information about book
    def print_info(self):
        print('{0: <19} {1}'.format('Title:', self.title))
        print('{0: <19} {1}'.format('Author:', self.author))
        print('{0: <19} {1}'.format('Category:', self.category))
        print('{0: <19} {1}'.format('Publication year:', self.year))

        if self.quantity == 0:
            print('{0: <19} {1}{2}{3}'.format('Available quantity:', Books.RED, 'Sold out!', Books.WHITE))
        elif self.quantity > 0:
            print('{0: <19} {1}{2}{3}'.format('Available quantity:', Books.GREEN, self.quantity, Books.WHITE))

        # if no feedback's
        if len(self.username) == 0:
            print('{0: <19} {1}'.format('Latest feedback:', 'No feedback left yet.'))
        # else print latest feedback
        else:
            username = " ".join(self.username[-1:])
            feedback = " ".join(self.feeds[-1:])
            print('{0: <19} {1} {2} {3}'.format('Latest feedback:', username, 'wrote:', feedback))
        print()

# create two sample book's
book_1 = Books('Amazon in Action', 'Steve Sampler', 'IT', '2016', 5, '', '')
book_2 = Books('MongoDB in Action', 'Johny Walker', 'IT', '2015', 3, '', '')

# create list to store all book's. on this list will be added new book's
all_books = [book_1, book_2]


# print number and title for all books in list
def menu_list():
    print('Books list:')
    print()
    for i in all_books:
        print(all_books.index(i) + 1, '. ', Books.BLUE, i.title, Books.WHITE, '.', sep='')
        i.print_info()


# define function for select certain book
def select_book():
    # fold input to protect from incorrect value type
    try:
        number = int(input('Select book: '))
        index = number - 1
        # print title of selected book
        print('{0}{1} {2}{3}{4}{5}'.format(number, '.', Books.BLUE, all_books[index].book_title(), Books.WHITE, '.', sep=''))
        # print all information about book
        all_books[index].print_info()
        # propose to buy selected book
        all_books[index].sale_book()
    except ValueError:
        print('=' * 19)
        print('{0}{1}{2}'.format(Books.RED, 'Input a digit!', Books.WHITE))
        print('=' * 19)
        print()
        # if exception happens return to main menu
        return


# show all feedback's about selected book
def feedback_selected():
    # fold input to protect from incorrect value type
    try:
        number = int(input('Select book: '))
        index = number - 1
        print('{0}{1} {2}{3}{4}{5}'.format(number, '.', Books.BLUE, all_books[index].book_title(), Books.WHITE, '.', sep=''))
        all_books[index].print_info()
        # print all feedback's
        all_books[index].all_feedbacks()
    except ValueError:
        print('=' * 19)
        print('{0}{1}{2}'.format(Books.RED, 'Input a digit!', Books.WHITE))
        print('=' * 19)
        print()
        # if exception happens return to main menu
        return


# define function for adding new feedback
def new_feedback_selected():
    # fold input to protect from incorrect value type
    try:
        number = int(input('Select book: '))
        index = number - 1
        print('{0}{1} {2}{3}{4}{5}'.format(number, '.', Books.BLUE, all_books[index].book_title(), Books.WHITE, '.', sep=''))
        all_books[index].print_info()
        # call add_feedback method for current book to add feedback
        all_books[index].add_feedback()
    except ValueError:
        print('=' * 19)
        print('{0}{1}{2}'.format(Books.RED, 'Input a digit!', Books.WHITE))
        print('=' * 19)
        print()
        # if exception happens return to main menu
        return


# create function to adding new book
def add_new_book():
    input_title = input('Input title: ')
    input_author = input('Input author: ')
    input_category = input('Input category: ')
    # fold input to protect from incorrect value type
    try:
        input_year = int(input('Input publication year: '))
    except ValueError:
        print('=' * 19)
        print('{0}{1}{2}'.format(Books.RED, 'Input a digit!', Books.WHITE))
        print('=' * 19)
        print()
        # if exception happens return to main menu
        return
    input_quantity = int(input('Input available quantity: '))
    # combine inputted values into new book
    new_book = Books(input_title, input_author, input_category, input_year, input_quantity, '', '')
    # add new book to the books list
    all_books.append(new_book)
    print()

# generate menu
while True:
    print('1. Show all books')
    print('2. Add new book')
    print('3. Exit')

    choice = input('> ')
    print()
    if choice == '1':
        # generate submenu
        x = True
        while x:
            menu_list()
            print('1. Buy a book')
            print('2. Show all feedback\'s')
            print('3. Add feedback')
            print('4. Back')

            choice = input('> ')
            print()

            # choice for buying new book
            if choice == '1':
                # call function to select certain book from all books list
                select_book()

            # choice for display all feedback's
            elif choice == '2':
                # call function to select certain book from all books list
                feedback_selected()

            # choice for add new feedback
            elif choice == '3':
                # call function to select certain book from all books list
                new_feedback_selected()

            # if other choice - exit from submenu
            else:
                x = False
    # if choice from main menu equal 2, call function for adding new book
    elif choice == '2':
        add_new_book()

    # else exit from program
    else:
        break
