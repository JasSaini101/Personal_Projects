from bakery import assert_equal
from random import randint


def convert_hand(num: int) -> str:
    ''' 
    function:
        convert_hand: turns an integer from 2-14 into the corresponing string in Poker using if statements
    args:
        num: the integers that got generated/dealt
    return:
        str: a string of readable poker cards 
    '''
    
    if 1 < num < 10:
        return(str(num)+ " ")
    elif num == 10:
        return("X ")
    elif num == 11:
        return("J ")
    elif num == 12:
        return("Q ")
    elif num == 13:
        return("K ")
    elif num == 14:
        return("A ")
    else:
        return(None)
    
def hand_to_string(hand: list[int]) -> str:
    '''   
    function:
        hand_to_string: turns a list of random integers and returns them as a readable poker hand string  
    args:
        hand: a list of integers that got generated/dealt
    return:
        str: a string of three poker cards
    '''
    
    if hand:
        return(convert_hand(hand[0]) + hand_to_string(hand[1:]))
    else:
        return("")

def sort_hand(hand: list[int]) -> list[int]:
    '''    
    function:
        sort_hand: rearranges the element in a list from greatest to least
    args:
        hand: a list of integers that got generated/dealt
    return:
        list[int]: a list of integers ordered from greatest to least  
    '''
    if hand[0] > hand[1] and hand[0] > hand[2]:
        one = hand[0]
        if hand[1] > hand[2]:
            two = hand[1]
            three = hand[2]
            return([one,two,three])
        else:
            three = hand[1]
            two = hand[2]
            return([one,two,three])
    elif hand[1] > hand[2]:
        one = hand[1]
        if hand[0] > hand[2]:
            two = hand[0]
            three = hand[2]
            return([one,two,three])
        else:
            three = hand[0]
            two = hand[2]
            return([one,two,three])
    else:
        one = hand[2]
        if hand[0] > hand[1]:
            two = hand[0]
            three = hand[1]
            return([one,two,three])
        else:
            three = hand[0]
            two = hand[1]
            return([one,two,three])
        
def has_triple(hand: list[int]) -> bool:
    '''
    function:
        has_triple: checks if all 3 of the elements in a list are the equivalent
    args:
        hand: a list of integers that got generated/dealt
    return:
        bool: True or False based on what is checked by the function
    '''
    
    if hand[0] == hand[1] == hand[2]:
        return True
    else:
        return False


def has_straight(hand: list[int]) -> bool:
    '''
    function:
        has_straight: checks if each element in a list is 1 less than the previous element
    args:
        hand: a list of integers that got generated/dealt
    return:
        bool: True or False based on what is checked by the function
    '''
    if hand[0] - hand[1] == 1:
        if hand[1] - hand[2] == 1:
            return(True)
        else:
            return(False)
    else:
        return(False)
    
def has_pair(hand: list[int]) -> bool:
    '''
    function:
        has_pair: checks if any two of the three elements in the list are equivalent
    args:
        hand: a list of integers that got generated/dealt
    return:
        bool: True or False based on what is checked by the function
    '''
    
    if hand[0] == hand [1]:
        return True
    elif hand[0] == hand[2]:
        return True
    elif hand[1] == hand[2]:
        return True
    else:
        return False
    
def calculate(alist: list[int], value: int) -> int:
    '''
    function: 
        calculate: plugs the elements in the list and the value into an equation
    args:
        hand: a list of integers that got generated/dealt
        value: an integer representing the value of the poker hand
    return:
        int: the value that is calculated by the function
    '''
    return((value * (16 ** 3)) + (alist[0] * (16 ** 2)) + (alist[1] * 16) + alist[2])

def score_hand(hand: list[int]) -> int:
    '''
    function:
        score_hand: scores a list of integers representing a poker hand in terms of poker rules
                    uses the calculate function by putting in the hand and value of the hand as arguments
    args:
        hand: a list of integers that got generated/dealt
    return:
        int: the score of the hand in terms of poker
    '''
    if has_triple(hand):
        value = 16
        return calculate(hand,value)
    elif has_straight(hand):
        value = 15
        return calculate(hand,value)
    elif has_pair(hand):
        if hand[0] - hand[1] == 0 or hand[0] - hand[2] == 0:
            value = hand[0]
            return calculate(hand,value)
        else:
            value = hand[1]
            return calculate(hand,value)
    else:
        value = 0
        return calculate(hand,value)
    
def dealer_plays(hand: list[int]) -> bool:
    '''
    function:
        dealer_plays: checks if the score of the dealer's hand is greater than 3072
    args:
        hand: a list of integers that got generated/dealt
    return: 
        bool: True or False based on the function
    '''
    if score_hand(hand) > 3072:
        return True
    else:
        return False
    
def play_round() -> int:
    '''
    function:
        play_round: deals a hand to the player and asks if they want to play. If so, gives the dealer a hand and 
                    determines if the dealer wants to play. If so, both hands are scored. The player gains or loses
                    points based on which chain of events happen (player folds, dealer folds, dealer higher score, player higher score)
        args:
            (No arguments)
        return:
            int: The amount of points the player gains or loses based on what happened in the round
    '''
    phand = deal()
    print("Your Hand: " + hand_to_string(phand))
    pchoice = get_choice()
    if pchoice == "f":
        return -10
    elif pchoice == "p":
        dhand = deal()
        if dealer_plays(dhand) == False:
            print("Dealer folds")
            return 10
        else:
            print("Dealer Plays")
            print("Dealer Hand: " + hand_to_string(dhand))
            dpoints = score_hand(dhand)
            ppoints = score_hand(phand)
            if dpoints > ppoints:
                print("Dealer wins")
                return -20
            elif ppoints > dpoints:
                print("Player wins")
                return 20
def get_choice():
    answer= ' '
    while answer not in 'pf':
        answer=input("Please enter either 'p' or 'f':")
    return answer

def deal():
    """ Simple random card dealing function """
    return [randint(2, 14), randint(2, 14), randint(2, 14)]

score = 0
Play = True
while Play:
    score += play_round()
    print("Your score is", score)
    cont = ' '
    while cont not in 'qr':
        cont=input("Press 'q' to quit or 'r' to play again: ")
    if cont == 'q':
        Play = False
        print("You ended with a score of", score)
        break
    print("Ok, Your score is", score, "- Starting a new round!")