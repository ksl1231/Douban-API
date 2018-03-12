import requests as r
import json
from my_spider import get_html

#获取网页模板
def get_url_content(url):
	headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"}
	obj = r.get(url,headers=headers,timeout=5)
	content = obj.text
	return content

#获取电影主要信息
def get_movie_subject(movie_id):
	head_url = 'https://api.douban.com/v2/movie/'
	subject_url = head_url + 'subject/' + movie_id
	content = get_url_content(subject_url).encode('utf-8').decode('unicode_escape') #解决乱码问题
	print(content)


if __name__ == '__main__':
	movie_id = '6390825'
	get_movie_subject(movie_id)
