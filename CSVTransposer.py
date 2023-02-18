#!/usr/bin/python3

################################################################################################
# Author: Mathias Verbeke
# Date of creation: 2022/02/18
# Summary: This Python script is a simple tool for transposing CSV files, which allows users to 
# switch the orientation of the data from rows to columns or vice versa. It reads in a CSV file, 
# transposes the data, and writes the transposed data to a new CSV file.
################################################################################################

##################
# Imported modules
##################

import argparse, csv, sys, os

########################
# Command line arguments
########################

parser = argparse.ArgumentParser()

parser.add_argument('infile', help = 'Provide the name of the input file.')
parser.add_argument('-d', '--delimiter', required = False, default = 'comma', choices=['comma', 'semicolon', 'colon', 'tab'])
parser.add_argument('-n', '--newdelimiter', required = False, choices = ['comma', 'semicolon', 'colon', 'tab'])
parser.add_argument('-q', '--quote', action = 'store_true', help = 'Quote al non-numeric values.')

args = parser.parse_args()

###########
# Variables
###########

if args.newdelimiter == None:
    args.newdelimiter = args.delimiter

if args.delimiter == 'comma':
    args.delimiter = ','

elif args.delimiter == 'colon':
    args.delimiter = ':'

elif args.delimiter == 'semicolon':
    args.delimiter = ';'

elif args.delimiter == 'tab':
    args.delimiter = '\t'

if args.newdelimiter == 'comma':
    args.newdelimiter = ','

elif args.newdelimiter == 'colon':
    args.newdelimiter = ':'

elif args.newdelimiter == 'semicolon':
    args.newdelimiter = ';'

elif args.newdelimiter == 'tab':
    args.newdelimiter = '\t'
 
##################
# Output file path
##################
basename = os.path.basename(args.infile)
dirname = os.path.dirname(args.infile)

output_file = f"{dirname}/transposed_{basename}"

#########################
# Read the input CSV file
#########################

with open(args.infile, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    data = list(csvreader)

    #################################################
    # Check if all the rows have equal column lengths
    #################################################

    flag = "NOK"
    for row in data:

        if len(row) == 0:
            sys.exit(f"Error: invalid csv file: There are empty rows in the csv file.")

        elif flag == "NOK":
            NoColumns = len(row)
            flag = "OK"
        
        elif flag == "OK":
            columns = len(row)

            if columns != NoColumns:
                sys.exit(f"Error: invalid csv file: The amount of numbers between columns differs between rows.")

# Transpose the data
transposed_data = list(map(list, zip(*data)))

# Write the transposed data to a new CSV file
if args.quote != True:
    with open(output_file, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=args.newdelimiter)
        csvwriter.writerows(transposed_data)

else:
    with open(output_file, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=args.newdelimiter, quoting=csv.QUOTE_NONNUMERIC)
        for row in transposed_data:
            new_row = []
            for item in row:
                # Test if field is numeric
                try:
                    item = float(item)
                    
                    # Test if field is integer
                    if item.is_integer():
                        item = int(item)

                except:
                    pass
                
                new_row.append(item)
            csvwriter.writerow(new_row)

print(f"{args.infile} transposed and saved to {output_file}")