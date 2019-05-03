#!/usr/bin/env python
__author__ = 'briansmith'



import argparse, textwrap


parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
    description = textwrap.dedent('''\
                                 Author: Brian A. Smith
                                 University of Arizona
                                 basmith@email.arizona.edu

                 Line slicing script of FASTA files
                 NOTE: step parameter has not been added.'''))
parser.add_argument("-i", "--input", required = True,
           help = "FASTA file required")
parser.add_argument("-o", "--output", required = True,
           help = "Desired output file name")
parser.add_argument("-s", "--start_slice", required = False,
                    type = int, help = "Select a starting position to cut [START:]")
parser.add_argument("-e", "--end_slice", required = False,
                    type = int, help = "Select an ending position to cut [:END]")
parser.add_argument("-R1", "--range1", required = False,
                    type = int, help = "Start of range slice extract [START:end]")
parser.add_argument("-R2", "--range2", required = False,
                    type = int, help = "End of range slice extract [start:END]")
parser.add_argument("-n", "--new_lines", required = False,
                    action = 'store_true', help = "Remove new lines in sequence (not including headers)")

args = parser.parse_args()

file = open(args.input, 'r')
out_file = open(args.output, 'w')

#Handling wrapped sequences

def fasta_unwrapper(input_file):
    fasta_count = 0
    for line in input_file:
        if line.startswith(">") and fasta_count == 0:
            input_data = line
        elif line.startswith(">") and fasta_count > 1:
            input_data += "\n" + line
        else:
            input_data += line.strip("\n")
        fasta_count += 1

    return input_data


if args.new_lines:
    fh = fasta_unwrapper(file).splitlines()
else:
    fh = file.readlines()


#Start of Slicing at proper index (python index n-1)
if args.start_slice:
    start_slice = args.start_slice - 1

if args.range1:
    range1 = args.range1 - 1


for line in fh:
    if line.startswith(">") and args.new_lines == True:
        out_file.write(line + "\n")
    elif line.startswith(">") and args.new_lines == False:
        out_file.write(line)
    elif not line.startswith(">"):
        line = line.strip('\n')
        if args.start_slice and args.end_slice:
            out_file.write(line[start_slice:])
            out_file.write(line[:args.end_slice])
        elif args.start_slice:
            out_file.write(line[start_slice:])
        elif args.end_slice:
            out_file.write(line[:args.end_slice])
        elif args.range1 and args.range2:
            out_file.write(line[range1:args.range2])
