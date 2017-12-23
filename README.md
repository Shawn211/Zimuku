# Zimuku
Python爬虫使用Scrapy框架抓取了zimuku内的字幕资料</br>

初始化创建Scrapy工程：        scrapy startproject zimuku</br>
并创建spider：               scrapy genspider demo http://zimuku.net</br>

目录结构：</br>
├── zimuku                  #外层目录</br>
│...├── __init__.py         #初始化脚本</br>
│...├── items.py            #Items代码模板，继承类自scrapy.Item</br>
│...├── middlewares.py      #Middlewares代码模板(继承类)</br>
│...├── pipelines.py        #Pipelines代码模板(继承类)</br>
│...├── settings.py         #Scrapy爬虫的配置文件</br>
│...└── spiders             #Spiders代码模板目录 我们写爬虫的地方</br>
│.......├── __init__.py</br>
│.......└── demo.py</br>
└── scrapy.cfg              #部署爬虫的配置文件</br>

spiders demo中</br>
#将我们需要爬的项目引入进来</br>
from zimuku.items import ZimukuItem</br>

settings.py中</br>
#只增加了这一行，通过配置告诉Scrapy明白是谁来处理结果</br>
ITEM_PIPELINES={'zimuku.pipelines.ZimukuPipeline':300,}</br>

import sys</br>
reload(sys)</br>
sys.setdefaultencoding('utf-8')</br>
