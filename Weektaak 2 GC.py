DNAfile = open("/Users/jacy/Documents/Bio-Informatica/Blok 1/Bio-Informatica/Weekopdracht 1/LIG1 Arabidopsis thaliana_datasets/ncbi_dataset/data/gene.fna","r")
seq = DNAfile.read()
DNAfile.close()

aantal_G = seq.count ("G")
aantal_C = seq.count ("C")
aantal_A = seq.count ("A")
aantal_T = seq.count ("T")

len_DNA = len(seq)

print (seq)
print("G: ", aantal_G)
print("C: ", aantal_C)
print("A: ", aantal_A)
print("T: ", aantal_T)
print("lengte van DNA: ", len_DNA)

gc_per = (aantal_G + aantal_C)/len_DNA * 100
print ("GC%: ",gc_per)
