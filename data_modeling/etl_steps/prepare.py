"""
This module provides Preparer classes to
prepare the raw files and make them ready
to be stored in the database.
"""
import numpy as np
import pandas as pd


def _types_to_native(values):
    native_values = values.apply(
        lambda x: x.items() if isinstance(x, np.generic) else x, axis=1)
    native_values = native_values.where(native_values.notnull(), None)
    return native_values


def _dataframe_to_dict(dataframe):
    return dataframe.to_dict("records")


class Preparer:
    """
    A generic preparer class.
    """

    def prepare(self, values):
        """
        Applies table specific preparation.
        """
        raise NotImplementedError

    def format(self, values):
        pass

    def transform(self, values):
        """
        Prepares the file, converts to native data types and converts to
        dictionary.
        """
        if isinstance(values, pd.Series):
            values = pd.DataFrame(values).T
        transformed_values = self.prepare(values)
        transformed_values = _types_to_native(transformed_values)
        transformed_values = _dataframe_to_dict(transformed_values)
        self.format(transformed_values)
        return transformed_values


class PreparerQuery1(Preparer):

    def prepare(self, values):
        prepared_values = values[["artist", "song", "length", "sessionId",
                                  "itemInSession"]]
        prepared_values.columns = ["artist_name", "song_title", "song_duration",
                                   "session_id", "item_in_session"]
        return prepared_values


class PreparerQuery2(Preparer):

    def prepare(self, values):
        prepared_values = values[["artist", "song", "firstName", "lastName",
                                  "userId", "sessionId", "itemInSession"]]
        prepared_values.columns = ["artist_name", "song_title", "user_first_name",
                                   "user_last_name", "user_id", "session_id", "item_in_session"]
        return prepared_values

    def format(self, values):
        for value in values:
            value["user_id"] = int(value["user_id"]) \
                if value["user_id"] is not None else None


class PreparerQuery3(Preparer):

    def prepare(self, values):
        prepared_values = values[["song", "firstName", "lastName", "userId"]]
        prepared_values.columns = ["song_title", "user_first_name",
                                   "user_last_name", "user_id"]
        return prepared_values

    def format(self, values):
        for value in values:
            value["user_id"] = int(value["user_id"]) \
                if value["user_id"] is not None else None
