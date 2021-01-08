class User:

    def __init__(self, username, user_id):
        print("new user being created...")    
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    
    def follow(self, user):
        user.followers += 1
        self.following += 1


if __name__ == "__main__":
    user_1 = User(username="Max", user_id="001")
    user_2 = User(username="Nina", user_id="002")

    user_2.follow(user_1)

    print(f"Name: {user_1.username} with id {user_1.id}. Has followers: {user_1.followers} and following {user_1.following}")
    print(f"Name: {user_2.username} with id {user_2.id}. Has followers: {user_2.followers} and following {user_2.following}")
