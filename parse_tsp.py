
import math

from sys import argv
from os.path import isfile


'''


    #print(lines)
    for line in lines:
        if line and line.lstrip()[0].isdigit(): # vrai, si ya que des chiffres dans la ligne
            #print (line.lstrip().split())
            sommets.append([int(i)+1 for i in line.split()])

    print (sommets)

    dic_arretes = dict() # sommet, sommet, cout
    arretes = list() # début, fin, poids
    print('------ nb sommets ---------')
    print(len(sommets))

#cost[nodes[i],nodes[j]]=cost[nodes[j],nodes[i]]=math.sqrt((x[nodes[i]]-x[nodes[j]])**2 + (y[nodes[i]]-y[nodes[j]])**2)
    # arretes

    for i in range(len(sommets)):
        for j in range(i):
            if i != j:

                print('test')
                # (1, 2) : 15.74747
                #if (math.sqrt(dist_euc(sommets[i][1], sommets[i][2], sommets[j][1], sommets[j][2]))!=0):
                dic_arretes [i,j] = dic_arretes[j,i] =math.sqrt(dist_euc(sommets[i][2], sommets[i][0], sommets[j][0], sommets[j][0]))

                arretes.append([i, j, dist_euc(sommets[i][1], sommets[i][2], sommets[j][1], sommets[j][2])])


    sommets_indices = list(range(1,len(sommets)+1))
    #print(len(sommets_indices), len(sommets))
    print('------ nb arretes ---------')
    print(len(arretes))
'''
def dist_euc(x1, y1, x2, y2):
	return(math.sqrt( (x1-x2)**2 + (y1 - y2)**2))


def parse_test(fichier):

	f = open(fichier, 'r') #passer fichier en parametre

	lines = f.read().splitlines()
	sommets = []
	arretes = []
	x = {}
	y={}
	cout = {}
	for line in lines:
		if line and line.lstrip()[0].isdigit(): #vrai, si ya que des chiffres dans la ligne
			k= line.split()
			sommets.append(int(k[0]))
			x[sommets[int(k[0])-1]] = int(k[1])
			y[sommets[int(k[0])-1]] = int(k[2])
	#print(x)
		for i in range(len(sommets)):
			#print(len(sommets))
			for j in range(i+1, len(sommets)):
				arretes.append((sommets[i],sommets[j]))
				arretes.append((sommets[j],sommets[i]))
				cout[sommets[i],sommets[j]]=cout[sommets[j],sommets[i]]=math.sqrt((x[sommets[i]]-x[sommets[j]])**2 + (y[sommets[i]]-y[sommets[j]])**2)



	return sommets, arretes, cout
    #return sommets_indices, arretes, sommets, dic_arretes

def parse_h2(filename):

    nodes = {}
    with open(filename, 'r') as f:
        lines = f.readlines()
        lines = list(map(lambda x:x.strip(), lines))
        # check structure fichier changer selon fichier
        s = lines.index("NODE_COORD_SECTION")
        e = lines.index("EOF")
        parsed = lines[s+1: e]

        parsed = list(map(lambda x: tuple(map(lambda y: float(y), x.split())), parsed))

    for node in parsed:
        nodes[int(node[0])] = {
            "id": int(node[0]),
            "x": node[1],
            "y": node[2]
        }

    return nodes
'''
def parse_h2(filename):

    nodes = {}
    with open(filename, 'r') as f:
        lines = f.readlines()
        lines = list(map(lambda x:x.strip(), lines))
        # check structure fichier changer selon fichier
        s = lines.index("NODE_COORD_SECTION")
        e = lines.index("EOF")
        parsed = lines[s+1: e]

        parsed = list(map(lambda x: tuple(map(lambda y: float(y), x.split())), parsed))

    for node in parsed:
        nodes[int(node[0])] = {
            "id": int(node[0]),
            "x": node[1],
            "y": node[2]
        }

    return nodes
'''
