from locust import User, task, constant

class MyFirstUser(User):
    
    @task
    def launch(self):
        print("Launching the Url")
        
    @task
    def serach(self):
        print("Searching")

class MySecondUser(User):
    
    @task
    def launch(self):
        print("Launching the Url")
        
    @task
    def serach(self):
        print("Searching")