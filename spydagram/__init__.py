import argparse
# All package functions are held in app...
# Pull in the userspace functions here:
from spydagram.app import sketch, svgToPng
from spydagram.template import graph

# If run as an executable - enter here 
def _cli_entrypoint():
    '''Entry point for the CLI
    '''
    # Parse arguments
    parser = argparse.ArgumentParser(
        prog='spydagram',
        description='Generate an SVG digram from a script file')
    
    parser.add_argument("-if", '--inputfile', type=str,
                        help='Name of the input file')
    
    parser.add_argument("-of", '--outputfile', type=str,
                        help='Name of the output file')

    args = parser.parse_args()

    # TOFO: Complete
    print("Run in Executable-Mode")
    print(args.inputfile, args.outputfile)
