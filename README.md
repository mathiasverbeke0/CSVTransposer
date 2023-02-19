# CSV Transposer
The CSV Transposer is a simple command-line tool for transposing CSV files, which allows users to switch the orientation of the data from rows to columns or vice versa. It reads in a CSV file, transposes the data, and writes the transposed data to a new CSV file.

## Requirements
The script requires Python 3.x and the following Python modules:
* argparse
* csv
* sys
* os

## Usage
```bash
usage: CSVTransposer.py [-h] [-d1 {comma,semicolon,colon,tab}] [-d2 {comma,semicolon,colon,tab}] -q1 {quoted,unquoted} -q2 {quoted,unquoted} infile

positional arguments:
  infile                Provide the name of the input file.

options:
  -h, --help            show this help message and exit
  -d1 {comma,semicolon,colon,tab}, --delimiter1 {comma,semicolon,colon,tab}
                        The delimiter used in input file.
  -d2 {comma,semicolon,colon,tab}, --delimiter2 {comma,semicolon,colon,tab}
                        The delimiter used in output file.
  -q1 {quoted,unquoted}, --quotation1 {quoted,unquoted}
                        Specify if non-numeric values in input file are (un)quoted.
  -q2 {quoted,unquoted}, --quotation2 {quoted,unquoted}
                        Specify if non-numeric values in output file must be quoted.
```

## Example
### Input
Suppose we have a CSV file named input.csv that contains the following data:
```bash
Name,Age,City
John,25,New York
Mary,30,San Francisco
Bob,40,Los Angeles
```
The delimiter used in this file is a comma (,).

### Output
We want to transpose the data and write it to a new CSV file named transposed_input.csv. The new file should contain the following data:
```bash
"Name","John","Mary","Bob"
"Age",25,30,40
"City","New" "York","San" "Francisco","Los Angeles"
```

### Command
We want to specify that non-numeric values in the input file are unquoted and non-numeric values in the output file must be quoted. We can achieve this by using the -q1 unquoted -q2 quoted options.
Here's the command to achieve the desired output:
```bash
CSVTransposer.py -q1 unquoted -q2 quoted input.csv
```
We can also specify a different delimiter for the output file using the -d2 option. For example, if we want to use a semicolon (;) as the delimiter in the output file, we can use the following command:
```bash
CSVTransposer.py -q1 unquoted -q2 quoted -d2 semicolon input.csv
```

## Error messages
The script provides the following error messages:
* *Error: invalid csv file: There are empty rows in the csv file.*
* *Error: invalid csv file: The amount of columns differs between rows. Your input file probably contains unquoted fields with a comma (e.g. float with comma as decimal separator).*
* *Error: Error: could not convert string to float: 'Cardiac'. Non-numeric values in the input file must be quoted by default. Your input file probably contains unquoted non-numeric values. If this is the case, you need to use the '-q1 unquoted' option. This option will instruct the script to read non-numeric values as strings and not attempt to convert them to numbers.*

# Notes
* If the -d1 option is not provided, the tool will use the comma as default delimiter.
* The CSVTransposer tool is designed to work with comma, semicolon, colon, and tab-delimited CSV files.
* The input file should have consistent delimiters throughout the file, but the delimiter used in the input file can be different from the delimiter used in the output file.
If the input file contains a header row, the header row will be transposed to the first column in the output file.
* The script does not check if the output file already exists. If the output file already exists, it will be overwritten.

## Contributing
Contributions are always welcome! If you find any issues or have suggestions for how to improve this tool, please feel free to open an issue or submit a pull request. To contribute, please follow these steps:
1. Fork the repository
2. Create a new branch for your changes
3. Make your changes and test them
4. Submit a pull request