# Include standard modules
import argparse
from datetime import datetime

def check_date(s):
    try:
        return datetime.strptime(s, "%Y-%m-%d").date()
    except ValueError:
        msg = "Date format not valid: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)


def parse_cli_args():
    # Initiate the parser with a description
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", "-v", help="Show program version", action="store_true")
    parser.add_argument("-q", "--queryname", help="Name of the query to be run from the list of pre-defined queries", required=True, type=str)
    parser.add_argument("-s", "--startdate", help="Start Date in the format YYYY-MM-DD", required=True, type=check_date)
    parser.add_argument("-e", "--enddate", help="End Date in the format YYYY-MM-DD", required=True, type=check_date)
    parser.add_argument("--itemtype", "-t", help="Item Type", required=True, type=str)

    args = parser.parse_args()

    if args.queryname:
        print("Query Name: %s" % args.queryname)

    if args.startdate:
        print("Start Date: %s" % args.startdate)

    if args.enddate:
        print("End Date: %s" % args.enddate)

    if args.itemtype:
        print("Item type: %s" % args.itemtype)
	
    return args

#if __name__ == '__main__':
#    parse_cli_args()
