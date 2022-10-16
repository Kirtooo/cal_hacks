import requests
response = requests.get('https://classes.berkeley.edu/content/2022-Fall-compsci-161-001-lec-001')
print("文本编码：",response.encoding)
print("响应状态码", response.status_code)
print("字符串形式的响应体：", response.text)