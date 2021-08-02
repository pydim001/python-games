import requests
import random
from bs4 import BeautifulSoup

def search():
    web = requests.get("https://wordfinder.yourdictionary.com/letter-words/15/")
    soup = BeautifulSoup(web.text, 'html.parser')
    blet = soup.find_all('div', attrs={"class":"table-cell table-results-cell table-cell-word"})
    rand = random.randint(0, len(blet))
    return blet[rand].text

def dict_words():
    web = requests.get("http://www.mieliestronk.com/corncob_lowercase.txt")
    soup = BeautifulSoup(web.text, 'html.parser')
    english_words = list(soup)[0].strip("\r").split()
    select = random.choice(english_words)
    return select

def famous():
    web = requests.get("https://www.famousscientists.org/list/")
    soup = BeautifulSoup(web.text, 'html.parser')
    blet = soup.find_all('a')
    rand = random.randint(11, len(blet)-11)
    return blet[rand].text.lower()

def us():
    web = requests.get("https://www.britannica.com/topic/list-of-cities-and-towns-in-the-United-States-2023068")
    soup = BeautifulSoup(web.text, 'html.parser')
    blet = soup.find_all('a', attrs={'class':'md-crosslink'})
    rand = random.randint(4, len(blet))
    return blet[rand].text.lower()

def india():
    web = requests.get("https://www.britannica.com/topic/list-of-cities-and-towns-in-India-2033033")
    soup = BeautifulSoup(web.text, 'html.parser')
    blet = soup.find_all('a', attrs={'class':'md-crosslink'})
    rand = random.randint(4, len(blet))
    return blet[rand].text.lower()

def fruit():
    web = requests.get("https://vegetarian.lovetoknow.com/Fruit_Alphabetical_List")
    soup = BeautifulSoup(web.text, 'html.parser')
    blet = soup.find_all('li')
    rand = random.randint(174, 246)
    return blet[rand].text.lower()

def man1():
    print('---------')
    print('|       |')
    print('|')
    print('|')
    print('|')
    print('|')

def man2():
    print('---------')
    print('|       |')
    print('|       0')
    print('|')
    print('|')
    print('|')

def man3():
    print('---------')
    print('|       |')
    print('|       0')
    print('|       |')
    print('|')
    print('|')

def man4():
    print('---------')
    print('|       |')
    print('|       0')
    print('|      \|')
    print('|')
    print('|')

def man5():
    print('---------')
    print('|       |')
    print('|       0')
    print('|      \|/')
    print('|')
    print('|')

def man6():
    print('---------')
    print('|       |')
    print('|       0')
    print('|      \|/')
    print('|      /')
    print('|')

def man7():
    print('---------')
    print('|       |')
    print('|       0')
    print('|      \|/')
    print('|      / \ ')
    print('|')

def repla(string):
    rep = ""
    for letter in string:
        if letter.isalpha():
            rep += "_ "
        elif letter == " ":
            rep += letter + " "
        else:
            rep += letter
    return rep

def nrepla(string):
    rep = ""
    for letter in string:
        if letter.isalpha() or letter == " ":
            rep += letter + " "
        else:
            rep += letter
    return rep

def guess(inp, repla, nrepla):
    for str in range(len(nrepla)):
        if inp == nrepla[str]:
            repla = repla[:str] + nrepla[str] + repla[str+1:]
    return repla


def play(string):
    miss = 0
    tried = ""
    man1()
    let = input(repla(string) + '\n')
    mguess = guess(let, repla(string), nrepla(string))
    if let not in string:
        tried += let
    while "_" in mguess and len(tried) < 6:
        if len(tried) == 0:
            man1()
        if len(tried) == 1:
            man2()
        if len(tried) == 2:
            man3()
        if len(tried) == 3:
            man4()
        if len(tried) == 4:
            man5()
        if len(tried) == 5:
            man6()
        net = input(mguess + '\n' + tried + '\n')
        let = net
        if let in tried:
            print('You already guessed this letter')
        if let not in string and let not in tried:
            miss += 1
            tried += let
        mguess = guess(let, mguess, nrepla(string))
    if len(tried) == 6:
        man7()
        print("Word is: " + string)
        print("You lost")
    else:
        print(mguess)
        print("Misses: " + str(miss))
        print("You Win")


play(dict_words()) #You cna change the words you want to play with
