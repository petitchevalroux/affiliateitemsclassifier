import os
import json
import HTMLParser
import re
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import metrics
import numpy
from sklearn.grid_search import GridSearchCV
import operator
from random import shuffle

base_path = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base_path, "data")

# Load json data
file_path = os.path.join(data_dir, "products_items.json")
json_data = open(file_path)
data = json.load(json_data)
json_data.close()

class Decoder:
	parser = HTMLParser.HTMLParser()
	# Recursively decode html entities
	def decode(self, str):
		s = self.parser.unescape(str)
		if re.search("&[^\s]*;", s):
			s = self.decode(s)

		return s

decoder = Decoder()
# Contain documents
documents = []
# Contain document's categories
documents_categories = []
# Contain categories label
categories = []
# Dictionnary hash for translating product identifier to product name
products = {}

shuffle(data)
for value in data:
	documents.append(decoder.decode(value["ITM_TITLE"]))
	documents_categories.append(value['PRD_ID'])
	if not products.has_key(value['PRD_ID']) :
		products[value['PRD_ID']] = decoder.decode(value['PRD_NAME'])

clf = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                      ('clf', SGDClassifier())
                      ])
clf.fit(documents, documents_categories)

test_docs = documents
predicted = clf.predict(test_docs)
# Prediction success rate
print 'Success rate:', numpy.mean(predicted == documents_categories)

for s, p in zip(documents[:10], predicted[:10]):
    print('Item "%s" classified as product "%s"' % (s, products[p]))