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
parser.add_argument('-d1', '--delimiter1', required = False, default = 'comma', choices=['comma', 'semicolon', 'colon', 'tab'], help = "The delimiter used in input file.")
parser.add_argument('-d2', '--delimiter2', required = False, choices = ['comma', 'semicolon', 'colon', 'tab'], help = "The delimiter used in output file.")
parser.add_argument('-q1', '--quotation1', required = True, choices = ['quoted', 'unquoted'], help = 'Specify if non-numeric values in input file are (un)quoted.')
parser.add_argument('-q2', '--quotation2', required = True, choices = ['quoted', 'unquoted'], help = 'Specify if non-numeric values in output file must be (un)quoted.')

args = parser.parse_args()

###########
# Delimiter
###########

if args.delimiter2 == None:
    args.delimiter2 = args.delimiter1

if args.delimiter1 == 'comma':
    args.delimiter1 = ','

elif args.delimiter1 == 'colon':
    args.delimiter1 = ':'

elif args.delimiter1 == 'semicolon':
    args.delimiter1 = ';'

elif args.delimiter1 == 'tab':
    args.delimiter1 = '\t'

if args.delimiter2 == 'comma':
    args.delimiter2 = ','

elif args.delimiter2 == 'colon':
    args.delimiter2 = ':'

elif args.delimiter2 == 'semicolon':
    args.delimiter2 = ';'

elif args.delimiter2 == 'tab':
    args.delimiter2 = '\t'

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
    if args.quotation1 == 'unquoted':
        csvreader = csv.reader(csvfile, delimiter = args.delimiter1)
        data = list(csvreader)
    
    else:
        try:
            csvreader = csv.reader(csvfile, delimiter = args.delimiter1, quoting = csv.QUOTE_NONNUMERIC)
            data = list(csvreader)
        
        except Exception as e:
            sys.exit(f"Error: {e}\nNon-numeric values in the input file must be quoted by default. Your input file probably contains unquoted non-numeric values. If this is the case, you need to use the '-q1 unquoted' option. This option will instruct the script to read non-numeric values as strings and not attempt to convert them to numbers.")
    
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
                sys.exit(f"Error: invalid csv file: The amount of columns differs between rows. Your input file probably contains unquoted fields with a comma (e.g. float with comma as decimal separator).")

####################
# Transpose the data
####################

transposed_data = list(map(list, zip(*data)))

#########################################
# Write the transposed data to a new file
#########################################

# Do not quote any of the fields in the output file
if args.quotation2 == 'unquoted':
    with open(output_file, 'w', newline = '') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter = args.delimiter2)
        csvwriter.writerows(transposed_data)

# Use the same quotation as the input file
elif args.quotation2 == 'quoted' and args.quotation1 == 'quoted':
    with open(output_file, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter = args.delimiter2, quoting = csv.QUOTE_NONNUMERIC)
        csvwriter.writerows(transposed_data)

# Autogenerate quotation: All fields that can not be converted to a numeric value, will be quoted
elif args.quotation2 == 'quoted' and args.quotation1 ==  'unquoted':
    with open(output_file, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter = args.delimiter2, quoting = csv.QUOTE_NONNUMERIC)
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

print(f"{basename} transposed and saved to {output_file}")