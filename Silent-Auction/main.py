import art
print(art.hammer)

bids = {}
choice = True
def bidding():
    print("Welcome to the Silent Auction!")
    name = input("What is your name? ")
    bid = int(input("Place your bid : $"))
    bids[name] = bid


while choice :
    bidding()
    again = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if again == "no":
        choice = False
    elif again not in ["yes" , "no"]:
        print("Error!")
        break
    print("\n" * 100)

winner = max(bids,key = bids.get)
print(f"The winner is {winner} with the highest bid of ${bids[winner]}")
