import requests
import selectorlib
import time
import sqlite3

URL = "https://programmer100.pythonanywhere.com/"
HEADERS =  {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/'
                  '537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

connection = sqlite3.connect('weather.db')
cursor = connection.cursor()

def scrape(url):
    response = requests.get(url, headers=HEADERS)
    text = response.text
    return text

def extract(text):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(text)['temperature']
    return value

def write(temp, datetime):
    cursor.execute("INSERT INTO temperature VALUES (?, ?) ", (datetime, temp))
    connection.commit()


if __name__ == "__main__":
    while True:
        result = extract(scrape(URL))
        temperature = result
        date = time.strftime("%y-%m-%d-%H-%M-%S")
        write(temperature, date)