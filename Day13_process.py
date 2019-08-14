# 1、without using process
# from random import randint
# from time import time,sleep
#
# def download_task(filename):
#     print('开始下载%s...' % filename)
#     time_to_download = randint(5,10)
#     sleep(time_to_download)
#     print('%s下载完成！耗费了%d秒' % (filename,time_to_download))
#
# def main():
#     start = time()
#     download_task('Python从入门到住院.pdf')
#     download_task('Peking Hot.avi')
#     end = time()
#     print('总共耗费了%.2f秒.' % (end - start))
#
# if __name__ == '__main__':
#     main()

# 2、using process

# from multiprocessing import Process
# from os import getpid
# from random import randint
# from time import time,sleep
#
# def download_task(filename):
#     print('启动下载进程、进程号[%d].' % getpid())
#     print('开始下载%s...' % filename)
#     time_to_downlaod = randint(5,10)
#     sleep(time_to_downlaod)
#     print('%s下载完成！耗费了%d秒' % (filename,time_to_downlaod))
#
# def main():
#     start = time()
#     p1 = Process(target=download_task,args=('python从入门到住院.pdf', ))
#     p1.start()
#     p2 = Process(target=download_task,args=('Peking Hot.avi', ))
#     p2.start()
#     p1.join()
#     p2.join()
#     end = time()
#     print('总共耗费了%.2f秒.' % (end - start))
#
# if __name__ == '__main__':
#     main()

# thread

# from random import randint
# from threading import Thread
# from time import time,sleep
#
# def download(filename):
#     print('开始下载%s...' % filename)
#     time_to_download = randint(5, 10)
#     sleep(time_to_download)
#     print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))
#
# def main():
#     start = time()
#     t1 = Thread(target=download, args=('Python从入门到住院.pdf',))
#     t1.start()
#     t2 = Thread(target=download, args=('Peking Hot.avi',))
#     t2.start()
#     t1.join()
#     t2.join()
#     end = time()
#     print('总共耗费了%.3f秒' % (end - start))
#
#
# if __name__ == '__main__':
#     main()

from random import randint
from threading import Thread
from time import time, sleep


class DownloadTask(Thread):

    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def foo(self):
        print("run!")

    def run(self):
        print('开始下载%s...' % self._filename)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print('%s下载完成! 耗费了%d秒' % (self._filename, time_to_download))


def main():
    start = time()
    t1 = DownloadTask('Python从入门到住院.pdf')
    t1.start()
    t2 = DownloadTask('Peking Hot.avi')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()
