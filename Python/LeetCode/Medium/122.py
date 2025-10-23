from typing import List

def maxProfit(prices: List[int]) -> int:
    
    if not prices:
        return 0

    min_price = prices[0]
    profit = 0
    all_time_profit = 0
    
    for price in prices[1:]:
        profit = max(profit, price - min_price)
        
        if min_price < price:
            all_time_profit +=  price - min_price
            min_price = price
            
        min_price = min(min_price, price)

    return all_time_profit
        
print(maxProfit([7,1,5,3,6,4]))