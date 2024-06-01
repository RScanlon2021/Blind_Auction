from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console
bids = {}

def winning_bid(new_bidder, new_bid):
  bids[new_bidder] = new_bid # Ensure bids are stored as integers

auction_running = True

while auction_running:
  clear()
  print(logo)
  print("Welcome to the secret auction program!\n")
  
  bidder = input("What is your name? ")
  bid = input("What's your bid? $")

  winning_bid(bidder, bid)

  highest_bidder = max(bids, key=lambda k: bids[k])
  highest_bid = bids[highest_bidder]

  more_bids = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
  if more_bids == 'no':
      print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
      auction_running = False

