
import configparser
from utilities.data_cleaner import date_cleaner
from api.opensearch import Opensearch

data = date_cleaner("./input/dailycheckins.csv")
config = configparser.ConfigParser()
config.read("./configs/opensearch_config.ini")
conn = Opensearch(host=config["AWS"]["host"],
                  basic_auth=config["AWS"]["basic_auth"])
payload = ""

for index, row in data.iterrows():
    id = index+1
    payload += f"{{ \"create\": {{ \"_index\": \"dailycheckins\" }} }} \r\n{{ \"user\": \"{row['user']}\", \"timestamp\": \"{row['timestamp_dt']}\", \"hours\": \"{row['hours']}\", \"project\": \"{row['project']}\"}}\r\n\r\n"


response = conn.bulkInsertion(payload)

print(response)
