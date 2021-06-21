from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import schedule_api, schedule_api2, schedule_api3


def start():
    scheduler = BackgroundScheduler()
    # scheduler.add_job(schedule_api, 'interval', hours=24)
    scheduler.add_job(schedule_api2, 'interval', hours=24)
    scheduler.add_job(schedule_api3, 'interval', hours=24)
    scheduler.start()
