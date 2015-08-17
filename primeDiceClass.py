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
import requests
import json
import sys

class primedice():
    def __init__(self):
        self.login_url = 'https://api.primedice.com/api/login'
        self.bet_url = 'https://api.primedice.com/api/bet'
        self.info_url = 'https://api.primedice.com/api/users/1'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/43.0.2357.130 Chrome/43.0.2357.130 Safari/537.36'
        }
        self.session = requests.Session()
        self.bet_count = 0

    def session_post(self, url, post):
        answer = self.session.post(url, data = post, headers = self.headers)
        if answer.status_code == 429:
            print "Too many requests"
        else:
            return answer

    def login(self, username, password):
        self.username = username
        self.password = password
        post_data = {
            'username':str(username),
            'password':str(password),
            'opt':''
        }

        login_response = self.session_post(self.login_url, post_data).content
        try:
            self.token = json.loads(login_response)["access_token"]
            self.bet_url_params = self.bet_url + "?access_token=" + self.token
            self.info_url_params = self.info_url + "?access_token=" + self.token

            self.balance = json.loads(\
            self.session.get(self.info_url_params).content\
            )["user"]["balance"]

            print "Login successful, token = %s" % (self.token)

        except:
            if login_response == "Unauthorized":
                sys.exit("Wrong login details")
            elif login_response == "Too many requests.":
                sys.exit("Too many requests. Wait before running the script again")
            else:
                print("Something went wrong, unknown error")
                sys.exit(login_response)

    def bet(self, amount = 0, target = 95, condition = "<"):
        try:
            target = float(target)
            amount = int(amount)
        except:
            return "Target must be an integer!"

        #try:
        if not condition in ["<",">"]:
            print "Wrong condition. Must be either > or <"
        else:
            params = {
                'access_token': self.token
            }
            post_data = {
                'amount': str(amount),
                'condition': str(condition),
                'target': str(target)
            }
            rix = self.session_post(self.bet_url_params, post = post_data)
            if rix.status_code == 200:
                bet_response = json.loads(rix.content)

                feedback = {
                    'jackpot': bet_response["bet"]["jackpot"],
                    'win': bet_response["bet"]["win"],
                    'amount': bet_response["bet"]["amount"],
                }
                self.balance = bet_response["user"]["balance"]
                return feedback
            elif rix.status_code == 400 and rix.content == "Insufficient funds":
                sys.exit("Insufficient funds")
            else:
                print "You have to debug this error"
                print rix
                print rix.content

        #except:
        #    print "Some error happened processing your request"

class helpers():
    def config_check(self, config):
        try:
            config.base_bet = float(config.base_bet)
        except:
            sys.exit("Base bet must be a float")

        try:
            config.base_bet = int(config.base_bet)
        except:
            sys.exit("Base bet must be a integer")

        try:
            config.win_chance = float(config.win_chance)
        except:
            sys.exit("Win chance must be a float")

        if config.win_chance > 98 or config.win_chance < 0.01:
            sys.exit("Win chance not in range 0.01 - 98")
