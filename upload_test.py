import requests

url = "http://httpbin.org/post" # Адрес загрузки файла на сервер ВКонтакте
file_path = "C:\Skypro\my_coursework2\data\music\hvatit-jeto-terpet.mp3"
response = requests.post(url, files={"audio": open(file_path, 'rb')})
json_response = response.json()
audio = json_response['files']['audio']