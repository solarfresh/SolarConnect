import pandas as pd
from pymongo import MongoClient


class MongoConnector(object):
    """
    Function to connect and query from mongo db
    """

    # create connect pool and open database
    def __init__(self, user=None, passwd=None, host='', port=27017, db='', **kwargs):
        db_url = "mongodb://{}:{}@{}:{}/".format(user, passwd, host, port)
        if not user or passwd:
            client = MongoClient(host, port)
        else:
            client = MongoClient(db_url)
        self.client = client
        self.db = client[db]

    def find(self, collection, query={}, projection=None, limit=None):
        cursor = self.db[collection].find(query, projection)
        if limit:
            cursor = cursor.limit(limit)
        df = pd.DataFrame([doc for doc in cursor])
        #  There might be an empty result
        try:
            df["id"] = df["_id"].astype("str")
        except:
            pass
        return df.drop("_id", axis=1)

    def insert(self, collection, dataframe):
        """
        To insert a pandas dataframe into mongo
        :param collection:  collection name
        :param dataframe:  pandas datafram
        :return:  list of ObjectId inserted
        """
        if not isinstance(dataframe, pd.DataFrame):
            raise TypeError("This function support Pandas dataframe only.")
        data = [row.to_dict() for idx, row in dataframe.iterrows()]
        result = self.db[collection].insert_many(data)
        return result.inserted_ids
