# coding=utf-8


import pickle
import requests
from lxml import html
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

reload(sys)
sys.setdefaultencoding('utf-8')


visitadas = {}
lista_geral = []
rede = {}


def clear_atm(category):


	category = [i.replace('\n','') for i in category]
	
	category = [i.strip(' ') for i in category if len(i) > 3 and not None]

	return filter(None,category)

def get_atm(data, tree):

	#pega somente o ATM activity category
	
	x = tree.xpath('//div/div[1]/div/div/div[2]/div/text()')

	data['actCategory'] = clear_atm(x)

	#ATM data category

	x = tree.xpath('//div/div[3]/div/div/div[2]/div/text()')
	
	data['dataCategory'] = clear_atm(x)

	#Atm stakeholders Precisa afunilar tem a consulta xtree

	x = tree.xpath('//div/div[5]/div/div/div[2]/div/text()')
	
	data['dataStakeholder'] = clear_atm(x)

	#atm regions Também precisa afunilar

	x = tree.xpath('//div/div[7]/div/div/div[2]/div/text()')

	data['regions'] = clear_atm(x)

	return data

def get_header(data,tree):
	
	name = tree.xpath('//*[@id="content"]/div/div[1]/h1/text()')

	name = [i.replace('\t','') for i in name]

	data['nameService'] = clear_atm(name)[0]

	per_describe = tree.xpath('//div[@class="percent-complete"]/text()')

	data['percentPrescribe'] =  per_describe[0]

	version = tree.xpath('//*[@id="block-system-main"]/div/div/div/div[1]/div/div[2]/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/text()')

	data['version'] = version[0]

	implementStatus = tree.xpath('//*[@id="block-system-main"]/div/div/div/div[1]/div/div[2]/div/div[1]/div/div/div/div[5]/div/div/div[2]/div/text()')

	data['implementStatus'] = implementStatus[0]

	versionCategory  = tree.xpath('//*[@id="block-system-main"]/div/div/div/div[1]/div/div[2]/div/div[1]/div/div/div/div[7]/div/div/div[2]/div/text()')

	data['versionCategory'] = versionCategory[0]

	return data

def get_registrationProcess(data, tree):

	serviceDescription = tree.xpath('//div/div[@class="pane-content"]/p/text()')

	data['serviceDescription'] = serviceDescription

	#voltar e peneirar mais

	#serviceDocumentation = tree.xpath('//div[@class="panel-panel"]/div/span/span/a/text()')

	#print serviceDocumentation

	serviceTecnicalInterface = tree.xpath('//div/div/div/div[3]/div/div[2]/div/div[1]/div/div/div/div[3]/div/div/div/div/div/div[2]/div/div/text()')

	with open('Output.txt','w') as text_file:
		text_file.write(html.tostring(tree))

	print serviceTecnicalInterface

	sys.exit()


#ja tem que estar logado
baseurl  ='https://eur-registry.swim.aero'


driver = webdriver.Chrome()

driver.implicitly_wait(2)

driver.get( baseurl+'/service-implementations')

#find_element_by_xpath

	
with open('Output.txt' ,'w') as te:
	te.write(driver.page_source)

sys.exit()

url = requests.get(baseurl+'/service-implementations')

tree = html.fromstring(url.content)

s = tree.xpath('//a/@href')

ss = [x for x in s if 'services' in x]

services = []
for i in ss:
	if i not in services:
		services.append(i)


print baseurl+'/services/m-clickaero/aeronautical-data-validation-service-10'

data = {}
data_atm = {}


page = requests.get(baseurl+'/services/m-clickaero/aeronautical-data-validation-service-10' )

ree = html.fromstring(page.content)

get_registrationProcess(data,ree)

#print get_header(data, tree)

print get_atm(data_atm, tree)
	
#with open('Output.txt','w') as text_file:
#	text_file.write(page.text)


