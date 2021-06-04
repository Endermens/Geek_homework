import requests


link = "https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs"
response = requests.get(link).text
rep1 = open("ip_it.txt", "w+", encoding = 'utf-8')
rep1.writelines(response)
rep1.close()

with open("ip_it.txt", "r", encoding = "utf-8") as f:
    content = ((line.split()[0], line.split()[5][1:], line.split()[6]) for line in f)
    for i in content:
        print(i)
