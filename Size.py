import sys
from Card import Card

print(sys.getsizeof(Card("A", "Hearts", "ace_of_hearts.png")))
print(sys.getsizeof(Card("5", "Spades", "5_of_spades.png")))