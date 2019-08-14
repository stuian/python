from threading import Thread
import requests

class DownloadHanlder(Thread):
    def __init__(self,url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(self.url)
        with open(filename,'wb') as f:
            f.write(resp.content) # 图片所以用wb模式
def main():
    resp = requests.get('http://api.tianapi.com/meinv/?key=APIKey&num=10')
    data_model = resp.json()
    for mm_dict in data_model['newslist']:
        url = mm_dict['picUrl']
        DownloadHanlder(url).start()  # 用多线程的方式下载图片

if __name__ == '__main__':
    main()