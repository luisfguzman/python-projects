class User:
    def __init__(self, email, name, password, job_title):
        self.email = email
        self.name = name
        self.password = password
        self.job_title = job_title

    def change_email(self, new_email):
        self.email = new_email

    def change_name(self, new_name):
        self.name = new_name

    def change_password(self, new_password):
        self.password = new_password
    
    def change_job_title(self, new_job_title):
        self.job_title = new_job_title

    def get_info(self):
        print(f"User {self.name} currently works as a {self.job_title}. You can contact them at {self.email}")