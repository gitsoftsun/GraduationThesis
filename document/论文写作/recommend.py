def Recommend(user, tra, W):
	 rank = dict()
	 interacted_items = tra[user]
	 for v, wuv in sorted(W[u].items, key=itemgetter(1), reverse=True)[0:K]:
		 for i, rvi in tra[v].items:
			 if i in interacted_items:
			 #we should filter items user interacted before
			 continue
		 rank[i] += wuv * rvi
	 return rank