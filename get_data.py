#connecting to the cluster
from elasticsearch import Elasticsearch
es = Elasticsearch()

def get_d():
	# getting the data from es
	res =es.get(index='test-index', doc_type='test', id=1)
	val = res['_source']
	print(val['description'])

def main():
	get_d()

if __name__ == '__main__':
	main()