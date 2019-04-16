"""
This module provides helper methods for the rest of the
project.
"""
import os

import pandas as pd


def read_file(filepath):
    """
    Reads a .csv file.
    """
    return pd.read_csv(filepath)


def get_files(filepath, extension=".csv"):
    """
    Gets all files in nested filepath.
    """
    all_files = os.listdir(filepath)
    all_files = [os.path.join(filepath, file) for file in all_files if file.endswith(extension)]
    return all_files
