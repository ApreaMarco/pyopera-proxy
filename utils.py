from base64 import b64encode
from threading import Thread, Event
from time import sleep, time
from contextlib import closing

COPY_BUF = 128 * 1024
WALLCLOCK_PRECISION = 1


def basic_auth_header(login, password):
    return "Basic " + b64encode(f"{login}:{password}".encode()).decode()


def proxy(ctx, left, right):
    def copy_conn(dst, src):
        try:
            with closing(dst), closing(src):
                while True:
                    buf = src.recv(COPY_BUF)
                    if not buf:
                        break
                    dst.sendall(buf)
        finally:
            dst.close()
            src.close()

    t1 = Thread(target=copy_conn, args=(left, right))
    t2 = Thread(target=copy_conn, args=(right, left))
    t1.start()
    t2.start()

    while t1.is_alive() or t2.is_alive():
        if ctx['stop']:
            left.close()
            right.close()
            break
        sleep(0.1)


def copy_header(dst, src):
    for k, v in src.items():
        dst[k] = v


def del_hop_headers(header):
    hop_headers = [
        "Connection", "Keep-Alive", "Proxy-Authenticate", "Proxy-Connection",
        "Te", "Trailers", "Transfer-Encoding", "Upgrade"
    ]
    for h in hop_headers:
        header.pop(h, None)


def copy_body(wr, body):
    buf = bytearray(COPY_BUF)
    while True:
        bread = body.readinto(buf)
        if bread <= 0:
            break
        wr.write(buf[:bread])
        wr.flush()


def after_wall_clock(d):
    deadline = time() + d
    ch = Event()

    def check_time():
        while not ch.is_set():
            if time() >= deadline:
                ch.set()
            sleep(WALLCLOCK_PRECISION)

    Thread(target=check_time).start()
    return ch


def run_ticker(ctx, interval, retry_interval, cb):
    def ticker():
        err = None
        while not ctx['stop']:
            next_interval = interval if err is None else retry_interval
            event = after_wall_clock(next_interval)
            event.wait()
            if ctx['stop']:
                break
            err = cb(ctx)

    Thread(target=ticker).start()
