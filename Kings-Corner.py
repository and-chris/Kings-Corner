# CS1210: HW2
######################################################################
# Complete the signed() function, certifying that:
#  1) the code below is entirely your own work, and
#  2) it has not been shared with anyone outside the intructional team.
#
def signed():
    return(["awchristopher"])

######################################################################
# Import randint and shuffle from random module.
from random import randint, shuffle, sample

######################################################################
# createDeck() produces a new, cannonically ordered, 52 card deck
# using a nested comprehension. Providing a value less than 13
# produces a smaller deck, like the semi-standard 40 card 4 suit 1-10
# deck used in many older card games (including tarot cards). Here,
# we'll use it with default values.
#
def createDeck(N=13, S=('spades', 'hearts', 'clubs', 'diamonds')):
    return([ (v, s) for s in S for v in range(1, N+1) ])

######################################################################
# Construct the representation of a given card using special unicode
# characters for hearts, diamonds, clubs, and spades. The input is a
# legal card, c, which is a (v, s) tuple. The output is a 2 or
# 3-character string 'vs' or 'vvs', where 's' here is the unicode
# character corresponding to the four standard suites (spades, hearts,
# diamonds or clubs -- provided), and v is a 1 or 2 digit string
# corresponding to the integers 2-10 and the special symbols 'A', 'K',
# 'Q', and 'J'.
#
# Example:
#    >>> displayCard((1, 'spades'))
#    'A♠'
#    >>> displayCard((12, 'hearts'))
#    'Q♡'
#
def displayCard(c):
    suits = {'spades':'\u2660', 'hearts':'\u2661', 'diamonds':'\u2662', 'clubs':'\u2663'}
    #Dictionary of facecards
    facecards={1:'A', 11:'J', 12:'Q', 13:'K'}
    card = 0
    suit = 0
    #Loops through everything in c (the card given) and assigns the values to the card and suit using
    #either just the integer or the dictionary (for a face card), and the list of suits for the suit
    for i in c:
        if type(i) == int and i > 1 and i <= 10:
            card = i
        elif type(i) == int and (i < 2 or i > 10):
            card = facecards[i]
        elif type(i) == str:
            suit = suits[i]
    return("{}{}".format(card,suit))
    

######################################################################
# Print out an indexed representation of the state of the table:
# foundation piles are numbered 0-3, corner piles 4-7.
#
# Example:
#   >>> showTable(F, C)
#     F0: 9♡...9♡
#     F1: 2♢...2♢
#     F2: 7♡...7♡
#     F3: 8♡...8♡
#     C4:
#     C5:
#     C6:
#     C7:
# Or, mid-game:
#     F0: 8♣...A♢
#     F1: J♣...J♣
#     F2: A♠...A♠
#     F3: 
#     C4: K♡...K♡
#     C5: 
#     C6: 
#     C7:
#
def showTable(F, C):
    x=0
    y=4
    #Loops through all the lists in F, and prints them out with their respective number
    for lisF in F:
        if lisF == []:
            print("F{}:".format(x))
            x+=1        
        elif x <= 3:
            print("F{}:{}...{}".format(x,displayCard(lisF[0]),displayCard(lisF[len(lisF)-1])))
            x+=1
    #Loops through all the lists in C and prints them out with their respective number
    for lisC in C:
        if lisC == []:
            print("C{}:".format(y))
            y+=1
        elif y <= 7:
            print("C{}:{}...{}".format(y,displayCard(lisC[0]),displayCard(lisC[len(lisC)-1])))
            y+=1
######################################################################
# Print out an indexed list of the cards in input list H, representing
# a hand. Entries are numbered starting at 8 (indexes 0-3 are reserved
# for foundation piles, and 4-7 are reserved for corners). The
# indexing is used to select cards for play.
#
# Example:
#   >>> showHand(H[0])
#   Hand: 8:A♢ 9:4♢ 10:3♡ 11:5♠ 12:6♠ 13:7♠ 14:8♠
#   >>> showHand(H[1])
#   Hand: 8:9♣ 9:5♢ 10:8♢ 11:9♢ 12:10♡ 13:A♠ 14:4♠
#
def showHand(H):
    z=8
    hand = []
    #Loops through all the tuples(cards) in hand and prints them out calling display card
    for q in H:
        hand.append('{}:{}'.format(z,displayCard(q)))
        z+=1
    print("Hand: {}".format(' '.join(hand)))

