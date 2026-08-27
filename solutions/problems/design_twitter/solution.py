import heapq

class Twitter:

    def __init__(self):
        self.tweets = {}
        self.followers = {}
        self.following = {}
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.setdefault(userId, []).append((self.timestamp, tweetId))
        self.timestamp += 1
        
    def getNewsFeed(self, userId: int) -> List[int]:

        myTweets = self.tweets.get(userId, [])

        tweets = myTweets[:]
        
        for id in self.following.get(userId, []):
            for tweet in self.tweets.get(id, []):
                tweets.append(tweet)
        
        heap = [(-n[0], n[1]) for n in tweets]

        heapq.heapify(heap)

        news = []

        i = 0
        while len(heap) > 0 and i < 10:
            t = heapq.heappop(heap)
            news.append(t[1])
            i += 1

        return news

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers.setdefault(followeeId, set()).add(followerId)
        self.following.setdefault(followerId, set()).add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers.get(followeeId, set()).discard(followerId)
        self.following.get(followerId, set()).discard(followeeId)