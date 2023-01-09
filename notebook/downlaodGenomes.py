from Bio import SeqIO
import time
from ete3 import NCBITaxa
import pandas as pd
import os
import wget
import sys
ncbi = NCBITaxa() 
ParentNode=sys.argv[1] #inja ro bayad karbar bde az kojaye derakht b paeen mikhad
ParentTaxid = ncbi.get_name_translator([ParentNode])[ParentNode][0]
tree = ncbi.get_descendant_taxa(ParentNode, return_tree=True)
leavesTaxIds=[]
for t in tree.iter_leaves():
    leavesTaxIds.append(int(t.get_leaf_names()[0]))
with open('taxids.txt', 'w') as f:
    for item in leavesTaxIds:
        f.write("%s\n" % item)