######################################################################
# We'll use deal(N, D) to set up the game. Given a deck (presumably
# produced by createDeck()), shuffle it, then deal 7 cards to each of
# N players, and seed the foundation piles with 4 additional cards.
# Returns D, H, F, where D is what remains of the deck, H is a list of
# N 7-card "hands", and F is a list of lists corresponding to the four
# "seeded" foundation piles.
# 
# Example:
#   >>> D, H, F = deal(2, D)
#   >>> len(D)
#   34
#   >>> len(H)
#   2
#   >>> H[0][:3]
#   [(5, 'clubs'), (12, 'clubs'), (3, 'diamonds')]
#   >>> F[2]
#   [(11, 'hearts')]
#
def deal(N, D):
    # Shuffle the deck, then return what's left of it after dealing 7
    # cards to each player and seeding the foundation piles.
    D = sample(D, len(D))
    H = []
    y = 0
    #Loops through the amounts of players and gives every player 7 cards
    for i in range(N):
        x=0
        handPlay = []
        #Loops through the deck to give the players 7 cards
        for j in D:
            if x <= 6:
                handPlay.append(j)
                D.remove(j)
                x += 1
        H.append(handPlay)
    F =[]
    #Loops through D to make the 4 foundation piles
    for q in D:
        if y < 4:
            F.append([q])
            D.remove(q)
            y += 1
    return(D,H,F)
    
######################################################################
# Returns True if card c can be appended to stack S. To be legal, c
# must be one less in value than S[-1], and should be of the "other"
# color (red vs black).
#
# Hint: Remember, S might be empty, in which case the answer should
# not be True.
#
# Hint: Use the encapsulated altcolor(c1, c2) helper function to check
# for alternating colors.
#
# Example:
#   >>> legal([(2, 'diamonds')], (1, 'spades'))
#   True
#   >>> legal([(2, 'diamonds')], (1, 'hearts'))
#   False
#
def legal(S, c):
    def altcolor(c1, c2):
        #Makes two lists called red and black, each consisting of the suits that match the name.
        red = ['hearts','diamonds']
        black = ['spades','clubs']
        #Returns True if c1 and c2 are opposite colors
        return (c1 in red and c2 in black) or (c1 in black and c2 in red)
    #Returns True if altcolor returns True(opposite color) and if the last card in the stack is one higher in value than the card
    return (c[0]) == (S[-1][0]-1) and altcolor(S[-1][1],c[1])

######################################################################
# Governs game play for N players (2 by default). This function sets
# up the game variables, D, H, F and C, then chooses the first player
# randomly from the N players. By convention, player 0 is the user,
# while all other player numbers are played by the auto player.
#
# Each turn, the current player draws a card from the deck D, if any
# remain, and then is free to make as many moves as he/she chooses. 
#
# Hint: fill out the remainder of the function, replacing the pass
# statements and respecting the comments.
# 
def play(N=2):
    # Set up the game.
    D, H, F = deal(N, createDeck())
    C = [ [] for i in range(4) ]   # Corners, initially empty.

    # Randomly choose a player to start the game.
    player = randint(0,N-1)    
    print('Player {} moves first.'.format(player))

    # Start the play loop; we'll need to exit explicitly when
    # termination conditions are realized.
    while True:
        # Draw a card if there are any left in the deck.
        if len(D) == 0: #If there are no cards, do nothing
            pass
        else: #Otherwise, add a card from the deck to hand
            H[player].append(D[-1])
            D.remove(D[-1])
        

        print('\n\nPlayer {} ({} cards) to move.'.format(player, len(H[player])))
        print('Deck has {} cards left.'.format(len(D)))

        # Now show the table.
        showTable(F, C)

        # Let the current player have a go.
        if player != 0:
            automove(F, C, H[player])
        else:
            usermove(F, C, H[player])

        # Check to see if player is out; if so, end the game.
        if H[player] == []:
            print('\n\nPlayer {} wins!'.format(player))
            showTable(F, C)
            break

        # Otherwise, go on to next player.
        else:
            if player != min(range(N)): #If there are players with smaller numbers, go down to their turn
                player -= 1
            elif player == min(range(N)): #Otherwise, if the current player is the smallest number(Player 0), then go to the top player(max)
                player = max(range(N))
            

