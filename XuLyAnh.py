import numpy
import matplotlib
import matplotlib.pyplot as plt


def pltSetup():
    pass


class Bai1():
    X1 = []
    X2 = [[9, 7, 1, 1, 1, 2, 2, 1],
          [8, 9, 9, 7, 1, 1, 1, 1],
          [7, 8, 9, 7, 1, 2, 1, 1],
          [8, 9, 9, 9, 9, 1, 1, 2],
          [8, 9, 9, 7, 7, 2, 1, 3],
          [9, 9, 9, 9, 8, 2, 2, 1],
          [9, 9, 8, 8, 7, 1, 2, 1],
          [8, 9, 8, 6, 5, 1, 1, 3]]

    def cau11(self):
        histRange = 9
        hist = numpy.zeros(histRange, dtype=int)
        x = numpy.arange(1, 10, 1)

        for row in range(len(self.X2)):
            for col in range(len(self.X2[row])):
                hist[self.X2[row][col] - 1] += 1
        y = numpy.sort(hist)
        fig, ax = plt.subplots()
        ax.set_ylabel("Hist")
        ax.bar(x, hist)
        ax.set_xticks(x)
        ax.set_yticks(y)

        plt.show()
        return hist


if __name__ == '__main__':
    baitap = Bai1()
    result = baitap.cau11()
    print(repr(result))
