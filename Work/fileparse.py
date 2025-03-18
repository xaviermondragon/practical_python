# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    """
    Parse a CSV file into a list of records
    """
    # You can't select columns by name if the file doesn't have headers
    if select and not has_headers:
        raise ValueError('select argument requires column headers')

    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # Read the file headers (if any)
        headers = next(rows) if has_headers else []

        # If specific columns have been selected, make indices for filtering
        if select:
            indices = [headers.index(col_name) for col_name in select]
            headers = select if has_headers else []
        else:
            indices = []

        records = []
        for row_no, row in enumerate(rows, 1):
            if not row:    # Skip rows with no data
                continue

            # Filter the row if a specific column selection was given
            if indices:
                row = [row[index] for index in indices]

            # Convert values to specific types if these were specified
            if types:
                try:
                    row = [type_conv(val) for val, type_conv in zip(row, types)]
                except ValueError as e:
                    if not silence_errors:
                        print(f'Row {row_no}: Couldn\'t convert {row}')
                        print(f'Row {row_no}: Reason {e}')
                    continue

            # If headers were given make a dictionary or else a tuple of the values
            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)

    return records
