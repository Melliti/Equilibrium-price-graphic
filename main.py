import csvParser
import graphic

loader = csvParser.csvParser()
graphic = graphic.Graphic()
loader.loadCSV()
graphic.drawGraphic(loader.prices, loader.Qd, loader.Qs)