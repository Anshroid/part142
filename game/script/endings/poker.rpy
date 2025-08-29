default eatingUnlocked = False

init python:
    import random


    class Dealer:
        def __init__(self, players, chips, smallBlind):
            self.mPlayers = players
            self.mNumPlayers = len(players)
            self.mSBlind = smallBlind
            self.mButton = 0
            self.mDeck = []

            for i in range(1, 14):
                for j in range(0, 4):
                    self.mDeck.append((i, j))

        def isBettingOver(self, checks):
            bettingOver = True

            for i in range(self.mNumPlayers):
                if self.alivePlayers[i]:
                    bettingOver = bettingOver and checks[i]

            return bettingOver

        def checkVal(self, currPerson):
            return max(self.contributions) - self.contributions[currPerson]

        def numAlive(self):
            num = 0
            for i in self.alivePlayers:
                if i:
                    num += 1
            return num

        def betting(self, lastBet=0):
            currPerson = (self.mButton + 1) % self.mNumPlayers
            checks = []

            for i in range(self.mNumPlayers):
                checks.append(False)

            while not self.isBettingOver(checks):
                if self.alivePlayers[currPerson]:                    
                    checkVal = self.checkVal(currPerson)

                    renpy.show_screen('poker_ui', self.pot, self.mPlayers[1].chips, self.mPlayers[0].chips, checkVal)
                    renpy.with_statement(trans=Dissolve(0.25))

                    if self.numAlive() == 1:
                        playerDecision = (1, 0)
                    else:
                        playerDecision = self.mPlayers[currPerson].getAction(
                            self.communityCards, self.playerCards[currPerson], checkVal, self.pot)

                    #if currPerson == 0:
                    #    renpy.say(C, str(playerDecision))

                    match playerDecision[0]:
                        case 0:
                            self.alivePlayers[currPerson] = False
                            if playerDecision[1] == -1:
                                self.playerCards[currPerson] = []
                        case 1:
                            checks[currPerson] = True
                            self.contributions[currPerson] += checkVal
                            self.mPlayers[currPerson].changeChips(-checkVal)
                            self.pot += checkVal
                        case 2:
                            for i in range(len(checks)):
                                checks[i] = False
                            checks[currPerson] = True
                            self.contributions[currPerson] += checkVal + \
                                playerDecision[1]
                            self.mPlayers[currPerson].changeChips(
                                -checkVal - playerDecision[1])
                            self.pot += checkVal + playerDecision[1]

                    renpy.show_screen('poker_ui', self.pot, self.mPlayers[1].chips, self.mPlayers[0].chips, checkVal)
                    renpy.with_statement(trans=Dissolve(0.25))

                currPerson = (currPerson + 1) % self.mNumPlayers

        def dealCards(self):
            random.shuffle(self.mDeck)

            for i in range(self.mNumPlayers):
                # if i == 1:
                #    self.playerCards.append([(1, 3), (2, 3), (3, 3), (4, 3), (5, 3)])
                #else:
                
                self.playerCards.append([])
                self.playerCards[i].append(tmp := self.mDeck.pop())
                if i == 1:
                    renpy.show(cardName(tmp), at_list=[hand1])
                    renpy.with_statement(trans=Dissolve(0.5))

                self.playerCards[i].append(tmp := self.mDeck.pop())
                if i == 1:
                    renpy.show(cardName(tmp), at_list=[hand2])
                    renpy.with_statement(trans=Dissolve(0.5))

        def flush(self, hand):
            counts = [0, 0, 0, 0]
            for i in hand:
                counts[i[1]] += 1

            return max(counts) >= 5

        def straight(self, hand):
            for card in hand:
                for i in range(4):
                    failure = False
                    for nextCard in hand:
                        if nextCard[0] == card[0] + i + 1 or (nextCard[0] + 13 == card[0] + i + 1 and i == 3):
                            continue
                        else:
                            failure = True

                    if failure:
                        break
                    if i == 3:
                        return True
            return False

        def straightFlush(self, hand):
            counts = [[], [], [], []]
            for i in hand:
                counts[i[1]].append(i)

            for i in range(4):
                if self.straight(counts[i]):
                    return True
            return False

        def subCounts(self, hand):
            counts = []
            for i in range(13):
                counts.append(0)

            for card in hand:
                counts[card[0] - 1] += 1

            return counts

        def subCards(self, hand):
            counts = []
            for i in range(13):
                counts.append([])

            for card in hand:
                counts[card[0] - 1].append(card)
            return counts

        def fourKind(self, hand):
            counts = self.subCounts(hand)
            return max(counts) == 4

        def fullHouse(self, hand):
            counts = self.subCounts(hand)
            return 3 in counts and 2 in counts

        def threeKind(self, hand):
            counts = self.subCounts(hand)
            return 3 in counts

        def twoPair(self, hand):
            counts = self.subCounts(hand)
            return counts.count(2) >= 2

        def pair(self, hand):
            counts = self.subCounts(hand)
            return 2 in counts

        def determineCategory(self, hand):
            if self.straightFlush(hand):
                return 0
            if self.fourKind(hand):
                return 1
            if self.fullHouse(hand):
                return 2
            if self.flush(hand):
                return 3
            if self.straight(hand):
                return 4
            if self.threeKind(hand):
                return 5
            if self.twoPair(hand):
                return 6
            if self.pair(hand):
                return 7
            return 8

        def helperDraw(self, cards):
            return max(cards, key=lambda x: 14 if x[0] == 1 else x[0])

        def determineWinners(self, highestCards, playerIndices):
            max = -1
            winners = []
            for i in range(len(highestCards)):
                if highestCards[i][0] > max:
                    max = highestCards[i][0]
                    winners = [playerIndices[i]]
                if highestCards[i][0] == max:
                    winners.append(playerIndices[i])
            return winners

        # ABSOLUTE HELL. I HATED EVERY MINUTE MAKING THIS FUNCTION. THIS FUNCTION TOOK MORE TIME THAN EVERYTHING ELSE
        # THIS function can kill itself
        # TECHNICALLY doesn't even have full functionality just because I cannot be bothered
        def settleDraw(self, players, category):
            if category == 0 or category == 4:
                highestCards = []

                for player in players:
                    hand = sorted(player[1], reverse=True,
                                  key=lambda x: 14 if x[0] == 1 else x[0])
                    for card in hand:
                        for i in range(4):
                            failure = False
                            for nextCard in hand:
                                if nextCard[0] == card[0] + i + 1 or (nextCard[0] + 13 == card[0] + i + 1 and i == 3):
                                    continue
                                else:
                                    failure = True

                            if failure:
                                break
                            if i == 3:
                                highestCards.append(card[0] + i + 1)

                return self.determineWinners(highestCards, [i[0] for i in players])

            if category == 1:
                highestCards = []
                for player in players:
                    cardCategories = self.subCards(player[1])
                    for i in range(13):
                        if len(cardCategories[i]) == 4:
                            highestCards.append(self.helperDraw(cardCategories[i]))

                return self.determineWinners(highestCards, [i[0] for i in players])

            if category == 2 or category == 5:
                highestCards = []
                for player in players:
                    cardCategories = self.subCards(player[1])
                    for i in range(13):
                        if len(cardCategories[i]) == 3:
                            highestCards.append(self.helperDraw(cardCategories[i]))
                return self.determineWinners(highestCards, [i[0] for i in players])

            if category == 3:
                highestCards = []
                for player in players:
                    cardCategories = [[], [], [], []]
                    for card in player[1]:
                        cardCategories[card[1]].append(card)
                    for i in cardCategories:
                        if len(i) == 4:
                            highestCards.append(self.helperDraw(i))
                return self.determineWinners(highestCards, [i[0] for i in players])

            if category == 6 or category == 7:
                highestCards = []
                for player in players:
                    cardCategories = self.subCards(player[1])
                    for i in range(13):
                        if len(cardCategories[i]) == 2:
                            highestCards.append(self.helperDraw(cardCategories[i]))
                return self.determineWinners(highestCards, [i[0] for i in players])

            if category == 8:
                highestCards = []
                for player in players:
                    highestCards.append(self.helperDraw(player[1]))

                return self.determineWinners(highestCards, [i[0] for i in players])

        def evalWinner(self):
            categories = []
            for i in range(9):
                categories.append([])

            for i in range(self.mNumPlayers):
                if self.alivePlayers[i]:
                    availableCards = self.playerCards[i] + self.communityCards
                    categories[self.determineCategory(availableCards)].append(
                        (i, availableCards))

            for i in range(9):
                if categories[i] != []:
                    if len(categories[i]) == 1:
                        return [categories[i][0]]
                    return self.settleDraw(categories[i], i)

        def playRound(self):
            if len(self.mDeck) < 9:
                renpy.say(C,"HOW MANY CARDS DID YOU EAT.")
                renpy.say(C,"We can't even play anymore. THERE'S NOT ENOUGH CARDS!")
                return False
            self.pot = 0
            self.alivePlayers = []
            self.contributions = []
            self.playerCards = []
            self.communityCards = []

            for i in range(self.mNumPlayers):
                self.alivePlayers.append(True)
                self.contributions.append(0)

            self.dealCards()

            self.mPlayers[self.mButton].changeChips(-self.mSBlind * 2)
            self.contributions[self.mButton] += self.mSBlind * 2
            self.mPlayers[self.mButton-1].changeChips(-self.mSBlind)
            self.contributions[self.mButton-1] += self.mSBlind

            self.pot += self.mSBlind * 3

            self.betting(lastBet=self.mSBlind)

            self.communityCards.append(tmp := self.mDeck.pop())
            renpy.show(cardName(tmp), at_list=[card1])
            renpy.with_statement(trans=Dissolve(0.5))

            self.communityCards.append(tmp := self.mDeck.pop())
            renpy.show(cardName(tmp), at_list=[card2])
            renpy.with_statement(trans=Dissolve(0.5))

            self.communityCards.append(tmp := self.mDeck.pop())
            renpy.show(cardName(tmp), at_list=[card3])
            renpy.with_statement(trans=Dissolve(0.5))
            self.betting()

            self.communityCards.append(tmp := self.mDeck.pop())
            renpy.show(cardName(tmp), at_list=[card4])
            renpy.with_statement(trans=Dissolve(0.5))
            self.betting()

            self.communityCards.append(tmp := self.mDeck.pop())
            renpy.show(cardName(tmp), at_list=[card5])
            renpy.with_statement(trans=Dissolve(0.5))
            self.betting()

            winners = self.evalWinner()

            for winner in winners:
                self.mPlayers[winner[0]].changeChips(self.pot//len(winners))

            renpy.show(cardName(self.playerCards[0][0]), at_list=[cyno1])
            renpy.show(cardName(self.playerCards[0][1]), at_list=[cyno2])
            renpy.with_statement(trans=Dissolve(0.5))

            renpy.say("Dealer", f"{'Cyno' if winner[0] == 0 else 'You'} won!")

            self.mDeck += self.communityCards
            for hand in self.playerCards:
                self.mDeck += hand

            self.mButton = (self.mButton + 1) % self.mNumPlayers

            for player in self.mPlayers:
                if player.chips <= self.mSBlind * 2:
                    return False
            return True


    class Player:
        def __init__(self, chips):
            self.chips = chips

        def changeChips(self, val):
            self.chips += val

        def getAction(self, communityCards, myCards, checkVal, pot):
            # (0,0) is fold normally, (0,-1) is to fold and eat hand
            # (1,0) is to check
            # (2,amount) is to raise by amount

            return (1, 0)

    class AIPlayer(Player):
        def getAction(self, communityCards, myCards, checkVal, pot):
            action = (random.randint(0, 2), 0)
            if action[0] == 0:
                renpy.say(C, "I fold...")

            if action[0] == 1:
                renpy.say(C, "I'll just check then.")

            if action[0] == 2:
                #raise = renpy.random.randint(0, self.chips)
                if self.chips >= 1:
                    action = (2, renpy.random.randint(0,self.chips))
                    renpy.say(C,f"I raise {action[1]}!")
                else:
                    action = (1,0)
                    renpy.say(C,"I fold...")
                
            return action

    class UserPlayer(Player):
        def getAction(self, communityCards, myCards, checkVal, pot):
            action = renpy.display_menu(items=[
                ('Fold', (0, 0)),
                ('Check', (1, 0)),
                ('Raise', (2, 0))
            ] + ([('Eat your cards', (0, -1)),] if random.random() > 0.92 or store.eatingUnlocked else []), interact=True, screen='choice')

            if action[1] == -1:
                renpy.music.play("sfx/eating.mp3", channel="sound")
                renpy.hide(cardName(myCards[0]))
                renpy.with_statement(trans=Dissolve(0.25))
                renpy.hide(cardName(myCards[1]))
                renpy.with_statement(trans=Dissolve(0.25))


            if action[0] == 2:
                action = (2, int(renpy.input(f"Raise how much?", allow="1234567890")))

                while action[1] > self.chips:
                    renpy.say(None, ">> You don't have enough chips for that!")
                    action = (2, int(renpy.input(f"Raise how much?", allow="1234567890")))

            if action[0] == 2:
                action = (2, int(renpy.input(f"Raise how much? You have {self.chips}")))

            if action[1] == 42:
                store.eatingUnlocked = True

            return action

    def cardName(card):
        if card[0] > 10:
            rank = ["jack", "queen", "king"][card[0] - 11]
        elif card[0] == 1:
            rank = "ace"
        else:
            rank = str(card[0])

        suit = ["spades", "hearts", "clubs", "diamonds"][card[1]]

        return f"{rank}_of_{suit}"

transform card1:
    zoom 0.5
    xalign 0.1
    yalign 0.4
    rotate -1.0

transform card2:
    zoom 0.5
    xalign 0.3
    yalign 0.4
    rotate 0.2

transform card3:
    zoom 0.5
    xalign 0.5
    yalign 0.4
    rotate -1.0

transform card4:
    zoom 0.5
    xalign 0.7
    yalign 0.4
    rotate -0.5

transform card5:
    zoom 0.5
    xalign 0.9
    yalign 0.4
    rotate 0.8

transform hand1:
    zoom 0.55
    xalign 0.46
    yalign 1.33
    rotate -2.0

transform hand2:
    zoom 0.55
    xalign 0.58
    yalign 1.3
    rotate 3.0

transform cyno1:
    zoom 0.4
    xalign 0.42
    yalign 0.0
    rotate 2.0

transform cyno2:
    zoom 0.4
    xalign 0.54
    yalign 0.0
    rotate -3.0

label poker:
    scene poker
    show screen poker_ui("", "", "", "")
    with fade

    $ dealer = Dealer([AIPlayer(200), UserPlayer(200)], 0, 5)

label round:
    scene poker with dissolve

    if not dealer.playRound():
        show screen poker_ui(0, dealer.mPlayers[1].chips, dealer.mPlayers[0].chips, 0)

        ">> The game ended..."

        return

    show screen poker_ui(0, dealer.mPlayers[1].chips, dealer.mPlayers[0].chips, 0)    

    menu:
        ">> Would you like to play another round?"

        "ya":
            jump round

        "na":
            return