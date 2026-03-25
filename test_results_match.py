import csv
import glob
import os


def _read_results_csv(path: str) -> set[tuple[str, str, str]]:
    """
    Returns normalized rows as (text1, text2, score_str).
    We normalize whitespace and keep score as a string so we can compare exact
    rounding/formatting as produced by compareWANSnoprint.py.
    """
    rows: set[tuple[str, str, str]] = set()
    with open(path, newline="") as f:
        reader = csv.reader(f)
        for r in reader:
            if not r:
                continue
            if len(r) != 3:
                raise AssertionError(f"Unexpected row shape in {path}: {r!r}")
            text1, text2, score = (c.strip() for c in r)
            if text1 and text2 and score:
                rows.add((text1, text2, score))
    return rows


def test_serial_results_match_parallel_results_folder():
    serial_path = "serial_results.csv"
    results_dir = "results"

    assert os.path.isfile(serial_path), f"Missing {serial_path}"
    assert os.path.isdir(results_dir), f"Missing {results_dir}/ directory"

    parallel_files = sorted(
        p for p in glob.glob(os.path.join(results_dir, "*.csv"))
        if os.path.basename(p) != os.path.basename(serial_path)
    )
    assert parallel_files, f"No per-author CSV files found in {results_dir}/"

    serial_rows = _read_results_csv(serial_path)

    parallel_rows: set[tuple[str, str, str]] = set()
    for p in parallel_files:
        parallel_rows |= _read_results_csv(p)

    missing_in_parallel = serial_rows - parallel_rows
    extra_in_parallel = parallel_rows - serial_rows

    assert not missing_in_parallel, (
        "Rows present in serial_results.csv but missing from results/*.csv, "
        f"example={next(iter(missing_in_parallel))!r}"
    )
    assert not extra_in_parallel, (
        "Rows present in results/*.csv but missing from serial_results.csv, "
        f"example={next(iter(extra_in_parallel))!r}"
    )