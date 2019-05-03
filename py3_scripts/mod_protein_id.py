__author__ = 'briansmith'

#!/usr/bin/env python

import argparse, textwrap

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
    description = textwrap.dedent('''\
                                 Author: Brian A. Smith
                                 University of Arizona
                                 basmith@email.arizona.edu

				 This script will replace protein ID with a count ID'''))
parser.add_argument("-i", "--input", required = True,
		   help = "FASTA Amino Acids file required")
parser.add_argument("-o", "--output", required = True,
		   help = "Desierd output file name")

args = parser.parse_args()

file = open(args.input, 'r')
out_file = open(args.output, 'w')

line_count = 1
for line in file.readlines():
	if line.startswith(">"):
		line = ">" + str(line_count)+"\n"
		out_file.write(line)
		line_count += 1
	elif not line.startswith(">"):
		out_file.write(line)
file.close()
