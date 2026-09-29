"""
Show the number of unique authors in the database.
"""
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str, help='Input file path')
    parser.add_argument('-o', '--output', type=str, help='Output file path')
    args = parser.parse_args()
    print(f"Input file: {args.input}")
    print(f"Output file: {args.output}")
    authors = set()
    with open(args.input, "r") as f:
        col = next(f)
        for line in f:
            authors.add(line.strip().split(",")[0])
    print(f"Number of unique authors: {len(authors)}")
    print(list(authors)[:10])  # Print first 10 authors
    
def take_avg(a,b):
    return (a+b)/2
    
if __name__ == "__main__":
    main()