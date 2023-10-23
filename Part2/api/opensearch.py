import requests
import json


class Opensearch:
    def __init__(self, host: str = "http://localhost:5601/", basic_auth: str = "") -> None:
        self.host = host
        self.basic_auth = basic_auth
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Basic {basic_auth}'
        }

    def createIndex(self, name: str):
        try:
            response = requests.request(
                "PUT", self.host+name, headers=self.headers, timeout=10)
            if response.status_code == 200:
                return f"Index: {name} has been created."
            else:
                return response.json()
        except Exception as e:
            return f"Error: {e}"

    def filterUser(self, user: str = "*", pagination: bool = False):
        filter_criteria = ''
        from_size = 0
        if pagination:
            from_size = 10001
        if user != "*":
            filter_criteria = f"where user = '{user}'"
        payload = json.dumps({
            "from": from_size,
            "size": 10000,
            "query": f"select id, user, timestamp, hours, project from dailycheckins {filter_criteria}"
        })
        try:
            response = requests.request(
                "POST", self.host+"_plugins/_sql", headers=self.headers, data=payload)
            data = response.json()["datarows"]
            dataDict = {
                "total_rows": response.json()["total"],
                "rows": []
            }
            for row in data:
                dataDict["rows"].append({
                    "user": row[1],
                    "timestamp": row[2],
                    "hours": row[3],
                    "project": row[4],
                })
            if user != "*":
                return json.dumps(dataDict, indent=4)
            return dataDict

        except Exception as e:
            return f"Error: {e}"

    def getAllIndexData(self, func=None):
        try:
            if func:
                resultset1 = func()
                resultset2 = func(pagination=True)
            return json.dumps({
                "total_rows": resultset1["total_rows"] + resultset2["total_rows"],
                "rows": resultset1["rows"] + resultset2["rows"]
            }, indent=4)
        except Exception as e:
            return f"Error: {e}"

    def bulkInsertion(self, data: str):
        try:
            response = requests.request(
                "POST", self.host+"/_bulk", headers=self.headers, data=data)
            return response.json()

        except Exception as e:
            return f"Error: {e}"
