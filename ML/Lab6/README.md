# Свёрточная сеть

Целью работы было постройка сверточной нейронной сети и проведение экспериментов на наборе данных.

Была построена свёрточная “нейронная” сеть, состоящая из последовательности преобразований свёртки и пулинга. Вывод сети завершается SoftArgMax преобразованием. Была найдена наилучшая
архитектура сети. Для поиска параметров был использован один из методов адаптивного градиентного спуска.  
В качестве минимизируемой функции ошибки была использована перекрёстная энтропия, а в качестве контрольной функции ошибки - Accuracy (Error Rate).   
Была построена обыкновенная матрица неточностей, а также матрица, у которой в ячейке i,j находится изображение класса i, которое сеть посчитала наиболее похожим на класс j.  

*График Accuracy от количества эпох. MNIST*

[MNISTAcc](./img/AccMNIST.png)

*Матрица неточнностей. MNIST*

[MNISTTrue](./img/TrueLabelMNIST.png)

*Матрица схожих элементов. MNIST*

[MNISTMax](./img/MaxMNIST.png)

*График Accuracy от количества эпох. Fashion-MNIST*

[FMNISTAcc](./img/AccFMNIST.png)

*Матрица неточнностей. Fashion-MNIST*

[FMNISTTrue](./img/TrueLabelFMNIST.png)

*Матрица схожих элементов. Fashion-MNIST*

[FMNISTMax](./img/MaxFMNIST.png)