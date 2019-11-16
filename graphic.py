import matplotlib.pyplot as plt

class Graphic:
    # Using array from csvParser, draw a graph
    def drawGraphic(self, price, qd, qs):
        plt.plot(qd, price, label="quantity demanded")
        plt.plot(qs, price, label="quantity supplied")
        plt.xlabel("Quantity")
        plt.ylabel("Price")
        plt.legend()
        plt.show()