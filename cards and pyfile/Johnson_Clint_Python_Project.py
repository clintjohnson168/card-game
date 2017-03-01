# Clint Johnson
# Python Project
# Higer or Lower

'''
 Psudo code
 create players class
  Atributes of hand, player name, turn, numberCorrect, frozen number
  whosTurn function
   display coin toss screen
   have player one call the coin
   have heads and tails button call event functions according to coin toss
  startTurn function
   Display current numberCorrect cards in hand
   Change card buttion
    Generate new rand card
    call turn
   Leave card button
    Call turn
  Turn function
   Create buttions higher, lower
   higher button
    if higher call continueTurn
    if lower call notCorrect
   Lower button
    if lower call continueTurn
    if higher call notCorrect
  notCorrect function
   display screen saying the guess is incorrect
  continueTurn function
   display screen, ask continue or freeze turn
   continue button
    call turn
   freeze button
    set frozenNumber to numberCorrect
  winScreen function
   display screen saying current player has won
  introToGame function
   display screen asking if players would like to see instructions
   yes button
    display instructions
   no button
    call whos turn
'''

import pygame, sys, random
from pygame.locals import *
from PlayingCards import *

class Player:
    'This is the Players Class'
    def __init__(self, name = "NA", num_of_cards = 5):
        'Initialzes player and name'
        self.myHand = []
        for i in range(num_of_cards):
            a = Card.randCard()
            self.myHand.append(a)
        self.myName = name
        self.Turn = True
        self.numberCorrect = 1
        self.frozen = 1

    def whosTurn(self, other):
        'Desides who goes fist with coin toss, returns True for user and False otherwise'
        # display who goes first screen
        # display window
        size = 700,500
        gray = 128,128,128
        black = 0,0,0
        blue = 0,0,255
        red = 255,0,0
        screen = pygame.display.set_mode(size)
        screen.fill(gray)
        #add text
        pygame.display.set_caption("Who Goes First")
        myfont = pygame.font.init()
        myfont = pygame.font.SysFont("Camic Sans MS", 30)
        label = myfont.render("Player 1, Heads or Tails?", True, black)
        screen.blit(label, (100,100))
        pygame.display.flip()
        # add buttons
        heads = pygame.draw.rect(screen, red, (100,300,75,50))
        heads_label = myfont.render("Heads", True, black)
        screen.blit(heads_label, (106,318))
        tails = pygame.draw.rect(screen, red, (300, 300, 75, 50))
        tails_label = myfont.render("Tails", True, black)
        screen.blit(tails_label, (308,318))
        # update window
        pygame.display.update()        
        # mouse click event
        guess = 0
        while True:
            event = pygame.event.poll()
            if (event.type == pygame.MOUSEBUTTONDOWN and heads.collidepoint(pygame.mouse.get_pos())):
                guess = 1
                break
            if (event.type == pygame.MOUSEBUTTONDOWN and tails.collidepoint(pygame.mouse.get_pos())):
                guess = 2
                break            
        # generate answer screen
        answer_screen = pygame.display.set_mode(size)
        answer_screen.fill(gray)
        
        #generate a coin
        coin = random.randint(1,2) #1=heads, 2=tails
        if(guess == coin):
            pygame.display.set_caption("Answer")
            a = pygame.font.init()
            a = pygame.font.SysFont("Camic Sans MS", 30)
            b  = a.render("You called it right!", True, black)
            answer_screen.blit(b, (100,100))
            pygame.display.flip()            
            pygame.display.update()
            pygame.time.wait(2000)
            return True
        else:
            pygame.display.set_caption("Answer")
            a = pygame.font.init()
            a = pygame.font.SysFont("Camic Sans MS", 30)
            b  = a.render("You called it wrong!", True, black)
            answer_screen.blit(b, (100,100))
            pygame.display.flip()            
            pygame.display.update()
            pygame.time.wait(2000)
            return False
        
    def startTurn(self):
        'shows start screen and decides who goes first'
        'will display answer screen for 2 seconds'
        # display window
        size = 700,500
        gray = 128,128,128
        green = 0,255,0
        black = 0,0,0
        red = 255,0,0
        blue = 0,0,255
        screen = pygame.display.set_mode(size)
        screen.fill(gray)
        pygame.display.update()
        #add text
        pygame.display.set_caption(self.getName()+ "'s Turn")
        myfont = pygame.font.init()
        myfont = pygame.font.SysFont("Camic Sans MS", 24)
        label = myfont.render(self.getName() + ", would you like to change your card?", True, black)
        screen.blit(label, (10,10))
        # add buttons
        sprites = pygame.sprite.Sprite()
        yes = pygame.draw.rect(screen, red, (100,400,75,50))
        yes_label = myfont.render("Yes", True, black)
        screen.blit(yes_label, (109,418))
        no = pygame.draw.rect(screen, red, (300, 400, 75, 50))
        no_label = myfont.render("No", True, black)
        screen.blit(no_label, (311,418))
        pygame.display.update()
        
        self.setNumberCorrect(self.frozen)
        # create and get cards in hand
        for i in range(self.numberCorrect):
            card = self.getHand()[i]
            print_card = pygame.image.load(card.getName() + '.png')
            screen.blit(print_card, ((50*(i+1)),100))
        pygame.display.update()
        # mouse click event
        while True:
            event = pygame.event.poll()
            if (event.type == pygame.MOUSEBUTTONDOWN and yes.collidepoint(pygame.mouse.get_pos())):
                new_card = Card.randCard()
                self.setHand(self.numberCorrect - 1, new_card)
                print_card = pygame.image.load(card.getName() + ".png")
                screen.blit(print_card, ((50*(self.numberCorrect+1)), 100))
                pygame.display.update()
                self.turn()                
                break
            if (event.type == pygame.MOUSEBUTTONDOWN and no.collidepoint(pygame.mouse.get_pos())):
                self.turn()
                break

    def turn(self):
        'This initializes the events in the turn'
        # display window
        size = 700,500
        gray = 128,128,128
        green = 0,255,0
        black = 0,0,0
        blue = 0,0,255
        red = 255,0,0
        screen = pygame.display.set_mode(size)
        screen.fill(gray)
        #add text
        pygame.display.set_caption(self.getName()+ "'s Turn")
        myfont = pygame.font.init()
        myfont = pygame.font.SysFont("Camic Sans MS", 24)
        label = myfont.render(self.getName() + ". Is the next card higher or lower?", True, black)
        screen.blit(label, (10,10))
        # add buttons
        sprites = pygame.sprite.Sprite()
        higher = pygame.draw.rect(screen, red, (100,400,75,50))
        higher_label = myfont.render("Higher", True, black)
        screen.blit(higher_label, (109,418))
        lower = pygame.draw.rect(screen, red, (300, 400, 75, 50))
        lower_label = myfont.render("Lower", True, black)
        screen.blit(lower_label, (311,418))
        # display numberCorrect amount of cards 
        for i in range(self.numberCorrect):
            card = self.getHand()[i]
            print_card = pygame.image.load(card.getName() + '.png')
            screen.blit(print_card, ((50*(i+1)),100))
        pygame.display.update()
        if(self.numberCorrect == 5):
            self.winScreen()
        # mouse click event
        while True:
            event = pygame.event.poll()
            if (event.type == pygame.MOUSEBUTTONDOWN and higher.collidepoint(pygame.mouse.get_pos())):
                # if next card is higer than current card
                next_card = self.getHand()[self.numberCorrect]
                if(card.getRank() < next_card.getRank()):
                    self.continueTurn()
                    break
                #else end player's turn
                else:
                    self.notCorrect()
                    new_card = Card.randCard()
                    self.setHand(self.numberCorrect, new_card)
                    break
                    
            if (event.type == pygame.MOUSEBUTTONDOWN and lower.collidepoint(pygame.mouse.get_pos())):
                # if next card is lower than current card
                next_card = self.getHand()[self.numberCorrect]
                if(card.getRank() > next_card.getRank()):
                    self.continueTurn()
                    break
                #else end player's turn
                else:
                    self.notCorrect()
                    new_card = Card.randCard()
                    self.setHand(self.numberCorrect, new_card)
                    break
                    

    def continueTurn(self):
        'asks player if they want to feeze or continue'
        # display window
        size = 700,500
        gray = 128,128,128
        green = 0,255,0
        black = 0,0,0
        blue = 0,0,255
        red = 255,0,0
        screen = pygame.display.set_mode(size)
        screen.fill(gray)
        #add text
        pygame.display.set_caption(self.getName()+ "'s Turn")
        myfont = pygame.font.init()
        myfont = pygame.font.SysFont("Camic Sans MS", 24)
        label = myfont.render(self.getName() + ", would you like to freeze or continue?", True, black)
        screen.blit(label, (10,10))
        # add buttons
        freeze = pygame.draw.rect(screen, red, (100,400,75,50))
        freeze_label = myfont.render("Freeze", True, black)
        screen.blit(freeze_label, (109,418))
        cont = pygame.draw.rect(screen, red, (300, 400, 95, 50))
        cont_label = myfont.render("Continue", True, black)
        screen.blit(cont_label, (311,418))
        pygame.display.update()
        #display correct cards in hand
        self.setNumberCorrect(self.numberCorrect+1)
        for i in range(self.numberCorrect):            
            card = self.getHand()[i]
            print_card = pygame.image.load(card.getName() + '.png')
            screen.blit(print_card, ((50*(i+1)),100))
        pygame.display.update()
        # mouse click event
        while True:
            event = pygame.event.poll()
            if (event.type == pygame.MOUSEBUTTONDOWN and freeze.collidepoint(pygame.mouse.get_pos())):
                #update numberCorrect and frozen
                self.setNumberFrozen(self.numberCorrect)
                #end turn
                break
            if (event.type == pygame.MOUSEBUTTONDOWN and cont.collidepoint(pygame.mouse.get_pos())):
                self.turn()
                break

    def notCorrect(self):
        'displays incorrect window for 2 seconds'
        # display window
        size = 700,500
        gray = 128,128,128
        black = 0,0,0
        blue = 0,0,255
        red = 255,0,0
        screen = pygame.display.set_mode(size)
        screen.fill(gray)
        #add text
        pygame.display.set_caption("Answer")
        myfont = pygame.font.init()
        myfont = pygame.font.SysFont("Camic Sans MS", 50)
        label = myfont.render("Sorry that is incorrect!", True, black)
        screen.blit(label, (100,100))
        pygame.display.update()
        pygame.time.wait(2000)
        i = self.frozen
        for i in range(self.numberCorrect):
            card = Card.randCard()
            self.setHand(i, card)
        return

    def winScreen(self):
        # display window
        size = 700,500
        gray = 128,128,128
        black = 0,0,0
        blue = 0,0,255
        screen = pygame.display.set_mode(size)
        screen.fill(gray)
        #add text
        pygame.display.set_caption("Win")
        myfont = pygame.font.init()
        myfont = pygame.font.SysFont("Camic Sans MS", 40)
        label = myfont.render("Congratulations " + self.getName() + " you win!!!", True, black)
        screen.blit(label, (100,100))
        pygame.display.update()
        pygame.time.wait(5000)
        pygame.display.quit()
        sys.exit()
        
    def introToGame(self):
        # display window
        size = 700,500
        gray = 128,128,128
        black = 0,0,0
        blue = 0,0,255
        red = 255,0,0
        screen = pygame.display.set_mode(size)
        screen.fill(gray)
        #add text
        pygame.display.set_caption("Instruction Screen")
        myfont = pygame.font.init()
        myfont = pygame.font.SysFont("Camic Sans MS", 30)
        label = myfont.render("This game is like the TV game show 'Cark Sharks'", True, black)
        screen.blit(label, (100,100))
        label_2 = myfont.render("Would you like to read the instructions?", True, black)
        screen.blit(label_2, (100,150))
        pygame.display.flip()
        # add buttons
        sprites = pygame.sprite.Sprite()
        yes = pygame.draw.rect(screen, red, (100,300,75,50))
        yes_label = myfont.render("Yes", True, black)
        screen.blit(yes_label, (106,318))
        no = pygame.draw.rect(screen, red, (300, 300, 75, 50))
        no_label = myfont.render("No", True, black)
        screen.blit(no_label, (308,318))
        # update window
        pygame.display.update()
        
        # mouse click event
        guess = 0
        while True:
            event = pygame.event.poll()
            if (event.type == pygame.MOUSEBUTTONDOWN and yes.collidepoint(pygame.mouse.get_pos())):
                self.instructionScreen()
                break
            if (event.type == pygame.MOUSEBUTTONDOWN and no.collidepoint(pygame.mouse.get_pos())):
                break

    def instructionScreen(self):
        # display window
        size = 700,500
        gray = 128,128,128
        black = 0,0,0
        blue = 0,0,255
        red = 255,0,0
        screen = pygame.display.set_mode(size)
        screen.fill(gray)
        #add text
        pygame.display.set_caption("Instruction Screen")
        myfont = pygame.font.init()
        myfont = pygame.font.SysFont("Camic Sans MS", 24)
        label_1 = myfont.render("This a game of the basic higher lower concept", True, black)
        screen.blit(label_1, (50,50))
        label_2 = myfont.render("This is a two person game, and who goes first will be decided by a coin toss", True, black)
        screen.blit(label_2, (50,75))
        l3 = myfont.render("During the Players turn he or she will be:", True, black)
        screen.blit(l3, (50,100))
        l4 = myfont.render("1) Asked if he or she wants to change their active card", True, black)
        screen.blit(l4, (60,125))
        l5 = myfont.render("2) Asked if his or her card is higher or lower than current", True, black)
        screen.blit(l5, (60,150))
        l6 = myfont.render("3) Asked if he or she would like to continue their turn or freeze on current card", True, black)
        screen.blit(l6, (60,175))
        l7 = myfont.render("The first player that has 5 correct cards displayed will be the winner", True, black)
        screen.blit(l7, (50, 200))        
        pygame.display.flip()
        # add buttons
        sprites = pygame.sprite.Sprite()
        next_1 = pygame.draw.rect(screen, red, (100,300,75,50))
        next_label = myfont.render("Next", True, black)
        screen.blit(next_label, (106,318))
        # update window
        pygame.display.update()
        
        # mouse click event
        guess = 0
        while True:
            event = pygame.event.poll()
            if (event.type == pygame.MOUSEBUTTONDOWN and next_1.collidepoint(pygame.mouse.get_pos())):
                break
            
    def getName(self):
        'returns name'
        return self.myName
    def getIsTurn(self):
        'returns true if it is still players turn, false otherwise'
        return self.Turn
    def getHand(self):
        'return a list of card is players hand'
        return self.myHand
    def setHand(self, pos, card):
        'set replaces the card at pos to the given card'
        self.myHand[pos] = card
    def appedHand(self):
        a = Card.randCard()
        myHand.append(a)
    def getNewCard(self, current):
        'gets a new randowm card and replaces current card in list'
        card = Card.randCard()
        self.myHand.remove(current)
        self.myHand.insert(card, current)
    def getNumberCorrect(self):
        'returns the number of correct quessed cards'
        return self.numberCorrect
    def setNumberCorrect(self, value):
        'set the value of correct cards'
        self.numberCorrect = value
    def getNumberFrozen(self):
        'return number Frozen'
        return self.frozen
    def setNumberFrozen(self, value):
        'sets numberForzen = value'
        self.frozen = value
    
def main():
    'Allows the game to start exicuting'
    # generate game screen
    pygame.init()
    size = width, height = 700, 500
    green = 0,255,0

    screen = pygame.display.set_mode(size)

    #**************************************************

    #**************************************************
    # generate players
    p1 = Player('Player 1')
    p2 = Player('Player 2')
    p1.introToGame()
    # while not the end of the game
    while True:
        for event in pygame.event.get():
            while(event.type != pygame.QUIT):
                turn = p1.whosTurn(p2)
                if(turn == True):
                     p1.startTurn()
                else:
                     p2.startTurn()
main()
