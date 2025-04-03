logo = '''

███████╗███████╗ ██████╗██████╗ ███████╗████████╗     █████╗ ██╗   ██╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗
██╔════╝██╔════╝██╔════╝██╔══██╗██╔════╝╚══██╔══╝    ██╔══██╗██║   ██║██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║
███████╗█████╗  ██║     ██████╔╝█████╗     ██║       ███████║██║   ██║██║        ██║   ██║██║   ██║██╔██╗ ██║
╚════██║██╔══╝  ██║     ██╔══██╗██╔══╝     ██║       ██╔══██║██║   ██║██║        ██║   ██║██║   ██║██║╚██╗██║
███████║███████╗╚██████╗██║  ██║███████╗   ██║       ██║  ██║╚██████╔╝╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║
╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝   ╚═╝       ╚═╝  ╚═╝ ╚═════╝  ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝

'''

print(logo)

bid_chain = []

while True:
    name = input('Welcome to seret auction!\nEnter your name: ')
    bid_price = float(input(f'Hello {name}, enter your bid price: $'))
    bid_chain.append({'name': name, 'bid_price': bid_price})
    has_other_bidder = input("Is there any other bidder? (yes/no): ").strip().lower()

    match has_other_bidder:
        case 'yes':
            continue
        case 'no':
            bid_chain.sort(key=lambda x: x['bid_price'], reverse=True)
            print('The winner is:')
            print(f"Name: {bid_chain[0]['name']}")
            print(f"Bid price: {bid_chain[0]['bid_price']}")
            print('Thanks for participating!')
            break
        case _:
            print('Invalid input, please enter yes or no')
            continue
