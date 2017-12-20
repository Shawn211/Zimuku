# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
reload(sys)						#这句不能少！！！
sys.setdefaultencoding('utf-8')
import codecs

class ZimukuPipeline(object):
    def process_item(self, item, spider):
    	nums=item['num']
        num=0
        with codecs.open('zimu','a+') as ku:
        	while num<nums:
        		ku.write(item[str(num)])
        		ku.write('\n')
        		num+=1