######################################################################
# Prompts a user to play their hand.  See transcript for sample
# operation.
#
def usermove(F, C, hand):
    # valid() is an internal helper function that checks if the index
    # i indicates a valid F, C or hand index.  To be valid, it cannot
    # be an empty pile or an out-of-range hand index. Remember, 0-3
    # are foundation piles, 4-7 are corner piles, and 8 and up index
    # into the hand.
    def valid(i):
        #Returns true if both of th
        if i <= len(hand):
            return True
        else:
            return False

    # Ensure the hand is sorted, integrating newly drawn card.
    hand.sort(key=lambda x: x[0]) #Uses lambda to help sort the hand destructively

    # Give some instruction.
    print('Enter your move as "src dst": press "/" to refresh display; "." when done')

    # Manage any number of moves.
    while True:           # Until the user quits with a .
        # Display current hand.
        showHand(hand)

        # Read inputs and construct a tuple.
        move = []
        while not move or not valid(move[0]) or not valid(move[1]):
            move = input("Your move? ").split()
            if len(move) == 1:
                if move[0] == '.':

                    return True    #Starts loops over, next player goes

                elif move[0] == '/':

                    showTable(F,C)    #Shows table and hand again
                    break
            try:
                move = [int(move[0]), int(move[1])]
                # Execute the command, which looks like [from, to].
                # Remember, 0-3 are foundations, 4-7 are corners, 8+
                # are from your hand.
                #
                # What follows here is an if/elif/else statement for
                # each of the following cases.

                # Playing a card from your hand to a foundation pile.
                if (move[1] <= 3 and move[1] >= 0) and move[0] >= 8: 
                    if F[move[1]] == []:
                        F[move[1]].append(hand[move[0]-8])
                        hand.remove(hand[move[0]-8])
                    elif legal(F[move[1]],hand[move[0]-8]):    
                        F[move[1]].append(hand[move[0]-8])
                        hand.remove(hand[move[0]-8])
                    else: 
                        print("Illegal move")

                # Moving a foundation pile to a foundation pile.
                elif move[1] in range(0,4) and move[0] in range(0,4) and legal(F[move[1]], F[move[0]][0]):
                    for i in range(len(F[move[0]])):       #Loops through everythiing in the foundation pile that is being moved, and appends it
                        F[move[1]].append(F[move[0]][i])   #to the foundation pile it is going to, then clears the moved foundation pile
                        i = 0
                    F[move[0]].clear()            

                # Playing a card from your hand to a corner pile (K only to empty pile).
                elif move[1] in range(4,8) and move[0] not in range(0,4):
                    if hand[move[0]-8][0] == 13 and C[move[1]-4] == []:
                        C[move[1]-4].append(hand[move[0]-8])
                        hand.remove(hand[move[0]-8]) 
                    elif legal(C[move[1]-4], hand[move[0]-8]):
                        C[move[1]-4].append(hand[move[0]-8])
                        hand.remove(hand[move[0]-8])
                    else:
                        print("Illegal move")

                # Moving a foundation pile to a corner pile. 
                elif move[0] in range(0,4) and move[1] in range(4, 8):
                    if F[move[0]][0][0] == 13 and C[move[1]-4] == []:
                        for i in range(len(F[move[0]])):       #Loops through the range of F, and appends it to C if the bottom card is a King
                            C[move[1]-4].append(F[move[0]][i]) 
                            i = 0
                    elif legal(C[move[1]-4], F[move[0]][0]):
                        for i in range(len(F[move[0]])):       #Loops through the range of F, and appends it to C if it is a legal move
                            C[move[1]-4].append(F[move[0]][i])
                            i = 0
                    else:
                        print("Illegal move")
                    F[move[0]].clear() #Clears the foundation pile at the end                     

                # Otherwise, print "Illegal move" warning.
                else:
                    print("Illegal move")
                    

            except:
                # Any failure to process ends up here.
                print('Ill-formed move {}'.format(move))

            # If the hand is empty, return. Otherwise, reset move and
            # keep trying.
            if not hand:
                return
            move = []

