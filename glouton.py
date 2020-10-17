
import sys, time, random
from parse_tsp import parse_h2, parse_test



# Exemple appel : sommets[i][1], sommets[i][2], sommets[j][1], sommets[j][2])] = (i, j)
def distanceEntre(f, t):
    return ((f['x'] - t['x'])**2 + (f['y'] - t['y'])**2)**0.5



# Implementation h1 glouton
def h1(n, nodes):
    path = [n]
    print(nodes)
    toVisit = list(nodes.keys()) # liste des sommets
    toVisit.remove(n) # supprimer element numero n
    while len(toVisit) > 0:
        m = 999999999
        mIdx = -1
        for target in toVisit:
            print(nodes[target])
            print(target)
            dist = distanceEntre(nodes[target], nodes[path[-1]])
            if dist < m:
                m = dist
                mIdx = target
                print(mIdx)
        toVisit.remove(mIdx)
        path.append(mIdx)
        print(path)
    return path



# Implementation h2 glouton
def h2(n, nodes, sommets, arretes, cout):
    path = n # liste
    #l_path =[1, 2]
    path.append(n[0])
    #print(path)
    toVisit = list(nodes.keys()) #
    #print(toVisit)
    toVisit.remove(n[0])
    toVisit.remove(n[1])
    print('test h2')
    print(sommets)
    print(distanceEntre(nodes[0], nodes[path[1]]))


    while len(toVisit) > 0:
        m = 999999999
        mIdx = -1
        for element in range(0, len(path) - 1):
            for target in toVisit:
                dist = distanceEntre(nodes[target], nodes[path[element]])
                dist1 = distanceEntre(nodes[target], nodes[path[element+1]])
                dist2 = distanceEntre(nodes[path[element]], nodes[path[element+1]])

                cout = (dist1 + dist) - dist2
                #print(cout)
                if(cout>0) and cout<m:
                    m = cout
                    mIdx = target
                    indice = element+1
        path.insert(indice,mIdx)
        #toVisit.remove(mIdx)
        #path.append(mIdx)
        toVisit.remove(mIdx)
    #print (path)
    return path

##################################################
### execution de l'algorithme
##################################################

def glouton(args = {"-l": True}):
    print("Algorithme glouton H2")
    tsp_file = sys.argv[1]
    nodes = parse_h2(tsp_file)
    sommets, arretes, cout = parse_test(tsp_file)
    #nodes = parse_test(tsp_file)

    #sommets_indices, arretes, sommets =  parse_test(tsp_file)
    print(nodes)
    alea1 = random.randint(1, len(nodes))
    alea2 = random.randint(1, len(nodes))
    liste_sommets = []
    liste_sommets.append(1)
    #liste_sommets.append(alea1)
    #liste_sommets.append(alea2)
    liste_sommets.append(2)
    path = h2(liste_sommets, nodes, sommets, arretes, cout)
    #print(path)
    #path = h2(random.randint(1, len(sommets)), sommets_indices)
    #dist = distance(path, nodes)


    '''
    print(sommets_indices)
    #print(arretes)
    print(len(sommets_indices))
    print(len(arretes))
    print(sommets_indices)
    #print(len(nodes))
    '''

    #print(path)
    #print("Solution")
    #solution(path)
    # distance
    #print(dist)

if __name__ == '__main__':
    glouton()


####
