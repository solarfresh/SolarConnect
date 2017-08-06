from solarconnect.google.analytic import GoogleAnalytics
from solarconnect.google.map import GoogleMap
from solarconnect.maxmind import MaxMind
from solarconnect.mongodb import MongoConnector
from solarconnect.sql import SQLConnector
from os import path, environ

BASE_DIR = path.dirname(path.abspath(__file__))

schema_demo_mysql = SQLConnector('mysql',
                           user='demo',
                           passwd='demo',
                           host='localhost',
                           port='3306',
                           db='demo')

schema_demo_mongo = MongoConnector(host='localhost', port=27017, db='demo')

geo_lite = {
    "city_path": BASE_DIR + "/etc/geo_lite/GeoLite2-City.mmdb",
    "country_path": BASE_DIR + "/etc/geo_lite/GeoLite2-Country.mmdb"
}
geo_lite_city = MaxMind(geo_lite.get('city_path'))
geo_lite_country = MaxMind(geo_lite.get('country_path'))

# google_analytic = GoogleAnalytics("XXXX@XXX",
#                                   BASE_DIR + "/etc/private_keys/XXX.p12")
#
# google_map = GoogleMap(api_key="XXXXXXX")