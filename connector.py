# This program will be a mongodb <-> elasticsearch data connnector
from pymongo import *
from elasticsearch import Elasticsearch

# connection to mongodb
def mongodb():
	client = MongoClient('10.238.10.20')
	db = client['Moto']
	collection = db['G5']
	sid = 0 
	for val in collection.find({}):
		rev = val['des']
		elastic(rev,sid)
		print(rev+' '+str(sid))
		sid+=1

def elastic(rev,sid):
	es = Elasticsearch()
	es.index(index = 'moto',doc_type = 'g5', id = sid, body = {'review':rev})
	print('Updated'+' sid')


def main():
	mongodb()

if __name__ == '__main__':
	main()
