import requests

class Program:
    def Main(heroes: list = ["Hulk", "Captain America", "Thanos"]): 
        data = {}
        for i in requests.get("https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json").json():
            if (i["name"] in heroes): data[i["name"]] = i["powerstats"]["intelligence"]
        return sorted(data, key=lambda i: data[i], reverse=True)[0]


if (__name__ == "__main__"):
    Program.Main()