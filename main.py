import csv
import argparse
import os
import sys

def create_parser():
  parser = argparse.ArgumentParser(description='Process a selected CSV file.')
  parser.add_argument('source', type=str, help="CSV source file path")
  parser.add_argument('--output', '-o', type=str, help="The file path where the output CSV will be saved. If no path provided, it will use the stdout.")
  parser.add_argument('--fields', required=True, type=str, help="List of fields to be selected, case sensitive, separated with comma (,). Throws error if a field is not existed in the CSV file.")
  parser.add_argument('--include-headers', action='store_true', help="Flag to include CSV headers in the output.")
  return parser

def process_csv(args):
  if not args.source.endswith('.csv'):
    raise Exception('The selected file is not a csv file')

  if args.output:
    sys.stdout = open(args.output)

  with open(args.source, 'r') as f:
    reader = csv.DictReader(f)
    headers_selected = args.fields.split(',')
    print(headers_selected)
    for row in reader:
      row_hash = dict(row)
      rows = [row_hash[header] for header in headers_selected]
      print(",".join(rows))


if __name__ == "__main__":
  parser = create_parser()
  args = parser.parse_args()

  process_csv(args)
