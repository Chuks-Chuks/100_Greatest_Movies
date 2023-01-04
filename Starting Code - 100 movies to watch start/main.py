import requests
from bs4 import BeautifulSoup
import html

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

request = requests.get(url=URL)
movies_web_page = request.text

soup = BeautifulSoup(movies_web_page, 'html.parser')

movies_100 = soup.find_all(name="h3", class_="title")
movies_titles_numbers = [movie.getText() for movie in movies_100]

re_arranged_list = [movies_titles_numbers[movie * - 1] for movie in range(1, len(movies_titles_numbers))]
re_arranged_list.append(movies_titles_numbers[0])
print(re_arranged_list)
with open("Greatest Movies of All Time.txt", "a", encoding="utf-8") as GOAT_movies:
    for message in re_arranged_list:
        file = GOAT_movies.write(html.unescape(f"{message}\n"))

