'''
Snake console game.
Implementation with curses library.
'''

import argparse
import sys
import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP
from random import randint

__author__ = 'Partly by Olexander Gerasymenko'


class Snake(object):
    '''
    define Snake object, set control keys, score, etc.
    '''
    REV_DIR_MAP = {
        KEY_UP: KEY_DOWN, KEY_DOWN: KEY_UP,
        KEY_LEFT: KEY_RIGHT, KEY_RIGHT: KEY_LEFT,
    }

    def __init__(self, x, y, window):
        self.body_list = []
        self.hit_score = 0
        self.timeout = TIMEOUT

        # snake body
        for i in range(SNAKE_LENGTH, 0, -1):
            self.body_list.append(Body(x - i, y))

        # snake head
        self.body_list.append(Body(x, y, '0'))
        self.window = window
        # move snake to right when game starts
        self.direction = KEY_RIGHT
        self.last_head_coor = (x, y)
        # direction map
        self.direction_map = {
            KEY_UP: self.move_up,
            KEY_DOWN: self.move_down,
            KEY_LEFT: self.move_left,
            KEY_RIGHT: self.move_right
        }

    # getter with information about score and gamer name
    @property
    def score(self):
        return 'Score: {0} | Gamer: {1}'.format(self.hit_score, gamer_name)

    # add item to snake body
    def add_body(self, body_list):
        self.body_list.extend(body_list)

    # eat food function
    def eat_food(self, food):
        food.reset()
        body = Body(self.last_head_coor[0], self.last_head_coor[1])
        self.body_list.insert(-1, body)
        # update game score
        self.hit_score += 1
        # change speed
        if self.hit_score % 3 == 0:
            self.timeout -= 5
            self.window.timeout(self.timeout)

    # if snake head hits body part will be end of game
    @property
    def collided(self):
        return any([body.coor == self.head.coor
                    for body in self.body_list[:-1]])

    # animation
    def update(self):
        last_body = self.body_list.pop(0)
        last_body.x = self.body_list[-1].x
        last_body.y = self.body_list[-1].y
        self.body_list.insert(-1, last_body)
        self.last_head_coor = (self.head.x, self.head.y)
        self.direction_map[self.direction]()

    # function to change direction
    def change_direction(self, direction):
        if direction != Snake.REV_DIR_MAP[self.direction]:
            self.direction = direction

    # add snake body inside window
    def render(self):
        for body in self.body_list:
            self.window.addstr(body.y, body.x, body.char)

    # snake head should always be the first in the body list
    @property
    def head(self):
        return self.body_list[-1]

    # set snake head initial coordinate
    @property
    def coor(self):
        return self.head.x, self.head.y

    # moving functions
    def move_up(self):
        self.head.y -= 1
        if self.head.y < 1:
            self.head.y = MAX_Y

    def move_down(self):
        self.head.y += 1
        if self.head.y > MAX_Y:
            self.head.y = 1

    def move_left(self):
        self.head.x -= 1
        if self.head.x < 1:
            self.head.x = MAX_X

    def move_right(self):
        self.head.x += 1
        if self.head.x > MAX_X:
            self.head.x = 1


class Body(object):
    '''
    define Snake's body object
    '''
    def __init__(self, x, y, char='-'):
        self.x = x
        self.y = y
        self.char = char

    # return coordinates
    @property
    def coor(self):
        return self.x, self.y


class Food(object):
    '''
    define food object
    '''

    # choose random position for food
    def __init__(self, window, char='X'):
        self.x = randint(1, MAX_X)
        self.y = randint(1, MAX_Y)
        self.char = char
        self.window = window

    # use curses.addstr to render object
    def render(self):
        self.window.addstr(self.y, self.x, self.char)

    # choose new random coordinates
    def reset(self):
        self.x = randint(1, MAX_X)
        self.y = randint(1, MAX_Y)


# define function for parsing extra args
def check_arg(args=None):
    '''
    create argparse object to change some default vars
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-U', '--user',
                        help='gamer name',
                        default='AleX')
    parser.add_argument('-W', '--width',
                        help='board width',
                        default=80)
    parser.add_argument('-H', '--height',
                        help='board height',
                        default=40)

    results = parser.parse_args(args)

    # waiting for integers only due to it will use for re-assigment int vars
    try:
        return (results.user,
                int(results.width),
                int(results.height),
                )
    # if except happens print message and exit from program
    except (TypeError, ValueError):
        print('Options HEIGHT, WIDTH accept integers only!')
        sys.exit()


if __name__ == '__main__':
    # define board and snake size
    SNAKE_LENGTH = 5
    SNAKE_X = SNAKE_LENGTH + 1
    SNAKE_Y = 3
    
    # by this var controls the speed of the game
    TIMEOUT = 100

    # assign default vales
    gamer_name, WIDTH, HEIGHT = check_arg(sys.argv[1:])
    MAX_X = WIDTH - 2
    MAX_Y = HEIGHT - 2

    # initializing curses window
    curses.initscr()
    window = curses.newwin(HEIGHT, WIDTH, 0, 0)
    window.timeout(TIMEOUT)
    window.keypad(1)
    # turn off key echo
    curses.noecho()
    curses.curs_set(0)
    window.border(0)

    # initialize snake and food object
    snake = Snake(SNAKE_X, SNAKE_Y, window)
    food = Food(window, 'X')

    # render window and objects
    while True:
        window.clear()
        window.border(0)
        snake.render()
        food.render()

        window.addstr(0, 5, snake.score)
        window.addstr(HEIGHT-1, 5, "Press 'q' to quit")
        event = window.getch()

        # 113 == ascii q, if q - exit from loop
        if event == 113:
            break

        # allow changing snakes direction
        if event in [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT]:
            snake.change_direction(event)

        # implementation eating of food
        if snake.head.x == food.x and snake.head.y == food.y:
            snake.eat_food(food)

        if event == 32:
            key = -1
            while key != 32:
                key = window.getch()

        # call the update Snake class function
        snake.update()

        # if snake collide its body - exit from loop
        if snake.collided:
            break

    # at exit close curses window
    curses.endwin()
