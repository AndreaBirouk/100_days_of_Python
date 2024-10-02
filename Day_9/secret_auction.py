from Day_9.art import gravel

print(gravel)


entries = {}

bidding_continues = True

while bidding_continues:
    name = input("what's you name?\n")
    bid = int(input("What's your bid?  £"))
    entries[name] = bid
    other_users = input("Are there any other bidders, who want to place a bid? Type 'yes' or 'no' \n").lower()
    

    if other_users == 'no':
        bidding_continues = False
    else:
        print('\n' * 100)

def get_highest_bidder(entries):
    highest_bid = max(entries.values())
    highest_bidder = ''
    for key in entries:
        if entries[key] == highest_bid:
            highest_bidder = key

    print(f"The winner is {highest_bidder} with the highest bid of {highest_bid}")

get_highest_bidder(entries=entries)