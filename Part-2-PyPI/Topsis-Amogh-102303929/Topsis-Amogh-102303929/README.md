# Topsis-Amogh-102303929

A command-line tool that ranks alternatives using **TOPSIS** (Technique for Order of Preference by Similarity to Ideal Solution), a multi-criteria decision analysis method.

TOPSIS scores each alternative by how close it is to an ideal best option and how far it is from an ideal worst option, across weighted criteria.

## Install

```
pip install Topsis-Amogh-102303929
```

## Usage

```
topsis <InputFile> <Weights> <Impacts> <OutputFile>
```

- **InputFile**: a CSV file. The first column names the alternatives; every other column is a numeric criterion (at least two criteria).
- **Weights**: comma-separated numbers, one per criterion, e.g. `"1,1,1,2"`.
- **Impacts**: comma-separated `+` or `-`, one per criterion. `+` means higher is better, `-` means lower is better.
- **OutputFile**: the CSV to write. It is the input plus two columns, `Topsis Score` and `Rank`.

## Example

`data.csv`:

```
Model,Price,Mileage,Comfort,Safety
A,250000,20,7,8
B,300000,18,8,9
C,200000,22,6,7
```

Price is better when lower, so its impact is `-`:

```
topsis data.csv "1,1,1,1" "-,+,+,+" result.csv
```

## How it works

1. Normalise each criterion column (divide by the square root of the sum of squares).
2. Multiply each column by its weight.
3. Find the ideal best and ideal worst value for each criterion, using its impact.
4. Measure each alternative's Euclidean distance to the ideal best (S+) and ideal worst (S-).
5. Score = S- / (S+ + S-), between 0 and 1. The highest score is ranked 1.

## Input checks

The tool stops with a clear error if the file is missing or unreadable, has fewer than three columns, contains non-numeric criteria values, has a different number of weights, impacts and criteria, has non-numeric weights, or has an impact other than `+` or `-`.

## Author

Amogh Singh
