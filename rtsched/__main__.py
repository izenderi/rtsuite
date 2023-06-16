import argparse
import sys
from rtsched.rtsched_main import rtsched

__author__ = "Ziliang(Johnson)"
__copyright__ = "Copyright 2023, Ziliang(Johnson)"
__license__ = "MIT"
__maintainer__ = "Ziliang(Johnson)"
__email__ = "ziliang.zhang@email.ucr.edu"
__version__ = "1.0"

def parse_args(args):
    """Parses command line arguments
    """

    parser = argparse.ArgumentParser(prog='rtsched',
        description="""Real-time Scheduler Tools for plotting and analysis""")
    parser.add_argument(
        "taskset_path", help="taskset csv file path to be tested")
    parser.add_argument(
        "line_mode", choices={"single", "multi"}, 
        help="line mode for plotting")
    parser.add_argument(
        "sched_policy", 
        choices={"rm", "dm", "edf"},
        help="Shceudling Policy with the test")

    return parser.parse_args(args)

def main(args=sys.argv[1:]):

    args = parse_args(args)

    rtsched(args.taskset_path, args.line_mode, args.sched_policy)


if __name__ == '__main__':
    main(sys.argv[1:])