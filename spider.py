import time
import requests
from lxml import etree
import pymysql


class Spider:
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/108.0.0.0 Safari/537.36 "
    }

    def create(self):
        # 须修改为自己数据库的账号密码，运行代码前必须在自己环境的MySQL中先建一个1905的数据库，字符集选utf8，排序规则为utf8_unicode_ci
        db = pymysql.connect(host='localhost', user='root', password='123456', database='1905')  # 连接数据库
        cursor = db.cursor()
        cursor.execute("DROP TABLE IF EXISTS dongzuo")
        sql = """ CREATE TABLE dongzuo (
                  id INT AUTO_INCREMENT PRIMARY KEY,
                  name VARCHAR(255) NOT NULL,
                  score FLOAT NOT NULL,
                  url VARCHAR(255) NOT NULL,
                  details TEXT NOT NULL
                );
                """
        cursor.execute(sql)
        cursor.execute("DROP TABLE IF EXISTS aiqing")
        sql = """ CREATE TABLE aiqing (
                          id INT AUTO_INCREMENT PRIMARY KEY,
                  name VARCHAR(255) NOT NULL,
                          score FLOAT NOT NULL,
                          url VARCHAR(255) NOT NULL,
                          details TEXT NOT NULL
                        );
                        """
        cursor.execute(sql)
        cursor.execute("DROP TABLE IF EXISTS ertong")
        sql = """ CREATE TABLE ertong (
                          id INT AUTO_INCREMENT PRIMARY KEY,
                  name VARCHAR(255) NOT NULL,
                          score FLOAT NOT NULL,
                          url VARCHAR(255) NOT NULL,
                          details TEXT NOT NULL
                        );
                        """
        cursor.execute(sql)
        cursor.execute("DROP TABLE IF EXISTS lishi")
        sql = """ CREATE TABLE lishi (
                          id INT AUTO_INCREMENT PRIMARY KEY,
                  name VARCHAR(255) NOT NULL,
                          score FLOAT NOT NULL,
                          url VARCHAR(255) NOT NULL,
                          details TEXT NOT NULL
                        );
                        """
        cursor.execute(sql)
        cursor.execute("DROP TABLE IF EXISTS xiju")
        sql = """ CREATE TABLE xiju (
                          id INT AUTO_INCREMENT PRIMARY KEY,
                  name VARCHAR(255) NOT NULL,
                          score FLOAT NOT NULL,
                          url VARCHAR(255) NOT NULL,
                          details TEXT NOT NULL
                        );
                        """
        cursor.execute(sql)
        cursor.execute("DROP TABLE IF EXISTS xuanyi")
        sql = """ CREATE TABLE xuanyi (
                          id INT AUTO_INCREMENT PRIMARY KEY,
                  name VARCHAR(255) NOT NULL,
                          score FLOAT NOT NULL,
                          url VARCHAR(255) NOT NULL,
                          details TEXT NOT NULL
                        );
                        """
        cursor.execute(sql)
        cursor.execute("DROP TABLE IF EXISTS jiating")
        sql = """ CREATE TABLE jiating (
                          id INT AUTO_INCREMENT PRIMARY KEY,
                  name VARCHAR(255) NOT NULL,
                          score FLOAT NOT NULL,
                          url VARCHAR(255) NOT NULL,
                          details TEXT NOT NULL
                        );
                        """
        cursor.execute(sql)
        cursor.execute("DROP TABLE IF EXISTS neidi")
        sql = """ CREATE TABLE neidi (
                          id INT AUTO_INCREMENT PRIMARY KEY,
                  name VARCHAR(255) NOT NULL,
                          score FLOAT NOT NULL,
                          url VARCHAR(255) NOT NULL,
                          details TEXT NOT NULL
                        );
                        """
        cursor.execute(sql)
        db.close()

    def dongzuopian(self):
        # 须修改为自己数据库的账号密码
        db = pymysql.connect(host='localhost', user='root', password='123456', database='1905')
        cursor = db.cursor()
        for i in range(1, 21):
            html = requests.get('https://www.1905.com/vod/list/n_1_t_5/o3p' + str(i) + '.html', headers=self.header)
            tree = etree.HTML(html.text)
            a = tree.xpath("//section[@class='mod row search-list']/div[@class='grid-2x grid-3x-md grid-6x-sm']")
            for n in a:
                title = ''.join(n.xpath(".//img/@alt"))
                link = ''.join(n.xpath(".//a/@href"))
                detail = ''.join(n.xpath(".//p//text()"))
                score = ''.join(n.xpath(".//i//text()"))
                cursor.execute("insert into dongzuo(name, score, url, details) values( %s, %s, %s, %s)",
                               [title, score, link, detail])
            print("第" + str(i) + "页爬取完毕")
            # 避免访问服务器过于频繁，每次访问等待1s
            time.sleep(2)
        db.commit()
        db.close()

    def aiqingpian(self):
        # 须修改为自己数据库的账号密码
        db = pymysql.connect(host='localhost', user='root', password='123456', database='1905')
        cursor = db.cursor()
        for i in range(1, 21):
            html = requests.get('https://www.1905.com/vod/list/n_1_t_1/o3p' + str(i) + '.html', headers=self.header)
            tree = etree.HTML(html.text)
            a = tree.xpath("//section[@class='mod row search-list']/div[@class='grid-2x grid-3x-md grid-6x-sm']")
            for n in a:
                title = ''.join(n.xpath(".//img/@alt"))
                link = ''.join(n.xpath(".//a/@href"))
                detail = ''.join(n.xpath(".//p//text()"))
                score = ''.join(n.xpath(".//i//text()"))
                cursor.execute("insert into aiqing(name, score, url, details) values( %s, %s, %s, %s)",
                               [title, score, link, detail])
            print("第" + str(i) + "页爬取完毕")
            # 避免访问服务器过于频繁，每次访问等待1s
            time.sleep(2)
        db.commit()
        db.close()

    def xijupian(self):
        # 须修改为自己数据库的账号密码
        db = pymysql.connect(host='localhost', user='root', password='123456', database='1905')
        cursor = db.cursor()
        for i in range(1, 21):
            html = requests.get('https://www.1905.com/vod/list/n_1_t_25/o3p' + str(i) + '.html', headers=self.header)
            tree = etree.HTML(html.text)
            a = tree.xpath("//section[@class='mod row search-list']/div[@class='grid-2x grid-3x-md grid-6x-sm']")
            for n in a:
                title = ''.join(n.xpath(".//img/@alt"))
                link = ''.join(n.xpath(".//a/@href"))
                detail = ''.join(n.xpath(".//p//text()"))
                score = ''.join(n.xpath(".//i//text()"))
                cursor.execute("insert into xiju(name, score, url, details) values( %s, %s, %s, %s)",
                               [title, score, link, detail])
            print("第" + str(i) + "页爬取完毕")
            # 避免访问服务器过于频繁，每次访问等待1s
            time.sleep(2)
        db.commit()
        db.close()

    def xuanyipian(self):
        # 须修改为自己数据库的账号密码
        db = pymysql.connect(host='localhost', user='root', password='123456', database='1905')
        cursor = db.cursor()
        for i in range(1, 21):
            html = requests.get('https://www.1905.com/vod/list/n_1_t_27/o3p' + str(i) + '.html', headers=self.header)
            tree = etree.HTML(html.text)
            a = tree.xpath("//section[@class='mod row search-list']/div[@class='grid-2x grid-3x-md grid-6x-sm']")
            for n in a:
                title = ''.join(n.xpath(".//img/@alt"))
                link = ''.join(n.xpath(".//a/@href"))
                detail = ''.join(n.xpath(".//p//text()"))
                score = ''.join(n.xpath(".//i//text()"))
                cursor.execute("insert into xuanyi(name, score, url, details) values( %s, %s, %s, %s)",
                               [title, score, link, detail])
            print("第" + str(i) + "页爬取完毕")
            # 避免访问服务器过于频繁，每次访问等待1s
            time.sleep(2)
        db.commit()
        db.close()

    def lishipian(self):
        # 须修改为自己数据库的账号密码
        db = pymysql.connect(host='localhost', user='root', password='123456', database='1905')
        cursor = db.cursor()
        for i in range(1, 21):
            html = requests.get('https://www.1905.com/vod/list/n_1_t_18/o3p' + str(i) + '.html', headers=self.header)
            tree = etree.HTML(html.text)
            a = tree.xpath("//section[@class='mod row search-list']/div[@class='grid-2x grid-3x-md grid-6x-sm']")
            for n in a:
                title = ''.join(n.xpath(".//img/@alt"))
                link = ''.join(n.xpath(".//a/@href"))
                detail = ''.join(n.xpath(".//p//text()"))
                score = ''.join(n.xpath(".//i//text()"))
                cursor.execute("insert into lishi(name, score, url, details) values( %s, %s, %s, %s)",
                               [title, score, link, detail])
            print("第" + str(i) + "页爬取完毕")
            # 避免访问服务器过于频繁，每次访问等待1s
            time.sleep(2)
        db.commit()
        db.close()

    def jiatingpian(self):
        # 须修改为自己数据库的账号密码
        db = pymysql.connect(host='localhost', user='root', password='123456', database='1905')
        cursor = db.cursor()
        for i in range(1, 21):
            html = requests.get('https://www.1905.com/vod/list/n_1_t_13/o3p' + str(i) + '.html', headers=self.header)
            tree = etree.HTML(html.text)
            a = tree.xpath("//section[@class='mod row search-list']/div[@class='grid-2x grid-3x-md grid-6x-sm']")
            for n in a:
                title = ''.join(n.xpath(".//img/@alt"))
                link = ''.join(n.xpath(".//a/@href"))
                detail = ''.join(n.xpath(".//p//text()"))
                score = ''.join(n.xpath(".//i//text()"))
                cursor.execute("insert into jiating(name, score, url, details) values( %s, %s, %s, %s)",
                               [title, score, link, detail])
            print("第" + str(i) + "页爬取完毕")
            # 避免访问服务器过于频繁，每次访问等待1s
            time.sleep(2)
        db.commit()
        db.close()

    def ertongpian(self):
        # 须修改为自己数据库的账号密码
        db = pymysql.connect(host='localhost', user='root', password='123456', database='1905')
        cursor = db.cursor()
        for i in range(1, 19):
            html = requests.get('https://www.1905.com/vod/list/n_1_t_7/o3p' + str(i) + '.html', headers=self.header)
            tree = etree.HTML(html.text)
            a = tree.xpath("//section[@class='mod row search-list']/div[@class='grid-2x grid-3x-md grid-6x-sm']")
            for n in a:
                title = ''.join(n.xpath(".//img/@alt"))
                link = ''.join(n.xpath(".//a/@href"))
                detail = ''.join(n.xpath(".//p//text()"))
                score = ''.join(n.xpath(".//i//text()"))
                cursor.execute("insert into ertong(name, score, url, details) values( %s, %s, %s, %s)",
                               [title, score, link, detail])
            print("第" + str(i) + "页爬取完毕")
            # 避免访问服务器过于频繁，每次访问等待1s
            time.sleep(2)
        db.commit()
        db.close()

    def neidipian(self):
        # 须修改为自己数据库的账号密码
        db = pymysql.connect(host='localhost', user='root', password='123456', database='1905')
        cursor = db.cursor()
        for i in range(1, 19):
            html = requests.get('https://www.1905.com/vod/list/n_1_a_1/o3p' + str(i) + '.html', headers=self.header)
            tree = etree.HTML(html.text)
            a = tree.xpath("//section[@class='mod row search-list']/div[@class='grid-2x grid-3x-md grid-6x-sm']")
            for n in a:
                title = ''.join(n.xpath(".//img/@alt"))
                link = ''.join(n.xpath(".//a/@href"))
                detail = ''.join(n.xpath(".//p//text()"))
                score = ''.join(n.xpath(".//i//text()"))
                cursor.execute("insert into neidi(name, score, url, details) values( %s, %s, %s, %s)",
                               [title, score, link, detail])
            print("第" + str(i) + "页爬取完毕")
            # 避免访问服务器过于频繁，每次访问等待1s
            time.sleep(2)
        db.commit()
        db.close()

    def run(self):  # 实现主要逻辑
        self.create()
        print("数据库构建完毕")
        self.dongzuopian()
        print("动作片爬取完毕")
        self.aiqingpian()
        print("爱情片爬取完毕")
        self.xijupian()
        print("喜剧片爬取完毕")
        self.xuanyipian()
        print("悬疑片爬取完毕")
        self.lishipian()
        print("历史片爬取完毕")
        self.jiatingpian()
        print("家庭伦理片爬取完毕")
        self.ertongpian()
        print("儿童片爬取完毕")
        self.neidipian()
        print("内地片爬取完毕")


if __name__ == "__main__":
    spider = Spider()
    spider.run()
