import sys
import os
import commands
#import subprocess for python3
import re
import sys
import libxml2

#import MySQLdb for python2
import mysql.connector #for python3 

from xml.dom.minidom import parse, parseString

# for converting dict to xml 
from cStringIO import StringIO
from xml.parsers import expat
from bs4 import BeautifulSoup


def get_elms_for_atr_val(tag,atr,val):
  lst=[]
  elms = dom.getElementsByTagName(tag)
  for node in elms:
    for attrName, attrValue in node.attributes.items():
			if (attrName == atr and attrValue == val):
				lst = list(filter(lambda x: x.nodeType == 1, node.childNodes))				

   # ............

  return lst

# get all text recursively to the bottom
def get_text(e):

  lst = []
	if e.nodeType in (3,4):
		if not e.data.isspace():
			lst.append(e.data)
	else:
		for child in e.childNodes:
			lst = lst + get_text(child)
	return lst



# replace whitespace chars
def replace_white_space(str):
   p = re.compile(r'\s+')
   new = p.sub(' ',str)   # a lot of \n\t\t\t\t\t\t
   return new.strip()

# replace but these chars including ':'
def replace_non_alpha_numeric(s):
   p = re.compile(r'[^a-zA-Z0-9:-]+')
   #   p = re.compile(r'\W+') # replace whitespace chars
   new = p.sub(' ',s)
   return new.strip()

# convert to xhtml
# use: java -jar tagsoup-1.2.jar --files html_file
def html_to_xml(fn):
   # ............
   #xhtml_file = fn + ".xhtml"
   xhtml_file = fn + ".html"
	os.system(java -jar tagsoup-1.2.jar --files $xhtml_file)
	return xhtml_file
   

def extract_values(dm):

  lst = []
  temparr =[]
  l = get_elms_for_atr_val('table','class','most_actives')
  l.pop(0)
	for tr in l:
		tds = list(filter(lambda x: x.nodeType == 1, tr.childNodes))
		for td in tds:
			key = get_text(td)
			temp.append(key[0].replace('\n', ''))
		lst.append(to_dict(temparr))
		temparr = []
	return lst
   # ............
   #    get_text(e)
   # ............
  

# mysql> describe most_active;
def insert_to_db(l,tbl):
  db = mysql.connector.connect(host="127.0.0.1", user="root", passwd="", db="stockinfo")
  #db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="", db="stockinfo")
	cursor = db.cursor()
	cursor.execute("""CREATE TABLE IF NOT EXISTS `%s` (
	`name` VARCHAR(255),
	`volume` VARCHAR(50),
	`price` VARCHAR(50),
	`change`VARCHAR(50),
	`perc_change` VARCHAR(50)
	)""" % (tbl))
	
	for dic in l:
		query = """INSERT INTO `%s` (name, volume, price, change, perc_change) VALUES ("%s", "%s", "%s", "%s", "%s");""" % (tbl, dic['name'], dic['volume'], dic['price'], dic['change'], dic['perc_change'])
		cursor.execute(query)
		db.commit()
	cursor.close()
	db.close()
	


 return  # ............

# show databases;
# show tables;
def main():
  html_fn = sys.argv[1]
  fn = html_fn.replace('.html','')
  xhtml_fn = html_to_xml(html_fn)

  global dom
  dom = parse(xhtml_fn)

  lst = extract_values(dom)

   # make sure your mysql server is up and running
  cursor = insert_to_db(lst,fn) # fn = table name for mysql

  l = select_from_db(cursor,fn) # display the table on the screen

   # make sure the Apache web server is up and running
   # write a PHP script to display the table(s) on your browser

  return xml
# end of main()

if __name__ == "__main__":
    main()

# end of hw7
