# 1905MovieCrawler-Visualization-Pyqt5
1905电影网站爬虫可视化，数据存储在MySQL并在Pyqt5展示数据，Pyqt5可视化大屏还有登录注册功能

## 一、运行环境

1、Python3.7

2、Windows10

3、Mysql

4、jupyter notebook

## 二、运行步骤

前提条件先把requirements.txt中的包安装好，才可以接着往下步骤：

1、先修改spider.py第15行和Login.py第84行中数据库链接的库名账号密码

![image-1](/Img/1.png)

![image-1](/Img/2.png)

2、运行spider.py，因为爬虫有设置time.sleep，所以采集速度慢，可以根据自己需求修改。爬取完毕会提醒 **数据全部采集完成**。采集还未完成时请不要运行其他文件。

3、运行QtLogin中的Login.py，即可运行程序，先注册再登录，就可以使用了。

## 三、后续

因为这个项目是匆忙写的，很多功能都很仓促，数据图表展示完全是静态的，后面可以万一有大佬有空闲时间想改成动态或者优化代码逻辑的，都可以的Pull request给我，我更新进项目中，Github不是每天在线，如果有大佬合并了代码，可以发邮件360812146@qq.com提醒我合并在此向大家先鞠个躬。
