import os

import tqdm
import pdfplumber
import pandas as pd

def create_table(path='.', verbose=True):
    line_x = [26, 280, 375, 475, 630, 750]
    line_y = [565]

    table_settings = {
        'horizontal_strategy': 'lines',
        'vertical_strategy': 'explicit',
        'explicit_vertical_lines': line_x,
        'explicit_horizontal_lines': line_y,
        'intersection_x_tolerance': 10
    }

    output_pdf = os.path.join(path, 'sponsors.pdf')


    pdf = pdfplumber.open(output_pdf)

    total_table = []
    # Loading bar if verbose
    loading_bar = (tqdm.tqdm if verbose else lambda x: x)
    for page in loading_bar(pdf.pages):
        total_table += page.extract_table(table_settings)[1:]

    result_table = []
    merge_rows = False

    for row in total_table[1:]:
        is_blank = sum([not entry for entry in row]) == 5
        if is_blank:
            continue
        else:
            # If somehow the line continued into the next one, adds the remaining of
            if row[0] == '' and not merge_rows:
                result_table[-1][-1] += f'\n{row[-1]}'
                result_table[-1][-2] += f'\n{row[-2]}'
                continue
            elif row[-1] == '' and row[-2] == '':
                merge_rows = True
                previous_values = row[:-2]
                continue

            if not merge_rows:
                result_table += [row]
            else:
                result_table += [previous_values + row[-2:]]

            merge_rows = False


    df = pd.DataFrame(result_table, columns=['Organisation Name', 'Town/City', 'County', 'Type & Rating', 'Route'])
    df.to_csv(os.path.join(path, 'sponsors.csv'))

if __name__ == "__main__":
    create_table()
