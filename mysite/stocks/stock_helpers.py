import requests
import os

api_key = os.environ["API_KEY"]

def get_data():
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

def get_exchange_rate(from_currency:str, to_currency:list) -> str:
    table = ""
    for currency in to_currency:
        url =  f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={currency}&apikey={api_key}"
        response = requests.get(url)
        data = response.json()
        exchange_rate = data['Realtime Currency Exchange Rate']['5. Exchange Rate']
        currency = data['Realtime Currency Exchange Rate']['2. From_Currency Name']
        destination_currency = data['Realtime Currency Exchange Rate']['3. To_Currency Code']
        last_refreshed = data['Realtime Currency Exchange Rate']['6. Last Refreshed']
        table += f"<tr> <td>{exchange_rate} </td> <td> {currency}</td> <td>{destination_currency}</td> <td>{last_refreshed}</td></tr>"
        print(data)
    print(table)
    return(table)


# def get_data():
#     url = "https://en.wikipedia.org/wiki/List_of_top_Premier_League_goal_scorers_by_season"
#     response= requests.get(url)  
#     return str(response)


# def loop_table():

#     url = "https://en.wikipedia.org/wiki/List_of_top_Premier_League_goal_scorers_by_season"


# f = open("helloo.html", "w")
# f.write(str(response.content))
# f.close()

# with open("helloo.html", "r") as file:
#     html_data = file.read()


# from bs4 import BeautifulSoup

# soup = BeautifulSoup(html_data)
# tables = soup.findAll("table") # this returns a list of tables
# matching_string = "Les Ferdinand"

# results = []
# for table in tables:
#     if matching_string in str(table):
#         results.append(table)
#         print(table)


# new_list = []
# new_var = "Mark Robins"
# for table in results:
#     if new_var in str(table):
#         new_list.append(table)
#         print(table)


# target_table.find('tbody')
# rows = target_table.find_all('tr')

# results = ""
# for row in rows:
#     cells = row.find_all("td")
#     for cell in cells:
#         cell_text = cell.get_text().replace('\\n', '')
#         results += f"{cell_text},"
#     results += "\n"