from influxdb import InfluxDBClient
from pprint import pprint
import json
import datetime
import random
import socket
import subprocess
import re
import time

HOST="influxdb.influxdb"
PORT=8086
DATABASE="pod-ping-latency-loss"
HOSTNAME=socket.gethostname()
PING_WAIT=2
PING_DST="8.8.8.8"

def send_ping():
    regex = "time=[0-9.]{1,6} ms"
    
    latency = None
    loss = None

    try:
        cmd = "ping -W {} -c {} {}".format(PING_WAIT, 1, PING_DST).split(' ')
        output = subprocess.check_output(cmd).decode().strip()
        lines = output.split("\n")
        
        for line in lines: 
            hit = re.search(regex, line)
            if hit:
                data = re.findall(regex, line)
                latency = re.findall("[0-9]{1,6}", data[0])[0]
                loss = 0

    except Exception as e:
        latency = 0
        loss = 1

    print("latency: {}\nloss: {}".format(latency, loss))
    return (latency, loss)


def insert_data(client, latency, loss):
    data = [
        {
            "measurement": "ping_latency",
            "tags": {
                "host": HOSTNAME,
            },
            "time": datetime.datetime.now().isoformat(),
            "fields": {
                "latency": int(latency),
                "loss": int(loss)
            }
        }
    ]

    client.write_points(data)


if __name__ == "__main__":
    client = InfluxDBClient(host=HOST, port=PORT)
    if DATABASE not in client.get_list_database():
        client.create_database(DATABASE)

    client.switch_database(DATABASE)

    while True:
        (latency, loss) = send_ping()
        if latency is not None or loss is not None:
            insert_data(client, latency, loss)

        time.sleep(5)