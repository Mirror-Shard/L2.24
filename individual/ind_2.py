#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from threading import Lock, Thread
from queue import Queue


def func_1(x=0.5):
    lock.acquire()
    EPS = 1e-07
    n, s, m, curr = 0, 0, 0, 0
    while True:
        pre = math.pow(x, 2*n) / math.factorial(2*n)
        n += 1
        curr = math.pow(x, 2*n) / math.factorial(2*n)
        if abs(curr - pre) < EPS:
            break
        s += curr
        q.put(s)
    lock.release()


def func_2():
    x = q.get()
    result = (math.exp(x) + math.exp(-x)) / 2
    print(result)


if __name__ == "__main__":
    q = Queue()
    lock = Lock()
    th1 = Thread(target=func_1).start()
    th2 = Thread(target=func_2).start()
