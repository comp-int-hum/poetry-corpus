import gzip
import argparse


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--index", dest="index", help="HathiTrust index")
    parser.add_argument("--output", dest="output", help="Output")
    args, rest = parser.parse_known_args()

    with gzip.open(args.index, "rt") as ifd:
        for line in ifd:
            pass
    
    #with gzip.open(args.output, "wt") as ofd:
    #    pass
