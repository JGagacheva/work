########################Transform the table with mesure concentrations:
#########Transform a csv file from columns to rows and add the data to appropriate position into a master CSV file:
import pandas as pd
#
# conc = pd.read_csv("/Users/jana/Box/Gagacheva/Sudoku/QuantFluorDNAmeasurments-11-11-2020/Pl.1-7-concentrations-11-11-2020.csv")
#
# for col in conc:
#     if "plate" in col:
#         indx = conc.columns.get_loc(col)
#         conc.insert(loc = indx, column = "Plate Name", value = col,  allow_duplicates = True)
#
# colNames=["Well Name", "PlateName1", "plate1", "PlateName2", "plate2", "PlateName3", "plate3", "PlateName4", "plate4", "PlateName5", "plate5", "PlateName6", "plate6", "PlateName7", "plate7"]
# conc.columns = colNames
#
# for col in conc:
#     conc[col] = conc[col].astype(str).str.replace("plate", "HG_plate")
#
# for col in conc.columns[1:]:
#     if "PlateName" in col:
#         indx = conc.columns.get_loc(col)
#         conc["Well Name - " + str(indx)] = conc["Well Name"].astype(str) + " " + conc[col]
#
# conc.to_csv("/Users/jana/Box/Gagacheva/Sudoku/QuantFluorDNAmeasurments-11-11-2020/DNA-Concentration-01-11-Transformed.csv", index = False)

#At this point, after exporting the file, switch to R because it's easier to handle and rearrange tables.
conc = pd.read_csv("/Users/jana/Box/Gagacheva/Sudoku/QuantFluorDNAmeasurments-11-11-2020/DNA-Concentration-01-11-Transformed.csv")
for col in conc:
    if "plate" in col:
        indx = conc.columns.get_loc(col) - 1
        conc.insert(loc = indx, column = "Plate Name", value = col)

conc.to_csv("/Users/jana/Box/Gagacheva/Sudoku/QuantFluorDNAmeasurments-11-11-2020/DNA-Concentration-01-11-Transformed.csv", index = False)
