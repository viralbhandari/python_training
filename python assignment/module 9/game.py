import random
import itertools
class Deck:
    suits = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
    ranks = ('Ace', '2', '3', '4', '5', '6', '7',
             '8', '9', '10', 'Jack', 'Queen', 'King')
    value={'2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven',
           '8':'eight','9':'nine'}
    
    def __init__(self):
        self.deck1 = list(product(Deck.suit,Deck.ranks))
        random.shuffle(self.deck1)
   
    def shuffle(self): 
        random.shuffle(self.deck1)

    def next_card(self):
        if len(self.deck1)==0:
            return 0
        else:
            return self.deck1.pop()
    def __str__(self):
        return str (self.deck1)

class Card(Deck):
    def __init__(self,deck):
        self.card = deck.draw_card()
        if self.card==0:
            raise Exception ('all card are over')
        self.suit=self.card[0]
        self.rank=self.card[1]
        self.value=self.value[self.rank]
        

    def __str__(self):
        return f'{self.rank} of {self.suit}'
    def getval(self):
        return self.value
def sel_val():
    a=int(input("enter your number: \n"))
    if not a in range(1,201):
        print("enter number between 1 and 200")
        exit()
    b=random.randint(1,200)
    return a,b

def game(lst,deck):
    lst.append(Card(deck))
    return lst[-1].value

player,computer=sel_val()
pcount,ccount=0,0
plst=[]
cmplst=[]
dec=Deck()

while True:
    try:
        pcount+=game(pllst,dec)
        if pcount==player:
            print('you won')
            break
        ccount+=game(cmplst,dec)
        if ccount==player:
            print('you lost,computer number was',{computer})
            break
    except Exception:
        print('It was a tie')
        if pcount>ccount:
            print('you won the tiebreaker your score {pcount} was higher than computer {ccount}')
        else:
            print('you lost the tiebreaker your score {pcount} was lower than computer {ccount}')
        break
 
    
    
