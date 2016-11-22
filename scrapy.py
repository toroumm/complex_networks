
import pickle
import requests
from lxml import html

visitadas = {}
lista_geral = []
rede = {}

def get_index(baseurl):
	global visitadas
	if baseurl in visitadas:
		return visitadas[baseurl]
	visitadas.update({baseurl:len(visitadas)+1})
	return visitadas[baseurl]


def scrapy_all(baseurl,criterio):

	try:
		url = requests.get(baseurl)
		tree = html.fromstring(url.content)

	except :

		if 'http' not in baseurl:
			baseurl = 'https://www.unifesp.br' + baseurl


		me = get_index(baseurl)
		mylink = baseurl
		adj_list = []
		global  lista_geral
		lista_geral.append(baseurl)
		global rede
		rede.update({'node_' + str(me): {'me': me, 'adj_list': adj_list, 'mylink': mylink}})
		return

	adj_list = []

	for link in tree.xpath('//a/@href'):

		link = link.strip('#')

		if 'http' not in link:
			#print 'ref', ref
			link = 'https://www.unifesp.br' + link

		adj_list.append(get_index(link))
		global lista_geral
		if link not in lista_geral and criterio in link and not '.pdf' in link :

			lista_geral.append(link)

			scrapy_all(link,criterio)

	me = get_index(baseurl)
	mylink = baseurl

	global rede
	rede.update({'node_'+str(me):{'me':me,'adj_list':adj_list,'mylink':mylink}})

	#if len(rede) > 20:
	#	with open("dados_sjc2.pk1", "wb") as ar:
	#		pickle.dump(rede, ar, pickle.HIGHEST_PROTOCOL)

	print baseurl, len(lista_geral), len(rede)

baseurl  ='https://www.unifesp.br'

scrapy_all(baseurl,"campus/sjc")

global rede
with open("dados_sjc_lenovo.pk1","wb") as ar:
	pickle.dump(rede,ar,pickle.HIGHEST_PROTOCOL)

	
