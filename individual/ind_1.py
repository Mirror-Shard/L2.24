#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from queue import Queue
from threading import Lock, Thread

"""
Условие задачи:
    * В качестве потребителя: Работник, пришедший на собеседование
    * В качестве производителя: Руководитель, принимающий работников на работу
"""


def producer(ls):
    lock.acquire()
    ls = ls
    for i in range(6):
        idx = random.randint(0, 3)
        exp = random.randint(1, 1000)
        q.put([ls[idx], exp])
    lock.release()


def consumer():
    lock.acquire()
    ls = []
    while not q.empty():
        s = q.get()
        r = random.choice(["Не подходит",
                           "Необходима стажировка",
                           "Принят"])
        print(f"Работник с id: {s[1]} "
              f"На должность: {s[0]}, "
              f"Результат: {r}")
        ls.append(
            {
                "id": s[1],
                "Должность": s[0],
                "Результат": r
            }
        )
    for i in ls:
        if i["Результат"] == "Принят":
            print(f"Работник с id {i['id']} принят на работу")
    lock.release()


if __name__ == "__main__":
    ls = ['рабочих и служащих без профессионального образования',
          'руководящие должности',
          'специальности, для которых нужно высшее образование',
          'непроизводственный персонал']
    lock = Lock()
    q = Queue()
    q2 = Queue()
    th1 = Thread(target=producer(ls)).start()
    th2 = Thread(target=consumer()).start()
