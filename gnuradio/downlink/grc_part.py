import argparse
import source.file_source.run_with_file_browser as file_source
import source.funcube_source.funcube_source as funcube_source
import downlink as demodulator

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
    file_source.application()
elif args.source == "pluto":
    print "pluto"
elif args.source == "funcubeplus":
    print "Funcube plus"
    funcube_source.main()
elif args.source == "demodulator":
    print "demodulator"
    demodulator.main()
else:
    print "Any"
