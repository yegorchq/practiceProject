import numpy as np
import time
from sklearn.datasets import make_spd_matrix
from relaxationMethod import relaxationMethod
from soprGradMethod import soprGradMethod

'''основная функция (подпрограмма), запускающая все тесты и получающая
 результаты замеров скорости выполнения [и точности] и визуализирующая
  эти результаты в графическом или табличном представлении.'''
def main():
  nList = [4, 8, 10, 20, 40]
  for n in nList:
    matrix = generateMatrix(n)
    b = np.random.randint(n)
    timeValues = startAllFunc(matrix, b, n)
    makeGraphics(timeValues, n)
    
#функция, генерирующая матрицу порядка 𝑛 с заданными свойствами 
#(симметричность и положительная определенность).
def generateMatrix(n):
    matrix = make_spd_matrix(n)
    return matrix
    
#Функция, замеряющая время выполнения всех 
#методов на системе определенного порядка 𝑛.
def startAllFunc(matrix, b, n)
    '''
    start_time = time.time()
    relaxationMethod(matrix, b)
    end_time = time.time()
    time_relaxation = end_time - start_time
    '''
    '''
    start_time = time.time()
    minNevyazkaMethod(matrix, b)
    end_time = time.time()
    time_minNevyazka = end_time - start_time
    '''
    '''
    start_time = time.time()
    minNevyazkaMethod(matrix, b)
    end_time = time.time()
    time_minNevyazka = end_time - start_time
    '''
    start_time = time.time()
    soprGradMethod(matrix, b)
    end_time = time.time()
    time_soprGrad = end_time - start_time
    
    #tmp
    timeValues = np.zeros(4)
    timeValues = [time_relaxation, time_minNevyazka, time_soprGrad, time_3]
    return timeValues


#
def makeGraphics(timeValues, n):
    names = ['Релаксация', 'Мин. невязка', 'сопряженные градиенты', 'метод?']
    plt.figure(figsize=(3, 3))

    plt.plot(names, values)
    plt.suptitle('%.2f' %n)
    plt.show()  