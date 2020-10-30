import pandas as pd
import argparse


def create_argument_parser():
    '''
    argument parser
    basic usage:
        parser = create_argument_parser()
        args = parser.parse.parse_args()
    '''
    arg_parser = argparse.ArgumentParser(description='Script to parser arguments')
    arg_parser.add_argument('input_file',
                            type=str,
                            help='path and name of input file')
    arg_parser.add_argument('output_file',
                            type=str,
                            help='output file name and path')

    return arg_parser


def tar_to_csv(input_file, output_file):
    """Convert TSV file to CSV using pandas"""
    print("reading file", input_file)
    csv_table = pd.read_table(input_file, sep='\t')
    print("saving file", output_file)
    csv_table.to_csv(output_file, index=False)
    print("conversion finished")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = create_argument_parser()
    args = parser.parse_args()

    tar_to_csv(args.input_file, args.output_file)
