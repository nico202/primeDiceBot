#Login details

# Username+password login not working anymore. Use the token instead.
# username = "INSERT_USERNAME_HERE"
# password = "INSERT_PASSWORD_HERE"

token = "INSERT_TOKEN_HERE"
# Read the readme on how to get it

#How much will this program run?
max_bet_number = 0          #0 is infinity
min_balance = 0             #Stop playing when reached min_balance
max_balance = 100000000     #Stop playing when reached max_balance

wait_time = 2               #Seconds to wait beetween requests

#Betting strategy
base_bet = 1                #minimum = 1
win_chance = 55             #maximum = 98,
maximum_bet = 100000000     #100000000 = 1 BTC

after_loss_multiplier = 2   #1 = do not multiply, 0 = return to base bet
after_win_multiplier = 0    #1 = do not multiply, 0 = return to base bet

after_loss_sum = 0          #After multiply, if lost, sum this
after_win_sum = 0           #After multiply, if win, sum this

after_loss_prob_sum = 0     #Can be negative too
after_win_prob_sum = 0      #Can be negative too

after_win_prob_reset = True #Just True or False
after_loss_prob_reset = False #Just True or False
