import sys

# Add Your functions here

def max_profit(money, prices, increases):
    total_profit = 0
    profits = [prices[i] * increases[i] / 100 for i in range(len(prices))]
    chosen = pick_houses(money, prices, profits)
    
    for profit in chosen:
        total_profit += profit
        
    return total_profit


"""
Returns a list of the profits stemming from the initial house purchases 
not exceeding the starting money that yield the maximum return     
"""
def pick_houses(money, prices, profits):
    pass
# You are allowed to change the main function. 

# Do not change the template file name. 

def main():

    # The first line is the amount of investment in million USD which is an integer number.
    line = sys.stdin.readline()
    line = line.strip()
    money = int(line)


# The second line includes an integer number which is the number of houses listed for sale.
    line = sys.stdin.readline()
    line = line.strip()
    num_houses = int(line)

    
    # The third line is a list of house prices in million dollar which is a list of \textit{integer numbers} (Consider that house prices can be an integer number in million dollar only).
    line = sys.stdin.readline()
    line = line.strip()
    prices = line.split(",")
    for i in range(0, len(prices)):
        prices[i] = int(prices[i])
    
   

    # read the number of vertices
    line = sys.stdin.readline()
    line = line.strip()
    increase = line.split(",")
    for i in range(0, len(increase)):
        increase[i] = float(increase[i])



# Add your implementation here .... 
    result =  max_profit(money, prices, increase) 

# Add your functions and call them to generate the result. 

    print(result)

    

    
main()

