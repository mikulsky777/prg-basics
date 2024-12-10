class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")
    
    def display_timeline(self):
        print(f'{self.username}\'s posts:')
        counter = 0
        for i in range(len(self.posts)):
            print(f'{counter+1}. {self.posts[counter]}')
            counter += 1


def main():

    user1 = SocialMediaProfile("johndoe")
    user1.add_post("Hello, world!")
    user1.add_post("Had a great day at the park!")
    user1.add_post("What's up, Natalie? How are you?")
    user1.display_timeline()

if __name__ == "__main__":
    main()