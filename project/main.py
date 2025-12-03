from data_processing import web_fetcher, file_reader
# from project.data_processing import file_reader

data = file_reader.read_data("data.txt")
print(data)

username =web_fetcher.fetch_user_data()
print(username)