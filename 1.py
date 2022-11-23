# 1277. Count Square Submatrices with All Ones
# Cуть: учитывая m * n матрицу из единиц и нулей, вернуть,
# сколько квадратных подматриц имеют все единицы.

# Пройдемся по каждому столбцу и строке, ждя каждого столбца и строки посчитаем кол-во квадратов
# сложность - O(n^2)

from typing import List
def countSquares(matrix: List[List[int]]) -> int:
        
        #напишем счетчик
        count = 0      
        col_size = len(matrix[0]) #кол-во столбцов
        row_size = len(matrix) #кол-во строк

        for col in range(col_size): # пройдемся теперь по всему столбцу
            for row in range(row_size): #и строке
                size = min(row_size - row,col_size - col) # посчитаем оптимальное кол-во квадратов
                for n in range(size):  #для каждого значения n
                    add = 0
                    for i in range(n + 1):   
                        add += sum(matrix[row + i][col:col + n + 1])    
                    if add != (1 + n)*(n + 1):
                        break
                    else:
                        count = count + 1
        return count
print(countSquares([
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]))     