from replit import clear
from art import logo


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


def main():
    print(logo)

    players = {}
    end_game = False

    while not end_game:
        name = input("What is your name? \n")
        price = int(input("What is your bid? $"))
        players[name] = price
        continue_game = input("Are there any other bidders? Type 'yes' or 'no'. \n")
        if continue_game == "no":
            end_game = True
        elif continue_game == "yes":
            clear()

    find_highest_bidder(players)


if __name__ == "__main__":
    main()
