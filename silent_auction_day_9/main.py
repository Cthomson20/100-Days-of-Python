# caesar cipher to practice dictionaries, loops, functions, etc
# imported art file provided by 100 days of Code written by Dr. Angela Yu


import art

print(art.logo)
bidding = True
bids = {}


def get_highest_bid(bidders):
    highest_bid = 0
    winner = ""
    for bidders in bids:
        bid_amount = bids[bidders]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidders
    print(f"The Winner is {winner} with a bid of ${highest_bid}")

while bidding:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid
    continue_bid = input("Are there any other bidders? Type 'yes or 'no'. \n ")
    if continue_bid == "yes":
        bidding = True
        print("\n" * 50)
    else:
        get_highest_bid(bids)
        bidding = False



