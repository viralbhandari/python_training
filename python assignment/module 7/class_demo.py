import random
class Coin:
    def __init__(self):
        self.sideup='Heads'
    def toss(self):
        if random.randint(0,1)==0:
            self.sideup='Heads'
        else:
            self.sideup='Tails'
    def get_sideup(self):
        return self.sideup
def main():
    my_coin=Coin()
    print('this side is up:',my_coin.get_sideup())
    print('I anm tossing the coin')
    my_coin.toss()
    print('THis side is up:',my_coin.get_sideup())
main()
