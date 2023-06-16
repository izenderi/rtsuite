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
    parser.add_argument(
        "taskset_path", help="taskset csv file path to be tested")
    parser.add_argument(
        "test_type",
        choices={"rt", "ub"},
        help="Real-time test type to be performed. \
            Choose from rt:Real-time test, \
            ub:Utilization Bound test")
    parser.add_argument(
        "sched_policy", 
        choices={"rm", "dm", "edf"},
        help="Shceudling Policy with the test")

    return parser.parse_args(args)

def main(args=sys.argv[1:]):

    args = parse_args(args)
    
    rttests(args.taskset_path, args.test_type, args.sched_policy)


if __name__ == '__main__':
    main(sys.argv[1:])