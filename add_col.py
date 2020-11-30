import pandas as pd
import numpy as np

#input = pd.read_csv("/Users/jana/Box/Gagacheva/Sudoku/Sanger/651412-Plate22-c/pl22c-guides_present.csv")
input = input("Enter your pdf file:")
input = input.strip()
guides = pd.read_csv(input)

#guides['Plate ID'] = ""

# for i, row in enumerate(guides["Gene.Coordinates"]):
#     # bits = "HG_plate3_G02".split("_") #This line is just for test
#     row2 = str(row)
#     row2 = row2.split(" ")
#     #print(row2)
#     # foo = bits[0] + "_" + bits[1] + " " + "_".join(bits[2:]) #This line is just for test
#     row_concat = row2[0] + " " + row2[1]
#     indx = i
#     guides.at[indx, "Gene.Coordinates"] = row_concat
#     guides.at[indx, "Plate ID"] = row2[1]
#
# guides.to_csv(input, index = False)

#tst = guides.drop(['Oligo.Plate.Barcode','Origin.Well.Position', 'Origin.Plate'], axis=1)
tst = guides.drop(['Origin.Well.Position', 'Origin.Plate'], axis=1)
tst['Origin.well.position'] = ""
tst['Origin.plate'] = ""

for i, row in enumerate(tst["Plate Coordinates"]):
    row2 = str(row)
    row2 = row2.split(" ")
    print(row2)
    plate = row2[0]
    well = row2[1]
    indx = i
    tst.at[indx, 'Origin.well.position'] = well
    tst.at[indx, 'Origin.plate'] = plate


tst.to_csv(input, index = False)
