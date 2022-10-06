import operator
from collections import OrderedDict
text = "RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE.  AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE."
diccionario = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'Ñ':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0}


for letra in text: ##recorre texto y cuenta cada letra 
	##if letra == diccionario[letra]
	if letra in diccionario:
		diccionario[letra]= diccionario[letra]+1
print (diccionario)
sorted_x=sorted(diccionario.items(), key=operator.itemgetter(1), reverse=True) ## se crea array de arrays
print(sorted_x)

keys= [row[0] for row in sorted_x]
print(keys)
values=['e', 'a', 'o', 'l', 's', 'n', 'd', 'r','u','i','t','c','p','m','y','q','b','h','g','f','v','j','ñ','z','x','k','w']

dict1= dict(zip(keys,values))
print(dict1)

for letraAux in text:
	if letraAux in dict1:
		##textonuevo = text.replace(letra, dict1[letra])
		let= dict1[letraAux]
	else: 
		let = letraAux
		
	print(let, end='')
	
textonuevo= "uln riooits plosa ed rsosfente bie, a ci paneoa, pehlo ejmoecaqa ulpl ulpqatso ad yacuscpl recre in uosteosl re snremenrenusa re udace, a rsyeoenusa red uldaqloauslnscpl yoentemlmidscta re da rsoeuusln anaobiscta.  riooits yie in yautlo re mospeo loren en ed mamed re da udace lqoeoa en uatadinga en hidsl re 1936. meol riooits, ulpl luiooe uln dac meoclnadsrarec en da vsctlosa, nl uagl red usedl. meoclnsysuaqa da toarsusln oevldiuslnaosa re da udace lqoeoa. ci enlope mlmidaosrar entoe da udace toaqaharloa, oeydehara en ed entseool pidtstirsnaosl en qaouedlna ed 22 re nlvsepqoe re 1936, piectoa eca srentsysuausln. ci pieote yie csn rira in fldme lqhetsvl ad moluecl oevldiuslnaosl en paouva. csn riooits bierl pac dsqoe ed uapsnl maoa bie ed ectadsnscpl, uln da ulpmdsusrar red flqseonl red yoente mlmidao g re da rsoeuusln anaobiscta, teopsnaoa en pagl re 1937 da taoea re dsbisrao da oevldiusln, recploadsñanrl a da udace lqoeoa g yausdstanrl uln eddl ed mlcteoslo tosinyl yoanbiscta."




print("______________________________________________________________________________________________________________________________________________")
textonuevo = textonuevo.replace('a','A')
textonuevo = textonuevo.replace('b','Q')
textonuevo = textonuevo.replace('c','S')
textonuevo = textonuevo.replace('d','L')
textonuevo = textonuevo.replace('e','E')
textonuevo = textonuevo.replace('f','G')
textonuevo = textonuevo.replace('g','Y')
textonuevo = textonuevo.replace('h','J')
textonuevo = textonuevo.replace('i','U')
textonuevo = textonuevo.replace('j','X')
##textonuevo = textonuevo.replace('k','L')
textonuevo = textonuevo.replace('l','O')
textonuevo = textonuevo.replace('m','P')
textonuevo = textonuevo.replace('n','N')
textonuevo = textonuevo.replace('ñ','Z')
textonuevo = textonuevo.replace('o','R')
textonuevo = textonuevo.replace('p','M')
textonuevo = textonuevo.replace('q','B')
textonuevo = textonuevo.replace('r','D')
textonuevo = textonuevo.replace('s','I')
textonuevo = textonuevo.replace('t','T')
textonuevo = textonuevo.replace('u','C')
textonuevo = textonuevo.replace('v','V')
##textonuevo = textonuevo.replace('w','L')
##textonuevo = textonuevo.replace('x','L')
textonuevo = textonuevo.replace('y','F')
##textonuevo = textonuevo.replace('z','L')

print(textonuevo)
##letrasOrden= "eaolsndruitcpmyqbngfvjñzxkw"

##for letra in 
##keys =sorted_x.keys()
##print(keys)



##nuevo_dic={}
##for let in diccionario:
	##if diccionario[letra]





##sorted_values = sorted(diccionario.values(), reverse=True) ##ordena los valores del diccionario(no es la clave) devuelve un array con los valores
#dict_sorted = {}

#for i in sorted_values:
#	for k in diccionario.keys():
#		if diccionario[k] == i:
#			dict_sorted[k] = diccionario[k]
#			break
##print(sorted_values)

###nuevo_diccionario = {'E':0,'A':0,'O':0,'L':0,'S':0,'N':0,'D':0,'R':0,'U':0,'I':0,'T':0,'C':0,'P':0,'M':0,'Y':0,'Q':0,'B':0,'H':0,'G':0,'F':0,'V':0,'J':0,'Ñ':0,'Z':0,'X':0,'K':0,'W':0}
    
    
  
    
    
	

