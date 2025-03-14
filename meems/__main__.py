#!/usr/bin/env python

"""
Command line interface to Simpd
"""

import argparse
import meems


def parse_command_line():
    "parses args for meems command"

    # init parser and add arguments
    parser = argparse.ArgumentParser(description="MEEMS: Simulate georeferenced community data")

    # add long args
    parser.add_argument(
        "--num_sites",
        help="Number of sites to sample from",
        type=int, default=10)

    parser.add_argument(
        "--num_species",
        help="Number of species globally",
        type=int, default=10)

    parser.add_argument(
        "--num_samples_per_site",
        help="Number of samples per site",
        type=int, default=5)

    parser.add_argument(
        "-o", help="Output file for simulation",
        dest="outfile", default=None)

    parser.add_argument(
        "-v", "--verbose", 
        help="Increase output verbosity",
        dest="verbose", action="store_true")

    # parse args
    return parser.parse_args()


def main():
    args = parse_command_line()
    m = meems.MEEMS(num_sites = args.num_sites,
                num_species = args.num_species,
                num_samples_per_site = args.num_samples_per_site,
                verbose=args.verbose)

    m.sim()
    if args.outfile:
        m.write_sim(args.outfile)
    else:
        print(m.df.to_csv(index=False))

if __name__ == "__main__":
    args = parse_command_line()
    m = meems.MEEMS(num_sites = args.num_sites,
                num_species = args.num_species,
                num_samples_per_site = args.num_samples_per_site,
                verbose=args.verbose)
    m.sim()
    print(m.df.head())
