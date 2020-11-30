#Remove duplicated rows from a csv file
import pandas as pd

df = pd.read_csv("/Users/jana/Box/Gagacheva/Sudoku/MasterFilesProgress/pl17to23_11_09_20_miss.csv")

tst = df.drop_duplicates('Gene.Coordinates', keep = 'first')

tst.to_csv("/Users/jana/Box/Gagacheva/Sudoku/MasterFilesProgress/tst-seq-11-09_miss.csv", index = False)

####Drop Duplicates
# csv = pd.read_csv("/Users/jana/Box/Gagacheva/Sudoku/MasterFilesProgress/missing_10_23_20-ALL.csv", sep = ",")
#``
# dedup = csv.drop_duplicates(subset='Gene.Coordinates')
#
# dedup.to_csv("/Users/jana/Box/Gagacheva/Sudoku/MasterFilesProgress/missing_10_23_20-tst.csv", index = False)
