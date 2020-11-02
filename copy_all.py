import argparse
from tsv_to_csv import tar_to_csv
from os import path, listdir, makedirs, system


def create_argument_parser():
    '''
    argument parser
    basic usage:
        parser = create_argument_parser()
        args = parser.parse.parse_args()
    '''
    arg_parser = argparse.ArgumentParser(description='Script to parser arguments')
    arg_parser.add_argument('output gcp storage bucket',
                            type=str,
                            help='path and name of output bucket')

    return arg_parser


def create_dict(file_path):
    directory = path.dirname(file_path)
    if not path.exists(directory):
        makedirs(directory)


if __name__ == '__main__':
    parser = create_argument_parser()
    args = parser.parse_args()

    dir_path = path.dirname(path.realpath(__file__))
    files = [x for x in listdir(dir_path) if ".tsv" in x]
    for file in files:
        create_dict("temp")
        output_file = file.replace(".tsv",".csv")
        tar_to_csv(file, "temp/" + output_file)
    system("gsutil temp/*.csv gs://movies-ingestion")


