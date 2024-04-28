print("Welcome to the secret auction program.")

biders_bids = []
bider_information = {}
bids_list = []

while True:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    other_biders = input("Are there any other bideres? (yes or no): ")

    bider_information['name'] = name
    bider_information['bid'] = bid

    bids_list.append(bid)

    if other_biders.lower() == 'no':
        biders_bids.append(bider_information)
        break
    elif other_biders.lower() == 'yes':
        biders_bids.append(bider_information)

higest_bid = max(bids_list)

for entry in biders_bids:
    if entry['bid'] == higest_bid:
        higest_bider = entry['name']
    else:
        continue


print(f"{higest_bider} bided the highest with {higest_bid}")