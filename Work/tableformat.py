# tableformat.py

class TableFormatter:
    def headings(self, headers):
        """
        Emit the table headings
        """
        raise NotImplementedError()

    def row(self, row_data):
        """
        Emit a single row ot table data
        """
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    """
    Emit a table in plain_text format
    """
    def headings(self, headers):
        for header in headers:
            print(f'{header:>10s}', end='')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, row_data):
        for d in row_data:
            print(f'{d:>10s}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    """
    Output portfolio data in CSV format
    """
    def headings(self, headers):
        print(','.join(headers))

    def row(self, row_data):
        print(','.join(row_data))

class HTMLTableFormatter(TableFormatter):
    """
    Output portfolio data in HTML format
    """
    def headings(self, headers):
        print('<tr><th>' + '</th><th>'.join(headers) + '</th></tr>')

    def row(self, row_data):
        print('<tr><td>' + '</td><td>'.join(row_data) + '</td></tr>')

def create_formatter(name):
    if name == 'txt':
        return TextTableFormatter()
    elif name == 'csv':
        return CSVTableFormatter()
    elif name == 'html':
        return  HTMLTableFormatter()
    else:
        raise RuntimeError(f'Unknown format {name}')
