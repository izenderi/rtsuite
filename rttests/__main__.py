import argparse
import sys
from rttests.rttests_main import rttests

__author__ = "Ziliang(Johnson)"
__copyright__ = "Copyright 2023, Ziliang(Johnson)"
__license__ = "MIT"
__maintainer__ = "Ziliang(Johnson)"
__email__ = "ziliang.zhang@email.ucr.edu"
__version__ = "1.0"

def parse_args(args):
    """Parses command line arguments
    """

    parser = argparse.ArgumentParser(prog='rttests',
        description="""Real-time Tests""")
    # parser.add_argument(
    #     "config_path", help="configurations for the pytorch2r10cnn to be generated")
    # parser.add_argument(
    #     "pytorch_path", help="Path of the r10cnn model to be generated")
    # parser.add_argument(
    #     "r10cnn_name", help="Name of the r10cnn model to be generated")
    # parser.add_argument("-i", "--input", action="store_true",
    #                     help="""Decide whether to generate input data for the model. Default is False""")
    # parser.add_argument("-t", "--num_tests", type=int,
    #                     help="""Number of tests to generate. Default is 10""", metavar='')

    return parser.parse_args(args)

def main(args=sys.argv[1:]):

    args = parse_args(args)
    # if args.input:
    #     include_input = True
    # else:
    #     include_input = False
    # if args.num_tests:
    #     num_tests = args.num_tests
    # else:
    #     num_tests = 10

    rttests()


if __name__ == '__main__':
    main(sys.argv[1:])