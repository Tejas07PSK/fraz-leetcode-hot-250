from heapq import heappop, heappush

class Twitter:
    def __init__ (self):
        self.timer = -1
        self.uid_tweet_map = {}
        self.uid_fuid_map = {}

    def postTweet (self, userId: int, tweetId: int) -> None:
        if (userId not in self.uid_tweet_map): self.uid_tweet_map[userId] = [(self.timer, tweetId)]
        else: self.uid_tweet_map[userId].append((self.timer, tweetId))
        if (userId not in self.uid_fuid_map): self.uid_fuid_map[userId] = set()
        self.timer -= 1

    def getNewsFeed (self, userId: int) -> List[int]:
        ans = []
        if (userId in self.uid_tweet_map):
            hp = []
            itr = reversed(self.uid_tweet_map[userId])
            entry_time, item = next(itr, (None, None))
            if (item != None): heappush(hp, (entry_time, item, itr))
            for followeeId in self.uid_fuid_map[userId]:
                itr = reversed(self.uid_tweet_map[followeeId])
                entry_time, item = next(itr, (None, None))
                if (item != None): heappush(hp, (entry_time, item, itr))
            while ((hp) and (len(ans) < 10)):
                entry_time, item, itr = heappop(hp)
                ans.append(item)
                entry_time, item = next(itr, (None, None))
                if (item != None): heappush(hp, (entry_time, item, itr))
        return ans

    def follow (self, followerId: int, followeeId: int) -> None:
        if (followerId not in self.uid_tweet_map): self.uid_tweet_map[followerId] = []
        if (followeeId not in self.uid_tweet_map): self.uid_tweet_map[followeeId] = []
        if (followerId not in self.uid_fuid_map): self.uid_fuid_map[followerId] = set()
        if (followeeId not in self.uid_fuid_map): self.uid_fuid_map[followeeId] = set()
        self.uid_fuid_map[followerId].add(followeeId)

    def unfollow (self, followerId: int, followeeId: int) -> None:
        if (followerId not in self.uid_tweet_map): self.uid_tweet_map[followerId] = []
        if (followeeId not in self.uid_tweet_map): self.uid_tweet_map[followeeId] = []
        if (followerId not in self.uid_fuid_map): self.uid_fuid_map[followerId] = set()
        if (followeeId not in self.uid_fuid_map): self.uid_fuid_map[followeeId] = set()
        self.uid_fuid_map[followerId].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
