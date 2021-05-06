# RemoveTaxa
# Language: Python
# Input: TXT (keyword-value pairs)
# Output: CSV
# Tested with: PluMA 1.1, Python 3.6
# Dependency:

PluMA plugin that removes taxa whose names contain a specifed pattern of text.

The plugin accepts as input a parameter file of keyword-value pairs:
csvfile: The input CSV file of taxa
pattern: Target text pattern

The output CSV file will contain taxa from the input csvfile that do
not contain the target pattern in their name.
