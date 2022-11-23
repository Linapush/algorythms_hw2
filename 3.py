# Препятствие и пробел отмечены в сетке как 1 и 0 соответственно.

# Arobot расположен в верхнем левом углу сетки = x, n
# Сетка препятствий[i][j] равна 0 или 1.
# Робот может двигаться только вниз или вправо в любой момент времени.
# Робот пытается добраться до нижнего правого угла сетки (на диаграмме ниже отмечено "Финиш").

# - нам нужно будет отслеживать текущее положение робота, которое мы обозначим как 'r, c'
# Рассмотрим, добавлены ли какие-либо препятствия к сеткам.

# Для каждой из ячеек:
# - Скобка и пробел отмечены в сетке как 1 и 0 соответственно.
# - мы можем пойти либо вправо, либо вниз
# - когда мы дойдем до нижнего правого угла
# - Мы нашли 1 возможный способ добраться до звезды

# Сложность - O(1)

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:         # если в начальной точке есть препятсивия, то мы просто возвращаемся
            return 0                        # у нас нет путей к финишной точке

        obstacleGrid[0][0] = 1              #До старта кол-во способов равно 1

        for i in range(1,m):                #для первого столбца
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1)
       
        for j in range(1, n):               #для первой строки
            obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] == 1)

        # Заполняем теперь значения: 
        # No. of ways of reaching cell[i][j] = cell[i - 1][j] + cell[i][j - 1]
        # i.e. From above and left.
        for i in range(1,m):            #для дотижения клетки [i][j] - кол-во способов = [i - 1][j] + [i][j - 1]
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0
           
        return obstacleGrid[m-1][n-1] #значения финишной клетки 

