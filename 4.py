#122. Best Time to Buy and Sell Stock II

#Вам дан целочисленный массив, prices, где prices[i] - цена данной акции в день

#Каждый день вы можете решить купить и/или продать акции.
#В любой момент времени вы можете владеть не более чем одной акцией.
#Однако вы можете купить его и тут же продать в тот же день .

#Найдите и верните максимальную прибыль, которую вы можете получить 
#сложность - O(n)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_hold, cur_not_hold = 0 #так как мы не можем продать в первый же день, 
     
        for stock_price in prices:
            prev_hold, prev_not_hold = cur_hold, cur_not_hold

            #есть два варианта
            
			# либо держать акции у себя, либо продать их
            cur_hold = max( prev_hold, prev_not_hold - stock_price )
			
			# не оставлять их у сеья и распродать их сегодня по цене акции
            cur_not_hold = max( prev_not_hold, prev_hold + stock_price )
            
        return cur_not_hold   #максимальная прибыль 
