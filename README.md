# csv-helper
CSV helper helps you reorganize your CSV files.

Usage:

```sh
$ python3 main.py -h
usage: main.py [-h] [--output OUTPUT] --fields FIELDS [--include-headers]
               source

Process a selected CSV file.

positional arguments:
  source                CSV source file path

optional arguments:
  -h, --help            show this help message and exit
  --output OUTPUT, -o OUTPUT
                        The file path where the output CSV will be saved. If
                        no path provided, it will use the stdout.
  --fields FIELDS       List of fields to be selected, case sensitive,
                        separated with comma (,). Throws error if a field is
                        not existed in the CSV file.
  --include-headers     Flag to include CSV headers in the output.
```
