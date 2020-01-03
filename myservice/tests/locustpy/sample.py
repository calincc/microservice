from locust import HttpLocust, TaskSet, task


class WebsiteTasks(TaskSet):
    @task
    def index(self):
        self.client.get("/")

    @task
    def hello(self):
        self.client.get("/hello/Calin")


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 100
    max_wait = 1500
