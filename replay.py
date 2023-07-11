import signal
import sys
import argparse
import time
import re
from collections import namedtuple

from pythonosc import udp_client

Message = namedtuple("Message", "time, address, value")

search = r"(\d{2}:\d{2}:\d{2})\.(\d{3}).*ADDRESS\((\/avatar[a-zA-Z0-9/]+)\).*FLOAT\(([0-9.-]+)\)"

def parse_line(line):
    match = re.search(search, line)
    if match is None:
        return None
    
    time_raw = match.group(1)
    milliseconds = match.group(2)
    address = match.group(3)
    value_raw = match.group(4)

    t = time.strptime(time_raw, "%H:%M:%S")
    timestamp = (t.tm_hour * 3600 + t.tm_min * 60 + t.tm_sec) * 1000 + int(milliseconds)
    return Message(time=timestamp, address=address, value=float(value_raw))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str)
    parser.add_argument("--port", type=int, default=9000)
    parser.add_argument("--ip", type=str, default="127.0.0.1")
    args = parser.parse_args()

    osc = udp_client.SimpleUDPClient(args.ip, args.port)

    time_diff = None

    with open(args.file, "+r") as fp:
        line = "a"
        while True:
            line = fp.readline()
            if line == "":
                break
            msg = parse_line(line)

            if msg is None:
                continue

            if time_diff is None:
                time_diff = time.time() * 1000 - msg.time

            time_until = msg.time + time_diff - (time.time() * 1000.0)
            if time_until > 0:
                time.sleep(time_until / 1000.0)

            osc.send_message(msg.address, msg.value)


if __name__ == "__main__":
    main()