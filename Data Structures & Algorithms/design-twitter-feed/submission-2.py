from collections import *
Post = namedtuple('Post', ['userId', 'tweetId'])
class Twitter:

    def __init__(self):
        self.posts = deque()
        self.followmap = defaultdict(set) #userId:{userId}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts.appendleft(Post(userId, tweetId))
        print(self.posts)

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        print(self.followmap)
        for post in self.posts:
            if post.userId in self.followmap[userId] or post.userId == userId:
                feed.append(post.tweetId)
            if len(feed) == 10:
                break
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].discard(followeeId)
