import maxminddb as mmdb
import pandas as pd


class MaxMind(object):
    """To obtain geo info by using geo-lite"""
    def __init__(self, geo_lite_path):
        super(MaxMind, self).__init__()
        self.geo_lite_path = geo_lite_path

    def find(self, ip):
        with mmdb.open_database(self.geo_lite_path) as conn:
            df = pd.DataFrame(conn.get(ip))
        return df
