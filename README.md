# kraken_v2
this is reimplementation of 
kraken: ultrafast metagenomic sequence classification using exact alignments article with some enhancement in ram and cpu usage.
# main article:
you can read main article from : 
https://genomebiology.biomedcentral.com/articles/10.1186/gb-2014-15-3-r46
# instruction 
for testing project
please go to notebook directory and open downloadAndExtract.ipynb with jupyter notebook then follow the instructions in notebook
# DownloadAndExtract.ipynb
in first notebook (DownloadAndExtract.ipynb) we want to download every genomes for all the leafs in NCBI taxonomy tree and then find all the kmers in each genomes. jelly fish can do Extraction part but I dont used that because it change order of kmers. so I wrote my code and print every kmer in file by slicing window acrross genomes 
# MakeIndex.ipynb
 in this notebook we want to download every genomes for all the leafs in NCBI taxonomy tree and then find all the kmers in each genomes. jelly fish can do Extraction part but I dont used that because it change order of kmers. so I wrote my code and print every kmer in file by slicing window acrross genomes 
the result of this note book is index file located in resources path of project and it will be used for searching taxonomy.
# readClassifier.ipynb
evaluation of our classifier using index file
