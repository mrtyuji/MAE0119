import matplotlib.pyplot as plt
from random import randint
import numpy as np

def lancaDado():
    return randint(1, 6)

def freq(n):
    freq1 = [0]
    freq2 = [0]
    freq3 = [0]
    freq4 = [0]
    freq5 = [0]
    freq6 = [0]
    ocorr = [0, 0, 0, 0, 0, 0, 0]
    for i in range(1,n+1):
        r = lancaDado()
        ocorr[r-1] += 1
        freq1.append(ocorr[0]/i)
        freq2.append(ocorr[1]/i)
        freq3.append(ocorr[2]/i)
        freq4.append(ocorr[3]/i)
        freq5.append(ocorr[4]/i)
        freq6.append(ocorr[5]/i)
    return(freq1, freq2, freq3, freq4, freq5, freq6)

def plotgraf(n):
    freq1, freq2, freq3, freq4, freq5, freq6 = freq(n)
    plt.figure(figsize=(10, 10), dpi=80)
    plt.subplot(211)
    x = np.array(range(0,n+1))
    if (n > 0):
        plt.plot(x, freq1, 'r-', label = "Face 1")
        plt.plot(x, freq2, 'm-', label = "Face 2")
        plt.plot(x, freq3, 'g-', label = "Face 3")
        plt.plot(x, freq4, 'b-', label = "Face 4")
        plt.plot(x, freq5, 'y-', label = "Face 5")
        plt.plot(x, freq6, 'c-', label = "Face 6")
        plt.axis([0, n, -0.03, 1.03])
    else:
        plt.plot(x, freq1, 'ro')
        plt.plot(x, freq2, 'mo')
        plt.plot(x, freq3, 'go')
        plt.plot(x, freq4, 'bo')
        plt.plot(x, freq5, 'yo')
        plt.plot(x, freq6, 'co')
        plt.axis([-0.03, 1, -0.03, 1])
    plt.plot(x, [1/6]*(n+1), 'k--',label = "1/6")
    plt.legend(bbox_to_anchor = (0.8, -0.2), loc = 1, borderaxespad = 0.)
    plt.title("Gráfico de lançamento de dados")
    plt.xlabel("Número de lançamentos")
    plt.ylabel("Frenquência relativa")
    plt.grid(True)

    plt.subplot(223)
    histo = [freq1[n], freq2[n], freq3[n], freq4[n], freq5[n], freq6[n]]
    color = ['r', 'm', 'g', 'b', 'y', 'c']
    index = np.arange(1,7)
    plt.plot(x, [1/6]*(n+1), 'k--',label = "1/6")
    plt.bar(index, histo, color = color)
    plt.axis([1, 6.9, 0, 1])
    plt.title("Histograma de lançamento de dados")
    plt.xlabel("Faces")
    plt.ylabel("Densidade de frequência")

def main():
    n = int(input("Número de lançamentos: \n"))
    plotgraf(n)
    plt.show()

if __name__ == "__main__":
    main()
