import pandas
import numpy as np

# JUDGE_WAY FILE

#Tracks (XX_tracks.csv)
FRAME = "frame"
TRACK_ID = "id"
X = "x"
Y = "y"
WIDTH = "width"
HEIGHT = "height"
FRONT_SIGHT_DISTANCE = "frontSightDistance"
BACK_SIGHT_DISTANCE = "backSightDistance"
DHW = "dhw"
THW = "thw"
TTC = "ttc"
LANE_ID = "laneId"

#Track Meta Information (XX_tracksMeta.csv)
NUMFRAMES = "numFrames"
DRIVINGDIRECTION = "drivingDirection"


def read_track_csv(arguments):
    """
    This method reads the tracks file from highD data.

    :param arguments: the parsed arguments for the program containing the input path for the tracks csv file.
    :return: a list containing all tracks as dictionaries.
    """
    # Read the csv file, convert it into a useful data structure
    df = pandas.read_csv(arguments["input_path"])
    # Use groupby to aggregate track info. Less error prone than iterating over the data.
    grouped = df.groupby([TRACK_ID], sort=False)
    # Efficiently pre-allocate an empty list of sufficient size
    tracks = [None] * grouped.ngroups
    current_track = 0
    for group_id, rows in grouped:
        tracks_Parameter = np.array(rows[X].values,
                           rows[Y].values,
                           rows[WIDTH].values,
                           rows[HEIGHT].values)
        tracks[current_track] = {TRACK_ID: np.int64(group_id),  # for compatibility, int would be more space efficient
                                 FRAME: rows[FRAME].values,
                                 FRONT_SIGHT_DISTANCE: rows[FRONT_SIGHT_DISTANCE].values,
                                 BACK_SIGHT_DISTANCE: rows[BACK_SIGHT_DISTANCE].values,
                                 THW: rows[THW].values,
                                 TTC: rows[TTC].values,
                                 DHW: rows[DHW].values,
                                 LANE_ID: rows[LANE_ID].values
                                 }
        current_track = current_track + 1
    return tracks