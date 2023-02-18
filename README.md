# CSV Transposer
The CSV Transposer is a simple command-line tool for transposing CSV files, which allows users to switch the orientation of the data from rows to columns or vice versa. It reads in a CSV file, transposes the data, and writes the transposed data to a new CSV file.

## Usage
```bash
usage: CSVTransposer.py [-h] [-d {comma,semicolon,colon,tab}] [-n {comma,semicolon,colon,tab}] infile

positional arguments:
  infile                Provide the name of the input file.

options:
  -h, --help            show this help message and exit
  -d {comma,semicolon,colon,tab}, --delimiter {comma,semicolon,colon,tab}
  -n {comma,semicolon,colon,tab}, --newdelimiter {comma,semicolon,colon,tab}
```

## Input/Output
The CSV Transposer takes a single input file and produces a single output file.
### Input
The input file should be a CSV file with a header row and any number of data rows. All rows must have the same number of columns. The file can be delimited by a comma, tab, or any other character that can be specified using the -d or --delimiter flag.

Here is an example input file input.csv:
```bash
a,b,c
1,2,3
4,5,6
7,8,9
```

### Output
The output file will also be a CSV file with a header row and the same number of data rows as the input file, but with columns and rows transposed. By default, the output file will be delimited by the same delimiter as the input file.

Here is an example output file transposed_input.csv:
```bash
a,1,4,7
b,2,5,8
c,3,6,9
```

## Examples
```bash 
$ python CSVTransposer.py data.csv
```
This command will read in the input CSV file, which is seperated by a comma, transpose the data, and write the transposed data to a new CSV file called transposed_data.csv in the same directory as the input file.

```bash 
$ python CSVTransposer.py data.csv -d semicolon
```
This command will read in the input CSV file, which is separated by semicolons, transpose the data, and write the transposed data to a new CSV file called transposed_data.csv in the same directory as the input file.

## Contributing
Contributions are always welcome! If you find any issues or have suggestions for how to improve this tool, please feel free to open an issue or submit a pull request. To contribute, please follow these steps:
1. Fork the repository
2. Create a new branch for your changes
3. Make your changes and test them
4. Submit a pull request