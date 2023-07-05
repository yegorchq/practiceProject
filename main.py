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
    
    
    
def generateMatrix(n):
    matrix = make_spd_matrix(n)
    return matrix
    
def startAllFunc(matrix, b, n)
    '''
    start_time = time.time()
    relaxationMethod()
    end_time = time.time()
    time_relaxation = end_time - start_time
    '''
    '''
    start_time = time.time()
    minNevyazkaMethod()
    end_time = time.time()
    time_minNevyazka = end_time - start_time
    '''
    '''
    start_time = time.time()
    minNevyazkaMethod()
    end_time = time.time()
    time_minNevyazka = end_time - start_time
    '''
    start_time = time.time()
    soprGradMethod()
    end_time = time.time()
    time_soprGrad = end_time - start_time
    
    timeValues = [time_relaxation, time_minNevyazka, time_soprGrad, time_Sonya]
    return timeValues