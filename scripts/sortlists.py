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
	Leaf58genes_sorted = sorted(Leaf58genes)
	lac107genes_sorted = sorted(lac107genes)
	file = open("Lac107_Different_prokkagenes.txt", 'w')
	for item in lac107genes_sorted:
		file.write("%s\n" % item)
	
	file2 = open("Leaf58_Different_prokkagenes.txt", 'w')
	for item in Leaf58genes_sorted:
		file2.write("%s\n" % item)
	




if __name__ == "__main__":
    main()