import sys
import requests
import json
import apis

from urllib.request import Request, urlopen
from urllib.parse import urlencode


def _request(symbol, stat):
    url = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % (symbol, stat)
    req = Request(url)
    resp = urlopen(req)
    return str(resp.read().decode('utf-8').strip())

def get_price(symbol):
    return _request(symbol, 'l1')


def square(n):
    """ Square numbers

    >>> square(2)
    4
    >>> square(3)
    8
    """
    return n*n

def dispatcher(command, arg):
    """ Does things """
    if command == "weather":
        print("Here's the weather forcast for "+arg)
        print(apis.fetch_weather(arg))
    if command == "square":
        print("The square of " + arg + " is " + str(square(int(arg))))
    elif command == "go away":
        print("It sounds like you no longer need my assistance")
        print("Very well. Goodbye!")
        return
    elif command == "bye":
        print("Goodbye! Have a good day!")
        return
    # Reprompt the user.
    prompter()


def prompter():
    """ asks for things """

    command = (input("How may I help you?: [weather, square, go away, bye]")).lower()
    if command == "weather":
        city = input("Sure thing! What city?")
        dispatcher(command, city)
    if command == "square":
        num = input("I love math! What number?")
        dispatcher(command, num)
    elif command == "stocks":
        symbol = input("Sure thing! What is the symbol of the stock?")
        get_price(symbol)
    else:
        dispatcher(command, "")

def starter(cliargs):
    # TODO: Finish up command line interface
    print("DEBUG: Called with ", cliargs[1:])

    print("Summoning Jarvis")
    print("Good evening!")

    if (len(cliargs) > 1):
        command = cliargs[1]
        arg = cliargs[2]
        # TODO: Call dispatcher with args instead of prompting user.
        dispatcher(command, arg)
    else:
        prompter()

#this is a comment
def dance():
    """Every personal assistant should know how to dance!"""
    print("left right chachacha left right chacha\n left left right right dip up chachacha")
    return

if __name__ == "__main__":
    starter(sys.argv)
