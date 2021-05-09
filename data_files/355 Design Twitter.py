
from collections import defaultdict
import heapq

__author__ = 'Daniel'


SZ = 10


class Tweet(object):
    central_clk = 0

    def __init__(self, id, nxt=None):
        self.timestamp = Tweet.central_clk
        self.id = id
        self.next = nxt  
        Tweet.central_clk += 1

    def __cmp__(self, other):
        return - (self.timestamp - other.timestamp)


class Twitter(object):
    
    def __init__(self):
        
        self.tweets = defaultdict(lambda: None)
        self.followees = defaultdict(set)

    def postTweet(self, userId, tweetId):
        
        nxt = self.tweets[userId]  
        self.tweets[userId] = Tweet(tweetId, nxt)

    def getNewsFeed(self, userId):
        
        h = []
        if userId not in self.followees[userId] and self.tweets[userId]:
            
            heapq.heappush(h, self.tweets[userId])

        for followee in self.followees[userId]:
            if self.tweets[followee]:
                heapq.heappush(h, self.tweets[followee])

        ret = []
        while h and len(ret) < SZ:
            tweet = heapq.heappop(h)
            ret.append(tweet.id)
            if tweet.next:
                heapq.heappush(h, tweet.next)

        return ret

    def follow(self, followerId, followeeId):
        
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        
        self.followees[followerId].discard(followeeId)  










if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""t""w""i""t""t""e""r"" ""="" ""T""w""i""t""t""e""r""("")""
"" "" "" "" ""t""w""i""t""t""e""r"".""p""o""s""t""T""w""e""e""t""(""1"","" ""5"")""
"" "" "" "" ""t""w""i""t""t""e""r"".""u""n""f""o""l""l""o""w""(""1"","" ""1"")""
