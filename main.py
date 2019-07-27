import argparse
import csv
import logging
import os
import sys

DELIMITER = ','

def create_parser():
  parser = argparse.ArgumentParser(description='Process a selected CSV file.')
  parser.add_argument('source', type=str, help="CSV source file path")
  parser.add_argument('--output', '-o', type=str, help="The file path where the output CSV will be saved. If no path provided, it will use the stdout.")
  parser.add_argument('--fields', required=True, type=str, help="List of fields to be selected, case sensitive, separated with comma (,). Throws error if a field is not existed in the CSV file.")
  parser.add_argument('--include-headers', action='store_true', help="Flag to include CSV headers in the output.")
  parser.add_argument('--verbose', '-v', action='store_true', help="Verbose logging")
  return parser

def setup_logging(args):
  log_level = logging.INFO if args.verbose else logging.ERROR
  logging.basicConfig(format="%(asctime)s - %(message)s", level=log_level)

def setup_output(args):
  output_path = args.output
  if output_path:
    sys.stdout = open(output_path, "w+")

def join_row_with_delimiter(rows):
  return DELIMITER.join(rows)

def process_csv(args):
  filepath = args.source
  if not filepath.endswith('.csv'):
    raise Exception('The selected file is not a csv file')

  logging.info("Opening source file on %s ..." % (filepath))
  with open(filepath, 'r') as f:
    reader = csv.DictReader(f)
    headers_selected = args.fields.split(',')
    logging.info("...with new header(s) format: %s" % (headers_selected))
    if args.include_headers:
      print(join_row_with_delimiter(headers_selected))

    row_count = 0
    for row in reader:
      row_hash = dict(row)
      values = [row_hash[header] for header in headers_selected]
      row_count += 1
      print(join_row_with_delimiter(values))

    logging.info("Completed processing %d rows." % (row_count))

  logging.info("CSV processing successfully completed.")


if __name__ == "__main__":
  parser = create_parser()
  args = parser.parse_args()

  setup_logging(args)
  setup_output(args)
  process_csv(args)
