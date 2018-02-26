# make sure ES is up and running
import requests

def status_check():
	res = requests.get('http://localhost:9200')
	# This statement prints the content of the webpage
	# print(res.content) 

	sc = res.status_code
	if sc == 200:
		print("ElasticSearch server is up and running")
	else:
		print('ElasticSearch server is down')
	return 0


def main():
	status_check()

if __name__ == '__main__':
	main()