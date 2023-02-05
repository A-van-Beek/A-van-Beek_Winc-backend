# Do not modify these lines
__winc_id__ = "78029e0e504a49e5b16482a7a23af58c"
__human_name__ = "modules"

# Add your code after this line
import this
import time
import math
import datetime
import platform
import greet


def wait(t: float):
    # print("start")
    time.sleep(t)
    # print("end")


def my_sin(t: float):
    # print(math.sin(t))
    return math.sin(t)


iso_now = datetime.datetime.now().strftime("%G-%m-%dT%H:%M")

platform = platform.system()


def supergreeting_wrapper(name: str):
    return greet.supergreeting(name)


# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    # print(this)
    print(iso_now)
    # my_sin(10)
    print(platform)
    # print(supergreeting_wrapper("Anke"))
    # wait(2)
