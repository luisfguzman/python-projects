from user import User
from post import Post

joe_doe = User("joe@doe.com", "Joe Doe", "password1234", "DevOps Engineer")
joe_doe.get_info()


jane_doe = User("jane@doe.com", "Jane Doe", "god", "HR Recruiter")
jane_doe.get_info()

new_post = Post("developing some software today", joe_doe.name)
new_post.get_info()