import time
import datetime
import random
def hello() -> str:
    return "Hello from horio!"
def wait(seconds: int) -> None:
    time.sleep(seconds)
def day() -> str:
    return time.strftime("%A", time.localtime())
def month() -> str:
    return time.strftime("%B", time.localtime())
def hour() -> str:
    return time.strftime("%H", time.localtime())
def second() -> str:
    return time.strftime("%S", time.localtime())
def minute() -> str:
    return time.strftime("%M", time.localtime())
def year() -> str:
    return time.strftime("%Y", time.localtime())
def diff(start: float, end: float) -> float:
    return end - start
def print(message: str) -> None:
    print(message)
def now() -> str:
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
def now_unix() -> float:
    return time.time()
def random_date() -> str:
    start_date = datetime.datetime(2000, 1, 1)
    end_date = datetime.datetime.now()
    random_date = start_date + (end_date - start_date) * random.random()
    return random_date.strftime("%Y-%m-%d %H:%M:%S")
def what_day_was(year: int, month: int, day: int) -> str:
    date = datetime.datetime(year, month, day)
    return date.strftime("%A")
def hello_world() -> str:
    return "Hello, World!"
def ms_to_seconds(ms: int) -> float:
    return ms / 1000.0
def seconds_to_ms(seconds: float) -> int:
    return int(seconds * 1000)
def ms_to_nanoseconds(ms: int) -> int:
    return ms * 1_000_000
def nanoseconds_to_ms(ns: int) -> float:
    return ns / 1_000_000.0
def seconds_to_nanoseconds(seconds: float) -> int:
    return int(seconds * 1_000_000_000)
def random_time() -> str:
    random_hour = random.randint(0, 23)
    random_minute = random.randint(0, 59)
    random_second = random.randint(0, 59)
    return f"{random_hour:02d}:{random_minute:02d}:{random_second:02d}"
def random_datetime() -> str:
    random_date_str = random_date()
    random_time_str = random_time()
    return f"{random_date_str} {random_time_str}"
def random_year() -> int:
    return random.randint(2000, datetime.datetime.now().year)
def random_month() -> int:
    return random.randint(1, 12)
def random_day(year: int, month: int) -> int:
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return random.randint(1, 29)
        else:
            return random.randint(1, 28)
    elif month in [4, 6, 9, 11]:
        return random.randint(1, 30)
    else:
        return random.randint(1, 31)
def create_datetime(year: int, month: int, day: int, hour: int = 0, minute: int = 0, second: int = 0) -> str:
    try:
        date = datetime.datetime(year, month, day, hour, minute, second)
        return date.strftime("%Y-%m-%d %H:%M:%S")
    except ValueError as e:
        return f"Invalid date: {e}"


