import requests
from bs4 import BeautifulSoup
import csv

def get_row_data(rows):
    out = []
    for row in rows:
        curr = []
        for td in row.find_all(["th", "td"]):
            try:
                td = td.text
            except:
                td = ""
            curr.append(td)

        out.append(curr)

    return out

def write_file(name, contents):
    f = open(name, 'w')
    f.write(str(contents))
    f.close()
    print(name + " written successfully")

if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions_per_capita#cite_note-5"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")

    tables = soup.find_all("table", class_="wikitable")
    co2_per_capita = tables[0].find("tbody").find_all("tr")
    header = get_row_data((co2_per_capita[0],))
    data = get_row_data(co2_per_capita[1:])

    write_file("header.tsv", header)
    write_file("data.tsv", data)
