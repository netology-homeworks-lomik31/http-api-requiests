import requests

class Disk:
    def __init__(self, token: str) -> None:
        self.token = token

    def _GetUploadLink(self, diskPath) -> str:
        headers = {
            "Accept": "application/json",
            "Authorization": f"OAuth {self.token}"
        }
        params = {"path": diskPath}
        return requests.get("https://cloud-api.yandex.net/v1/disk/resources/upload", headers=headers, params=params).json()

    def UploadFile(self, diskPath, filePath):
        href = self._GetUploadLink(diskPath=diskPath).get("href", "")
        response = requests.put(href, data=open(filePath, "r"))
        return response

class Program:
    def Main():
        Disk("TOKEN").UploadFile

if (__name__ == "__main__"):
    Program.Main()