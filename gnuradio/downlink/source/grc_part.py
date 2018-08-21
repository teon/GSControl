import argparse
import file_source

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", required=False, default=False, action="store_true",
                    help="Increase output verbosity.")
parser.add_argument("-p", "--path", required=False, default="",
                    help="Path for IQ recording (for File IQ source)")
parser.add_argument("-s", "--source", required=True, default="",
                    help="Source:")
args = parser.parse_args()

if args.source == "file":
    print "file"
elif args.source == "pluto":
    print "pluto"
elif args.source == "funcubeplus":
    print "Funcube plus"
else:
    print "Any"
