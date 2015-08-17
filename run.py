''' LICENCE
This file is part of primeDiceBot.

    primeDiceBot is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    primeDiceBot is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Nome-Programma.  If not, see <http://www.gnu.org/licenses/>.
'''

import primeDiceClass as primedice
import config
import sys
import time

print "Script is starting, please wait!"
helpme = primedice.helpers()

helpme.config_check(config)

user = primedice.primedice()

user.login(config.username, config.password)

bet_size = config.base_bet
probability = config.win_chance
print "Game is starting!"

while (user.bet_count < config.max_bet_number) \
or (user.balance >= config.min_balance)\
or (user.balance <= config.max_balance)\
or (bet_size <= maximum_bet):
    if bet_size > user.balance:
        print("Insufficient funds! :( Returning to base bet & probability")
        bet_size = config.base_bet
        probability = config.win_chance

    time.sleep(config.wait_time)
    user.bet_count += 1
    print "[%s] Betting %s, %s" % (user.bet_count, bet_size, probability),
    bet_feedback = user.bet(bet_size, probability, "<")

    if bet_feedback["win"]:
        print "WON,\tbalance = %s" % (user.balance)
        bet_size *= config.after_win_multiplier
        if not bet_size:
            bet_size = config.base_bet
        bet_size += config.after_win_sum

        if config.after_win_prob_reset:
            probability = config.win_chance
        else:
            probability += config.after_win_prob_sum

    else:
        print "LOST,\tbalance = %s" % (user.balance)
        bet_size *= config.after_loss_multiplier
        if not bet_size:
            bet_size = user.base_bet
        bet_size += config.after_loss_sum

        if config.after_loss_prob_reset:
            probability = config.win_chance
        else:
            probability += config.after_loss_prob_sum

    if probability > 98:
        probability = 98
    if probability < 0.01:
        probability = 0.01

print "I stopped playing"
