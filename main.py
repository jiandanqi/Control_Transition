import os
import sys
import pickle
import argparse

from data_management.read_csv import *

def create_args():
    parser = argparse.ArgumentParser(description="Parameter")
    # --- Input paths ---
    parser.add_argument('--input_path', default="E:/21_10_Control Transition/data/01_tracks.csv", type=str,
                        help='CSV file of the tracks')
    parsed_arguments = vars(parser.parse_args())
    return parsed_arguments
    print(args.input_path)
#if __name__ == '__main_' :
 #   create_args()
