import os
import sys
import pandas as pd
import numpy as np
from os.path import expanduser

fas_file = input("Enter your fas file:")
ref_file = input("Enter your reference file:")

inp = fas_file
pth = os.path.dirname(inp)

outpt_name = "trimmed-seqs-tst.txt"
outpt = os.path.join(pth, outpt_name)

home = expanduser("~")
cutadapt_path = "Library/Python/3.8/bin/cutadapt"
ctdpt = os.path.join(home, cutadapt_path)

command = [
    ctdpt,
    "-a",
    "AcctTGTTGG...GTTTAAGAGC",
    "--discard-untrimmed",
    "-m=20",
    "-M=20",
    "-o",
    outpt.strip(),
    inp.strip()
]
import subprocess
process = subprocess.Popen(command, stdout=subprocess.PIPE)
output, error = process.communicate()

guides = pd.read_csv(outpt, sep = ",", header = None)
#read every other row to extract the sequences and the name of the clones
guides_seq = guides[guides.index % 2 != 0]
guides_seq.columns = ["Sequence"]
####print(isinstance(guides_seq, pd.DataFrame))
guides_seq.loc[:,"Index"] = range(len(guides_seq))
guides_seq = guides_seq.set_index("Index")
guides_nms = guides[guides.index % 2 == 0]
guides_nms.columns = ["Plate Coordinate"]
####print(isinstance(guides_nms, pd.DataFrame))
guides_nms.loc[:,"Index"] = range(len(guides_nms))
guides_nms = guides_nms.set_index("Index")


# #remove the prefix and suffix of the clone name]
replace_values = {'>': '', '_QB0058': ''}
guides_nms2 = guides_nms.replace(replace_values, regex = True)

#Add the original well and plate columns
result = pd.merge(guides_nms2, guides_seq, on='Index')
result['Origin.well.position'] = ""
result['Origin.plate'] = ""

for i, row in enumerate(result["Plate Coordinate"]):
    row2 = str(row)
    row2 = row2.split("-")
    #print(row2)
    plate = row2[2]
    well = row2[3]
    indx = i
    # result.at[indx, 'Origin.well.position'] = well
    # result.at[indx, 'Origin.plate'] = plate
    result.loc[indx, 'Origin.well.position'] = well
    result.loc[indx, 'Origin.plate'] = plate

result2 = result.drop(['Plate Coordinate'], axis=1)

###########load reference file
reference = ref_file.strip()
guides_ref = pd.read_csv(reference)
guides_ref2 = guides_ref.drop(['Origin.Well.Position', 'Origin.Plate'], axis=1)

#find the guides that are present and the ones that are not in the sequence clones
guides_present = pd.merge(guides_ref2, result2, on = "Sequence") #present

# Identify what values are in guides_ref2 and not in guides_present
Sequence_diff = set(guides_ref2.Sequence).difference(result2.Sequence)
where_diff = guides_ref2.Sequence.isin(Sequence_diff)
#print(len(where_diff.index))

# Slice TableB accordingly and append to TableA
guides_missing = guides_ref2[where_diff]

missing_name = "guides_misssing.csv"
present_name = "guides_present.csv"
missing_path = os.path.join(pth, missing_name)
present_path = os.path.join(pth, present_name)

# export the dataframes as csv files:
guides_missing.to_csv(missing_path, index = False)
guides_present.to_csv(present_path, index = False)
