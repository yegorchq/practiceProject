import numpy as np
from relaxationMethod impirt relaxationMethod



'''основная функция (подпрограмма), запускающая все тесты и получающая
 результаты замеров скорости выполнения [и точности] и визуализирующая
  эти результаты в графическом или табличном представлении.'''
def main():
  nList = [4, 8, 10, 20 , 40]
  for n in nList:
    generateMatrix(n)
