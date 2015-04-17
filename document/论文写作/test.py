import graphlab as gl
train_data = gl.SFrame.read_csv(traindata_path,header=True, delimiter='\t',\
	quote_char='"', column_type_hints = {'id':str, 'sentiment' : int, 'review':str } )
train_data['1grams features'] = gl.text_analytics.count_ngrams(train_data['review'],1)
train_data['2grams features'] = gl.text_analytics.count_ngrams(train_data['review'],2)
cls = gl.classifier.create(train_data, target='sentiment', features=['1grams features','2grams features'])