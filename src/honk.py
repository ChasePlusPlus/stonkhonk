import requests
import sys
import json

CONFIG_PATH = '../keys/stonkhonk.config'
ALPHA_KEY = ""

class Stonk:
	def __init__(self, symbol, op, high, low, cur, vol, ltd, pc, chg, chgp):
		self.symbol = symbol
		self.openPrice = op
		self.high = high
		self.low = low
		self.currPrice = cur
		self.volume = vol
		self.lastTradeDay = ltd
		self.prevClose = pc
		self.change = chg
		self.changePct = chgp
	
	def honk(self):
		print("-----", self.symbol,"-----")	
		print("| Open:\t", self.openPrice)
		print("| Price:", self.currPrice)
		print("| Vol:\t", self.volume)
		print("----- /HONK -----")


def getCreds():
	with open(CONFIG_PATH,'r') as f:
		# print(f.readline())
		line = f.readline()
		alphakey = line.split('\'')[1]
		# alphakey = "testkey"
		return(alphakey)


def getQuote(symbol,key):
	url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol='+symbol+'&apikey='+key
	resp = requests.get(url)
	qt = resp.json()
	return qt


def getHonk(sym,key):
	stk = getQuote(sym,key)
	quote = stk['Global Quote']
	print(quote)
	stonk = Stonk(quote['01. symbol'], quote['02. open'], quote['03. high'], quote['04. low'], quote['05. price'], quote['06. volume'], quote['07. latest trading day'], quote['08. previous close'], quote['09. change'], quote['10. change percent'])
	stonk.honk()

def main():
	print("HONK HONK")

	alphakey = getCreds()
	ALPHA_KEY = alphakey
	running = True
	while running:
		cmd = input("$:")
		# print(cmd)
		if cmd == 'exit':
			running = False
			sys.exit("HONK HONK")

		elif 'honk' in cmd:
			cmds = cmd.split()
			if len(cmds) < 2:
				print("honk <symbol>")
				break
			symbol = cmds[1]
			getHonk(symbol,alphakey)			
			
		elif cmd == 'help':
			print("HELP:")
			print("\texit:\texit/ctrl-d")
			
			print("\thonk:\t")
			print("\thonk <SYMBOL>\treturns quote for symbol")



if __name__ == "__main__":
	main()


