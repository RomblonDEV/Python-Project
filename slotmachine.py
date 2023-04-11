import random


MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_value = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        #Inside of this for loop we check that every single symbol in line or row
        #that we're checkin gis the same, so we can get the first symbol that in this row 
        #and then just make sure it's same for the rest of the symbols
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)
    return winnings, winnings_lines
            
        

def get_slot_machine_spinner(rows, cols, symbols):
    #We gonna generate what symbols are goin to be in each column
    #based on the frequency of symbos that we have
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for i in range(symbol_count):
            all_symbols.append(symbol)
            
    columns = []#Defining column list
    for col in range(cols):#Generating column for every single column thus game have
        #This code will picking random values for each
        column =[]
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

#Print the column 
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(column) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()
                

# creating a function for the deposit
def deposit():
    while True:
        amount = input("How much you would like to deposit? ₱")
        
        #this code will check if the amount is numeric
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("You have insufficient moeny to play the game")
        else:
            print("Please enter your amount in numeric format.")
    return amount

#this function is for lines of the slot games, asking the player if how many lines the bet on the game
def number_lines():
    while True:
        lines = input(f"How many number of lines you wish to play (1 - {str(MAX_LINES)})")
        
        #this code will check if the amount is numeric
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter the valid lines you wish to play")
        else:
            print("Please enter your amount in numeric format.")
    return lines
    

def get_bet():
    while True:
        amount = input("How much you would like to bet? ₱")
        
        #this code will check if the amount is numeric
        if amount.isdigit():
            amount = int(amount)
            if  MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount of bet is between ₱{MIN_BET} - ₱{MAX_BET}.")
        else:
            print("Please enter your amount in numeric format.")
    return amount
    

def game(balance):
    lines = number_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"You don't have enough money to to bet, your current balance is ₱{balance}")
        else:
            break
            
    print(f"You're betting ₱{bet} on {lines} lines. Total bet is {total_bet}.")
    slots = get_slot_machine_spinner(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winnings_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ₱{winnings}")
    return winnings - total_bet

#We can call this function again and then it will rerun the game
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ₱{balance}")
        spin = input("Press enter to play or (q to quit)")
        if spin == "q":
            break
        balance += game(balance)
    
    
    
main()