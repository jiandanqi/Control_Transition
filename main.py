import os
import pickle
import argparse

from data_management.read_csv import *

def create_args():
    parser = argparse.ArgumentParser(description="Parameter")
    # --- Input paths ---
    parser.add_argument('--input_path', default="E:/21_10_Control Transition/data/01_tracks.csv", type=str,
                        help='CSV file of the tracks')
    parsed_arguments = vars(parser.parse_args())
    print(parsed_arguments)
    return parsed_arguments

if __name__ == '__main_' :
    created_arguments = create_args()
    print("Try to find the saved pickle file for better performance.")
    # Read the track csv and convert to useful format
    if os.path.exists(created_arguments["pickle_path"]):
        with open(created_arguments["pickle_path"], "rb") as fp:
            tracks = pickle.load(fp)
        print("Found pickle file {}.".format(created_arguments["pickle_path"]))
    else:
        print("Pickle file not found, csv will be imported now.")
        tracks = read_track_csv(created_arguments)
        print("Finished importing the pickle file.")

    if created_arguments["save_as_pickle"] and not os.path.exists(created_arguments["pickle_path"]):
        print("Save tracks to pickle file.")
        with open(created_arguments["pickle_path"], "wb") as fp:
            pickle.dump(tracks, fp)
