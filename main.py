import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt
import time
from sklearn.datasets import make_spd_matrix
#from relaxationMethod import relaxationMethod
#from soprGradMethod import soprGradMethod
from MetodNaiskorSp import MetodNaiscorSp
#from 

#основная функция (подпрограмма), запускающая все тесты и получающая
#результаты замеров скорости выполнения [и точности] и визуализирующая
#эти результаты в графическом или табличном представлении.'''
def main():
  
  nList = [4, 8, 10, 20, 40, 199]
  eps = 10**(-20)
  timeValues = np.zeros(shape=(6,4))
  print("start")
  iter = 0
  for n in nList:
    matrix = generateMatrix(n)
    b = np.random.rand(n)
    timeValues[iter] = startAllFunc(matrix, b, n, eps)
    iter+=1
  makeGraphics(timeValues, nList)
  print("exit")
    
#функция, генерирующая матрицу порядка 𝑛 с заданными свойствами 
#(симметричность и положительная определенность).
def generateMatrix(n):
  
    matrix = make_spd_matrix(n)
    return matrix
    
#Функция, замеряющая время выполнения всех 
#методов на системе определенного порядка 𝑛.
def startAllFunc(matrix, b, n, eps):

    start_time = time.time()
    #relaxationMethod(matrix, b, eps)
    end_time = time.time()
    time_relaxation = end_time - start_time
  
    start_time = time.time()
    #minNevyazkaMethod(matrix, b, eps)
    end_time = time.time()
    time_minNevyazka = end_time - start_time
   
    start_time = time.time()
  # soprGradMethod(matrix, b, eps)
    end_time = time.time()
    time_soprGrad = end_time - start_time

    start_time = time.time()
    MetodNaiscorSp(matrix, b, eps)
    end_time = time.time()
    time_NaiskorSp = end_time - start_time

    #tmp
    print(time_soprGrad)
    
    timeValues = [time_relaxation, time_minNevyazka, time_soprGrad, 0]
    return timeValues

#рисуем графички
def makeGraphics(timeValues, nList):
  
    names = ['релакс', 'мин.невязк', 'сопр.град', 'наиск.спуск']
    plt.figure(figsize=(15, 10))
    for i in range(int(timeValues.size/len(names))):
      ax = plt.subplot(2, 3, i+1)
      ax.bar(names, timeValues[i])
      ax.set_title('n = %.2f' %nList[i])
    plt.show()

#запуск
main()
