#Author: Courtney Leligdon
#		 University of Arizona

def populate_lists(lac107genes, Leaf58genes):
	lac107 = open("Lac107_MP_prokkagenes_list_updated.txt", 'r')
	for line in lac107:
		lac107genes.append(line.title())
	Leaf58 = open("leaf58_prokkagenes_list_updated.txt", 'r')	
	for line in Leaf58:
		Leaf58genes.append(line.title())
							
def main():
	lac107genes = []
	Leaf58genes = []
	populate_lists(lac107genes, Leaf58genes)
	genes = set(lac107genes).intersection(Leaf58genes)
	genes_sorted = sorted(genes)
	file = open("MegaplasmidProkkaGene_Overlap.txt", 'w')
	for item in genes_sorted:
		file.write("%s\n" % item)
	
if __name__ == "__main__":
    main()