line_x = [26, 280, 375, 475, 630, 750]
line_y = [565]

table_settings = {
    'horizontal_strategy': 'lines',
    'vertical_strategy': 'explicit',
    'explicit_vertical_lines': line_x,
    'explicit_horizontal_lines': line_y,
    'intersection_x_tolerance': 10
}

import tqdm
import pdfplumber

pdf = pdfplumber.open("sponsors.pdf")

total_table = []
for page in tqdm.tqdm(pdf.pages):
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
            result_table[-1][-1] = result_table[-1][-1] or ''
            result_table[-1][-2] = result_table[-1][-2] or ''
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

import pandas as pd

df = pd.DataFrame(result_table, columns=['Organisation Name', 'Town/City', 'County', 'Type & Rating', 'Route'])
df.to_csv('sponsors.csv')
