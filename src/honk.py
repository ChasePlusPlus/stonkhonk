import requests
import sys

CONFIG_PATH = '../keys/stonkhonk.config'


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
	return resp


def honk(quote):
	print(quote)


def main():
	print("HONK HONK")
	alphakey = getCreds()
	running = True
	while running:
		cmd = input(">>>:")
		print(cmd)
		if cmd == 'exit':
			running = False
			sys.exit("HONK HONK")

		elif 'honk' in cmd:
			cmds = cmd.split()
			if len(cmds) < 2:
				print("honk <symbol>")
				break
			symbol = cmds[1]
			quote = getQuote(symbol, alphakey)			
			honk(quote)

		elif cmd == 'help':
			print("HELP:")
			print("\texit:\texit/ctrl-d")
			
			print("\thonk:\t")
			print("\thonk <SYMBOL>\treturns quote for symbol")



if __name__ == "__main__":
	main()