######################################################################
# Plays a hand automatically using a fixed but not particularly
# brilliant strategy. The strategy involves consolidating the table
# (to collapse foundation and corner piles), then scanning cards in
# your hand from highest to lowest, trying to place each card. The
# process is repeated until no card can be placed. See transcript for
# an example.
#
def automove(F, C, hand):
    # Keep playing cards while you're able to move something.
    moved = True
    while moved:
        moved = False	# Change back to True if you move a card.
        # Start by consolidating the table.
        consolidate(F, C)

        # Sort the hand (destructively) so that you consider highest
        # value cards first.
        hand.sort(key=lambda x: x[0], reverse=True)

        # Scan cards in hand from high to low value, which makes removing
        # elements easier.
        for i in range(len(hand)-1, -1, -1):
            # If current card is a king, place in an empty corner
            # location (guaranteed to be one).

            if i < len(hand) and hand[i][0] == 13:
                for x in range(len(C)):   #Loops through all the corner piles, and appends it to the first empty one
                    if C[x] == [] and hand[i][0] == 13:
                        C[x].append(hand[i])
                        hand.remove(hand[i])
                        moved = True

            # Otherwise, try to place current card on an existing
            # corner or foundation pile.
            for j in range(4):
                # Here, you have an if/elif/else that checks each of
                # the stated conditions.

                # Place current card on corner pile.
                if C[j] != [] and i < len(hand) and legal(C[j],hand[i]):
                    C[j].append(hand[i])
                    hand.remove(hand[i])
                    moved = True

                # Place current card on foundation pile.
                elif F[j] != [] and i < len(hand) and legal(F[j], hand[i]):
                    F[j].append(hand[i])
                    hand.remove(hand[i])
                    moved = True

                # Start a new foundation pile.
                elif F[j] == []:
                    F[j].append(hand[0])
                    hand.remove(hand[0])
                    moved = True
                    

######################################################################
# consolidate(F, C) looks for opportunities to consolidate by moving a
# foundation pile to a corner pile or onto another foundation pile. It
# is used by the auto player to consolidate elements on the table to
# make it more playable.
#
# Example:
#   >>> showTable(F, C)
#     F0: 6♢...6♢
#     F1: 10♣...10♣
#     F2: J♡...J♡
#     F3: Q♠...Q♠
#     C4: K♢...K♢
#     C5:
#     C6:
#     C7:
#   >>> consolidate(F, C)
#   >>> showTable(F, C)
#     F0: 6♢...6♢
#     F1:
#     F2: 
#     F3: 
#     C4: K♢...10♣
#     C5:
#     C6:
#     C7:
#
def consolidate(F, C):
    # Consider moving one foundation onto another.
    for i in range(4):
        for j in range(4):
            if F[j] != [] and F[i] != [] and legal(F[i], F[j][0]):
                for x in F[j]:  #Comprehension that appends everything in one foundation pile onto another
                    F[i].append(x)
                F[j].clear()

    # Consider moving a foundation onto a corner.
    for q in range(4): #Loops through 4 times (one for every foundation pile)
        for z in range(4): #Loops through 4 times (one for every corner pile)
            if F[q] != [] and C[z] == [] and F[q][0][0] == 13:
                for x in range(len(F[q])):  #
                    C[z].append(F[q][x])   
                F[q].clear()
            elif C[q] != [] and F[z] != [] and legal(C[q], F[z][0]): 
                for y in F[z]: #
                    C[q].append(y)
                F[z].clear()
######################################################################
if __name__ == '__main__':
    # Play two-player version by default.
    play(2)
