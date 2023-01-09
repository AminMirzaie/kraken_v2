import pandas as pd
import glob
import os
summary = pd.read_csv("../resources/assembly_summary.txt",sep = "\t",skiprows=1)
fileNames = glob.glob("../genomes/*.fna")
gbrs_paired_asm_myFiles = [p[11:26] for p in glob.glob("../genomes/*.fna")]
filesName = []
for i in range(len(gbrs_paired_asm_myFiles)):
    l = fileNames[i].split("/")
    old_path_name = fileNames[i]
    new_path_name = l[0]+"/"+l[1]+"/"+ str(int(summary[summary["gbrs_paired_asm"] == gbrs_paired_asm_myFiles[i]]["taxid"]))+".fna"
    os.rename(old_path_name, new_path_name)
    filesName.append(new_path_name)
for fname in filesName:
    with open(fname,'r') as f:
        lines = f.readlines()
    chrom = ""
    chromList =[]
    count =0
    z =0
    for line in lines:
        if line[0] == '>' and count ==0:
            count += 1
        elif line[0] == '>' and count !=0:
            chromList.append(chrom)
            chrom = ""
        elif z== len(lines)-1:
            chrom = chrom +line.strip()
            chromList.append(chrom)
        else:
            chrom = chrom +line.strip()  
        z+=1 
    kmerLenght = 31
    kmerlist = []
    for chrom in chromList:
        for i in range(len(chrom)-kmerLenght+1):
            kmerlist.append(chrom[i:i+kmerLenght])
    with open(".."+fname.split(".")[2]+"_kmer.fq", 'w') as filehandle:
        filehandle.writelines("%s\n" % place for place in kmerlist)
