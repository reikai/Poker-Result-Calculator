# -*- coding: utf-8 -*-
"""
Created on Sat Oct 8 12:50:57 2022

@author: TyTip
"""

from itertools import count


class Player:
    def __init__(self, name, buyin, cashout, gameresult):
        self.name = name
        self.buyin = buyin
        self.cashout = cashout
        self.gameresult = gameresult
    
    def __str__(self):
        return f"{self.name}(Buyin: {self.buyin})"
    
    def func(self, name, cashout):
        self.cashout = int(input('How much did {} cashout with?'.format(self.name)))
        
    def pay(self, winner, loserdebt):
        if self.gameresult > winner.gameresult:
            # Overpayment. $50 debt, $25 winnings
            print("{} pays {} {}.".format(self.name, winner.name, winner.gameresult))
            loserdebt = loserdebt - winner.gameresult #reduce loserdebt
            self.gameresult = self.gameresult - winner.gameresult # $50 debt reduced by $25 winnings
            winner.gameresult = 0 #winner no longer owed
            return loserdebt
        elif self.gameresult < winner.gameresult: 
            # Underpayment. Think $50 debt, $60 winnings
            if self.gameresult == 0:
                return loserdebt
            else: 
                print("{} pays {} {}.".format(self.name, winner.name, self.gameresult))
                loserdebt = loserdebt - self.gameresult #reduce loserdebt
                winner.gameresult = winner.gameresult - self.gameresult # $60 winnings reduced by $50
                loser.gameresult = 0 #debtor is free! $50 paid, loser is clear
                return loserdebt
        elif self.gameresult == winner.gameresult: 
            # Exact payment. $50 debt, $50 winnings.
            print("{} pays {} {}.".format(self.name, winner.name, self.gameresult))
            loserdebt = loserdebt - self.gameresult 
            self.gameresult = 0
            winner.gameresult = 0
            return loserdebt
        

numplayers = int(input('How many players do you have?\n'))
# players = [Player("Player {}".format(i+1), 0, 0, 0) for i in range(numplayers)]
players = []
totalbuyin = 0
totalcashout = 0

count = 0
while count < numplayers:
    # ogName = "Player " + count
    ogName = "Player {}".format(count + 1)

    name = input("\nWhat is the name of {}?\n".format(ogName))
    buyin = int(input("\nHow much did {} buy in for?\n".format(name)))
    totalbuyin = totalbuyin + buyin
    cashout = int(input("\nHow much did {} cash out for?\n".format(name)))
    totalcashout = totalcashout + cashout
    gameresult = cashout - buyin

    player = Player(name, buyin, cashout, gameresult)
    players.append(player)
    count+= 1

        
# Collect input data
# for player in players:
#     player.name = input("\nWhat is the name of {}?\n".format(player.name))
#     player.buyin = int(input("\nHow much did {} buy in for?\n".format(player.name)))
#     totalbuyin = totalbuyin + player.buyin
#     player.cashout = int(input("\nHow much did {} cash out for?\n".format(player.name)))
#     totalcashout = totalcashout + player.cashout
#     player.gameresult = player.cashout - player.buyin

# Checksum to send user to restart if buyin and cashout totals don't match
if totalbuyin != totalcashout:
    print("ERROR: CHECK BUYIN / CASHOUT OUT MATH.\n TOTAL BUYIN MUST EQUAL TOTAL CASH OUT.")

winners = []
losers = []

print("\nRESULTS: -------------------")

for player in players:
    if player.gameresult > 0:
        winners.append(player)
        print("{} won {}.".format(player.name, player.gameresult))
    elif player.gameresult < 0:
        losers.append(player)
        print("{} lost {}.".format(player.name, player.gameresult))
    elif player.gameresult == 0:
        print("{} didn't win or lose money.".format(player.name))
    else:
        print("I'm not sure what happened.")


loserdebt = 0

for winner in winners:
    loserdebt = loserdebt + winner.gameresult

# convert loser.gameresults into positive numbers
for loser in losers:
    loser.gameresult = loser.gameresult * -1


# What are the conditions for payment?
# REDO ALL OF THESE WITH THE IDEA THAT LOSER.GAMERESULTS ARE POSITIVE INSTEAD OF NEGATIVE

print("\nPAYMENTS: -------------------")

while loserdebt != 0:
    for loser in losers:
        if loser.gameresult > 0: #people owe money
            for winner in winners: #this person is owed money
                if winner.gameresult > 0: #this person hasn't been paid fully
                    #PAYMENT TIME. HOW MUCH? :D :D :D :D :D :D 
                    loserdebt = loser.pay(winner, loserdebt)
                    
                    # if loser.gameresult > winner.gameresult:
                    #     # Overpayment. $50 debt, $25 winnings
                    #     print("{} pays {} {}.".format(loser.name, winner.name, winner.gameresult))
                    #     loserdebt = loserdebt - winner.gameresult #reduce loserdebt
                    #     loser.gameresult = loser.gameresult - winner.gameresult # $50 debt reduced by $25 winnings
                    #     winner.gameresult = 0 #winner no longer owed
                    # elif loser.gameresult < winner.gameresult: 
                    #     # Underpayment. Think $50 debt, $60 winnings
                    #     if loser.gameresult == 0:
                    #         break
                    #     print("{} pays {} {}.".format(loser.name, winner.name, loser.gameresult))
                    #     loserdebt = loserdebt - loser.gameresult #reduce loserdebt
                    #     winner.gameresult = winner.gameresult - loser.gameresult # $60 winnings reduced by $50
                    #     loser.gameresult = 0 #debtor is free! $50 paid, loser is clear
                    # elif loser.gameresult == winner.gameresult: 
                    #     # Exact payment. $50 debt, $50 winnings.
                    #     print("{} pays {} {}.".format(loser.name, winner.name, loser.gameresult))
                    #     loserdebt = loserdebt - loser.gameresult 
                    #     loser.gameresult = 0
                    #     winner.gameresult = 0
                          
# YESSSSSSSSSSSSSSSSSSSSS                    


print("\nSUMMARY: -------------------")
print("Players bought in for {}, and exited the game with {}.".format(totalbuyin, totalcashout))
print("Remaining debts between players after payments: {}".format(loserdebt))











