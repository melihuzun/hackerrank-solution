import requests
import threading


def get_data(year: int) -> int:
    url = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}"
    r = requests.get(url).json()
    total_pages = r["total_pages"]
    return total_pages


def scrape_pages(year: int, page_num: int, lst: list) -> int:
    count = 0
    url = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&page={page_num}"
    r = requests.get(url).json()
    for i in r["data"]:
        if int(i["team1goals"]) == int(i["team2goals"]):
            count += 1
    lst.append(count)
    return count


def get_goals(year: int) -> int:
    ouputlist = []
    pages = get_data(year)
    lock = threading.Lock()
    lock.acquire()
    threads = [
        threading.Thread(target=scrape_pages, args=(year, x, ouputlist))
        for x in range(1, pages + 1)
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return sum(ouputlist)


print(get_goals(2011))
