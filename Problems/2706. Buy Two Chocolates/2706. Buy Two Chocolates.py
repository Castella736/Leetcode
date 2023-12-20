class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min_val = [float('inf'), float('inf')]
        
        for price in prices:
            if price < min_val[0]:
                min_val[1] = min_val[0]
                min_val[0] = price
            elif price < min_val[1]:
                min_val[1] = price
                
        return money-sum(min_val) if money-sum(min_val) >= 0 else money