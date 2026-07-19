import requests

BASE_URL="https://student-digital-brain-production.up.railway.app"

def signup(data):
    return requests.post(f"{BASE_URL}/users/signup",json=data)

def login(data):
    return requests.post(f"{BASE_URL}/users/login",json=data)

def dashboard():
    return requests.get(f"{BASE_URL}/dashboard/")

def add_task(data):
    return requests.post(f"{BASE_URL}/tasks/add",json=data)

def get_tasks():
    return requests.get(f"{BASE_URL}/tasks/")

def complete_task(task_id):
    return requests.put(f"{BASE_URL}/tasks/complete/{task_id}")

def delete_task(task_id):
    return requests.delete(f"{BASE_URL}/tasks/{task_id}")

def recommend(data):
    return requests.post(
        f"{BASE_URL}/recommend/",
        json=data
    )