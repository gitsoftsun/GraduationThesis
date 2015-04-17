class User_CF:
    def __init(self, train, test){
        self.train = train
        self.test = test
    }
    def user_similarity(self):
        """
            计算用户之间相似度
            return： W集合
        """
        U = dict()  #用户之间有交集的集合
        Num = dict()  #和用户有关系的物品number
        # 计算U 和 Num 的代码省略
        # 计算用户之间相似度
        self.W = dict()
        for user,friend in U.items():
            self.W[user] = {}
            for v,count in friend.items():
                self.W[user][v] = count / math.sqrt(Num[user] * Num[v])
        return self.W

    #为用户推荐两个相关物品
    def recommendation(self,user):
        rank = dict()
        relvent_item = self.train[user].keys()     
        for v,similar_value in self.W[user].items():
            for i,rvi in self.train[v].items():
                if i in relvent_item:
                    continue
                rank.setdefault(i,0)
                rank[i] += similar_value * rvi
        return dict(rank.items())