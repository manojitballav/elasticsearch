#connecting to the cluster
from elasticsearch import Elasticsearch
es = Elasticsearch()

def insert():
	#index some test data
	res = es.index(index='test-index', doc_type='test', id=3, body={'description': 'Mono is Manojit'})
	print('Data inserted')

def main():
	insert()

if __name__ == '__main__':
	main()