from typing import Any, Callable, Dict, Iterable, List, Tuple, Union
import csv

def parse_csv(
    lines,
    select: List[str] | None = None,
    types: List[Callable[[str], Any]] | None = None,
    has_headers: bool = True,
    delimiter: str = ',',
    silence_errors: bool = False
) -> Iterable[Dict[str, Any] | Tuple[str, float]]:
    """
    Parse a CSV file into a list of records with type conversion.
    """
    if select and not has_headers:
        raise RuntimeError('select requires column headers')

    rows = csv.reader(lines, delimiter=delimiter)

    # Read the file headers (if any)
    headers: List[str] = next(rows) if has_headers else []

    # If specific columns have been selected, make indices for filtering and set output columns
    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select

    records: List[Dict[str, Any] | Tuple[str, float]] = []
    for rowno, row in enumerate(rows, 1):
        if not row:  # Skip rows with no data
            continue

        # If specific column indices are selected, pick them out
        if select:
            row = [row[index] for index in indices]

        # Apply type conversion to the row
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    print(f"Row {rowno}: Couldn't convert {row}")
                    print(f"Row {rowno}: Reason {e}")
                continue

        # Make a dictionary or a tuple
        record: Any = None
        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)

        records.append(record)

    return records
