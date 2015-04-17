train = dict()
train['lzy'] = {}
train['lzy']['mac'] = int(99)
train.setdefault('lsr', {})
train['lsr']['car'] = int(88)

print "train['lzy']['mac'] :%s" % train['lzy']['mac']

C = dict()
N = dict()

for user, items in train.items():
	print user, items.keys
	for i in items.keys():
		print i
		# N.setdefault(i,0)
		# print N
        # N[i] += 1
        # C.setdefault(i,{})
        # for j in items.keys():
        #     if i == j : continue
        #     C[i].setdefault(j,0)
        #     C[i][j] += 1
