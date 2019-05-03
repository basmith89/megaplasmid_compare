#!/usr/bin/env python
__author__ = 'briansmith'
import csv
import re
import argparse, textwrap

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
    description = textwrap.dedent('''\
                                 Author: Brian A. Smith
                                 University of Arizona
                                 basmith@email.arizona.edu

                 This script will extract amino acid seq ID from
                 prokka's gff3 file and the start, end position into
                 a tab delimited file.
                 NOTE: ensure there are no comment lines in input file.
                 Also, It is critical the last column be enclosed by double quotes.
                 When I converted the .gff to .csv with excel it did this automatically.
                 If doing your own file conversion please add double quotes.'''))

parser.add_argument("-i", "--input", required = True,
           help = "FASTA file required")
parser.add_argument("-o", "--output", required = True,
           help = "Desired output file name")

args = parser.parse_args()

out_file = open(args.output, 'w')

#'rU' allows to read file unversial new-line mode
with open(args.input, 'rU') as f:
    #next(f)
    readcsv = csv.reader(f, delimiter=',')
    for row in readcsv:
        id = row[8]
        try:
            id = re.search(r'ID=(.*?);', row[8]).group(1)
        except AttributeError:
            found = 'No match found'
        gene_name = row[8]
        product_name = re.findall(r"(?<=product=).+$", row[8], re.M)
        try:
            gene_name = re.search(r';gene=(.*?);', row[8]).group(1)
        except AttributeError:
            found = 'No gene name found'

        except AttributeError:
             found = 'No product found'
        #Had to make a weird work around here because gene_name
        #would capture the entire attribute row even when
        #regex target was NOT present. Also note that product name
        #regex is findall method.  Couldn't get .search to work
        #like gene_name and id. So, used findall witch captures in
        #a list, turned that list into a string.
        if len(gene_name) > len('n'.join(product_name)):
            desc = '\n'.join(product_name)
        else:
            desc = gene_name
        startcoord = row[3]
        endcoord = row[4]
        out_file.write(id + "\t" + startcoord + "\t" + endcoord + "\t" + desc + "\n")
