import csv
import sys

class csvParser:
    prices = []
    Qd = []
    Qs = []

    # Load and parser the CSV. Add values to arrays
    def loadCSV(self, filename = "data.csv"):
        if len(sys.argv) > 1:
            print(sys.argv[1])
            filename = sys.argv[1]
        try:
            with open(filename, "r") as csvFile:
                reader = csv.reader(csvFile, delimiter=",")
                count = 0
                for row in reader:
                    if count == 0:
                        count += 1
                        continue
                    self.prices.append(int(row[0]))
                    self.Qd.append(int(row[1]))
                    self.Qs.append(int(row[2]))
        except:
            print(f"Make sure you have a csv called {filename}")
            exit()