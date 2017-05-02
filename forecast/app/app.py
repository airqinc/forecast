import pandas as pd
import numpy as np
import requests
import sched
import time

def predict(req, sch):
    #requests.get(req)
    #diagnosed_data = pd.read_json()
    #diagnosed_data = pd.get_dummies(diagnosed_data, columns=["DayName","WindDirection"])
    print("Hello")
    scheduler.enter(delay, priority, predict, (req, sch,))

if __name__ == '__main__':
    delay = 5
    priority = 1
    requestDir = ""
    scheduler = sched.scheduler(time.time, time.sleep)
    predict(requestDir, scheduler)
    scheduler.run()
