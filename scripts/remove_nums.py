#Author: Courtney Leligdon
#		 University of Arizona

def main():
	lac107 = open("Lac107_MP_prokkagenes_list.txt", 'r')
	lac107_updated = open("Lac107_MP_prokkagenes_list_updated.txt", 'w')
	for line in lac107:
		new_line = line.replace(line[:16], '')
		lac107_updated.write(new_line)
		
		
		
	Leaf58 = open("leaf58_prokkagenes_list.txt", 'r')	
	Leaf58_updated = open("leaf58_prokkagenes_list_updated.txt", 'w')
	for line in Leaf58:
		new_line = line.replace(line[:16], '')
		Leaf58_updated.write(new_line)


if __name__ == "__main__":
    main()