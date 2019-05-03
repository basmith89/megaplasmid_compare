#!/usr/bin/env python
__author__ = 'briansmith'
import csv
import argparse, textwrap

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
    description = textwrap.dedent('''\
                                 Author: Brian A. Smith
                                 University of Arizona
                                 basmith@email.arizona.edu
		
		This script will match ids from the the BLAST results (query/subject ids)
                with the data produced by the gff_info_extract.py script.
            	 '''))

parser.add_argument("-i", "--id_file", required = True,
           help = "FASTA file required")
parser.add_argument("-d", "--data_file", required = True,
           help = "Desired output file name")
parser.add_argument("-o", "--output", required = True,
            help = "Desired output file name")

args = parser.parse_args()

out_file = open(args.output, 'w')

with open(args.id_file, 'r') as f:
    for sub_id in f:
        sub_id = sub_id.strip()

        with open(args.data_file, 'r') as data:
            readcsv = csv.reader(data, delimiter='\t')
            for row in readcsv:
                if sub_id == row[0]:
                    out_file.write('\t'.join(row) + "\n")
