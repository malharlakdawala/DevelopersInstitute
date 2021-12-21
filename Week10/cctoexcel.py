# This script is designed to convert bank statements from pdf to excel.
#
# It has been tweaked on HDFC Bank Credit Card statements,
# but in theory you can use it on any PDF document.
#
# The script depends on camelot-py,
# which can be installed using pip
#
# pip install "camelot-py[cv]"


import os
import argparse
import camelot
import pandas as pd
from collections import defaultdict


def extract_df(path, password=None):
    # The default values from pdfminer are M = 2.0, W = 0.1 and L = 0.5
    laparams = {'char_margin': 2.0, 'word_margin': 0.2, 'line_margin': 1.0}

    # Extract all tables using the lattice algorithm
    lattice_tables = camelot.read_pdf(path, password=password,
                                      pages='all', flavor='lattice', line_scale=50, layout_kwargs=laparams)

    # Extract bounding boxes
    regions = defaultdict(list)
    for table in lattice_tables:
        bbox = [table._bbox[i] for i in [0, 3, 2, 1]]
        regions[table.page].append(bbox)

    df = pd.DataFrame()

    # Extract tables using the stream algorithm
    for page, boxes in regions.items():
        areas = [','.join([str(int(x)) for x in box]) for box in boxes]
        stream_tables = camelot.read_pdf(path, password=password, pages=str(page),
                                         flavor='stream', table_areas=areas, row_tol=5, layout_kwargs=laparams)
        dataframes = [table.df for table in stream_tables]
        dataframes = pd.concat(dataframes)
        df = df.append(dataframes)

    return df


def main(args):
    for file_name in os.listdir(args.in_dir):
        root, ext = os.path.splitext(file_name)
        if ext.lower() != '.pdf':
            continue
        pdf_path = os.path.join(args.in_dir, file_name)
        print(f'Processing: {pdf_path}')
        df = extract_df(pdf_path, args.password)
        excel_name = root + '.xlsx'
        excel_path = os.path.join(args.out_dir, excel_name)
        df.to_excel(excel_path)
        print(f'Processed : {excel_path}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--in-dir', type=str, required=True, help='directory to read statement PDFs from.')
    parser.add_argument('--out-dir', type=str, required=True, help='directory to store statement XLSX to.')
    parser.add_argument('--password', type=str, default=None, help='password for the statement PDF.')
    args = parser.parse_args()

    main(args)

# py cctoexcel.py --in-dir "C:\Users\malha\Downloads\test" --out-dir "C:\Users\malha\Downloads" --password "<password>"
