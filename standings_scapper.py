import requests
from bs4 import BeautifulSoup

def standings_scapper(SCRAPPING_URL):
    result = requests.get(SCRAPPING_URL).text
    doc = BeautifulSoup(result, "html.parser")
    table = doc.select(".table tbody tr")

    standings = []

    for pos, row in enumerate(table):
        fullname = row.select("td")[1].select("span")[1].text
        shortname = row.select("td")[1].select("span")[2].text
        played = row.select("td")[2].text
        won = row.select("td")[3].text
        lost = row.select("td")[4].text
        nr = row.select("td")[5].text
        tied = row.select("td")[6].text
        netrr = row.select("td")[7].text
        points = row.select("td")[8].text

        standings_row = {
            "pos" : str(pos+1),
            "fullname" : fullname,
            "shortname" : shortname,
            "played" : played,
            "won" : won,
            "lost" : lost,
            "nr" : nr,
            "tied" : tied,
            "netrr" : netrr,
            "points" : points
        }
        standings.append(standings_row)

    return standings