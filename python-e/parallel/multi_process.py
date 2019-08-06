"""
多进程
"""
import time
import multiprocessing as mp


def job(a, b):
    for index in range(10):
        print('子进程', index)
        time.sleep(1)


if __name__ == '__main__':
    p1 = mp.Process(target=job, args=(1, 2))
    p1.start()
    print('子进程启动完毕')
    p1.join()
    time.sleep(10)
