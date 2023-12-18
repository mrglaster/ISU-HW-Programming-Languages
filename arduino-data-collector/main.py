import logging
import time

import zmq
import csv
import datetime

available_keys = ['p', 'm', 't']

logging.basicConfig(filename='receiver.log', level=logging.CRITICAL)
logger = logging.getLogger()


def write_log(message):
    logging.critical(f"{datetime.datetime.utcnow()} : {message}")


def write_record(current_time, tag, value):
    with open('data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter='\t', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([current_time, tag, value])


def main():
    timeout_ms = 5000
    ctx = zmq.Context()
    clt = ctx.socket(zmq.SUB)
    try:
        clt.connect("tcp://192.168.0.102:5555")
        clt.subscribe('')
    except:
        write_log(f"Unable to connect to server")
        main()

    poller = zmq.Poller()
    poller.register(clt, zmq.POLLIN)

    try:
        while True:
            socks = dict(poller.poll(timeout=timeout_ms))
            if clt in socks and socks[clt] == zmq.POLLIN:
                try:
                    message = clt.recv_string()
                    current_time = datetime.datetime.utcnow()
                    print(message)
                    if len(message):
                        if len(message) == 1 and message not in available_keys:
                            write_log(f"Unknown tag: {message}")
                        elif len(message) == 1:
                            write_record(current_time, message, 'True')
                        else:
                            values_got = message.split(' ')
                            if values_got[0] not in available_keys:
                                write_log(f"Unknown tag: {values_got[0]}")
                            else:
                                write_record(current_time, values_got[0], values_got[1])
                    else:
                        write_log(f"Message with length 0 received")
                except zmq.error.Again:
                    write_log(f"Timeout while receiving message")
                except:
                    write_log(f"It seems arduino is disconnected!")
                    time.sleep(5)
            else:
                write_log(f"No connection to device. Retrying...")
                main()
    except KeyboardInterrupt:
        write_log(f"Keyboard Interrupt. Exiting...")


if __name__ == '__main__':
    main()
