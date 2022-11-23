# House Robber 2
#Поскольку дома круглые, и мы не можем грабить дома 1 и n вместе, у нас есть 2 варианта:

#1> Ограбить дома от 1 до n-1 - текущий дом - он не может грабить предыдущий i-1 дом, но может безопасно перейти к предыдущему i-2 
#2> Ограбить дома от 2 до n - не грабить текущий дом - грабитель получает всю возможную добычу от ограбления i-1и всех последующих зданий.

#Здесь мы можем использовать два массива для хранения максимальной суммы для этих двух случаев


class Solution:
    def rob(self, nums):
        
        n = len(nums)
        if n == 1: return nums[0] 
        if n == 2: return max(nums[0], nums[1])
        
        arr_1 = [0] * n
        arr_2 = [0] * n 
        
        arr_1[0] = nums[0] 
        arr_1[1] = nums[0]

        arr_2[0] = 0
        arr_2[1] = nums[1]
        
        
        for i in range(2, n):
            arr_1[i] = max(nums[i] + arr_1[i - 2], arr_1[i - 1]) #первый случай
            arr_2[i] = max(nums[i] + arr_2[i - 2], arr_2[i - 1]) #второй случай
        
        return max(arr_1[n - 2], arr_2[n - 1]) #максимальная сумма этих двух случаев
