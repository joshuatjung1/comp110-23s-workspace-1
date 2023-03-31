from csv import DictReader

def read_csv_rows(filename: str) -> list[dict[str,str]]:
    """Read csv file and return as a list of dicts with header keys."""
    result: list[dict[str,str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_vals(table: list[dict[str,str]], header: str) -> list[str]:
    """Return values in a table column under a specific header."""
    result: list[str] = []
    #step through table 
    for row in table: 
        #save every value under the key "header"
        result.append(row[header])
    return result


def columnar(table: list[dict[str, str]]) -> dict[str,list[str]]:
    """Reformats data so that it's a dictionary with column headers as keys."""
    results: dict[str, list[str]] = {}
    # loop through keys of one row of table
    first_row: dict[str, str] = table[0]
    for keys in first_row:
        # for each key, make a dictionary entry with all column values
        results[keys] = column_vals(table, keys)
    return results
