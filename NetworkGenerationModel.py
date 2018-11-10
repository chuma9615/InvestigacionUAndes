import random
import networkx as nx
import matplotlib as plt
# import itertools as it
#     (for i,j in it.permutations(cliquel,2):) This poop is used with intertools

def scaleprob(plist):
    """Scale probability list so it adds to 1."""
    return [x/sum(plist) for x in plist]

def genCliques(k,minSize,maxSize):
    """Returns a graph G composed of k cliques with a number of nodes between
    minSize and maxSize each, and a list of nodes, one for each clique."""
    G = nx.Graph()  #The Graph
    Gnds= 0     #Number of nodes in G
    cliquel=[]  #clique list, list of ids of the node of each clique that will merge with the tree.
    for clique in range(k):
        num = random.randint(minSize,maxSize)
        tempG = nx.complete_graph(range(Gnds,Gnds + num))
        cliquel.append(Gnds)
        Gnds += num
        G = nx.compose(G,tempG)
    return [G,cliquel]

def genScaleFreeDegreeDistribution(G,NewEdges):
    """Generates a scale free degree distribution from a barabasi-albert model
    graph, taking the degree of each node, subtracting the degree of a node in G,
     and giving it as an attribute 'sfDeg' to a random node in G."""
    BA = nx.barabasi_albert_graph(len(G),NewEdges)
    BAdeg=[t[1] for t in BA.degree()]
    Gdeg=[t[1]*-1 for t in G.degree()]
    BAdeg.sort()
    Gdeg.sort(reverse=True)
    rest=random.sample([0 if sum(x)<0 else sum(x) for x in zip(BAdeg,Gdeg)],len(G)) #+2?
    rest=[(n,rest[n]) for n in range(len(G))]
    nx.set_node_attributes(G,dict(rest),"sfDeg")

# def NodeMerges(G,n):
#     """For each node n(int) in graph G, returns the number of merges this node
#     must make."""
#     avg=sum([G.degree[deg] for deg in range(len(G))])/len(G)
#     return int(G.nodes[n]["sfDeg"]/avg)

# def CliqueMerges1(G1,i):
#     """Returns the total number of merges for each clique containing node i"""
#     result=NodeMerges(G1,i)
#     for x in G1.neighbors(i):
#         result+=NodeMerges(G1,x)
#     return result

def CliqueMerges(G,G1,i):
    """Returns the total number of merges needed for each clique containing node i"""
    result=sum([G.nodes[n]["sfDeg"] for n in nx.ego_graph(G1,i).nodes()])
    return result

def clean_waste(tree):
    """Removes innecesary nodes from the tree created with random_tree()"""
    waste=[n for n in tree.nodes() if tree.degree()[n] == 2]
    while waste:
        node=waste[0]
        neigs = [n for n in tree.neighbors(node)]
        realneigs = [neig for neig in neigs if tree.degree()[neig] != 1]
        if realneigs:
            for neig in realneigs:
                tree=nx.contracted_nodes(tree,node,neig,self_loops=False)
        waste=[n for n in tree.nodes() if tree.degree()[n] == 2]
    waste=[n for n in tree.nodes() if tree.degree()[n] == 2]
    return tree

def genTree(G,cliquel):
    """Generates a graph composed of a random tree in wich each leaf is one of
    the cliques in G."""
    k=len(cliquel)   #Number of cliques
    if k < 2:
        print("there must be more than 1 clique!")
    #To determine the constant "3.8" it was tested the torso_nodes/nodes ratio for
    #the function random tree, and it was discovered to be aprox 0.625, with a
    #max value of 0.76 at low number of nodes, so to be sure, I used 0.8:


    tree = nx.random_tree(int(k*3.8))
    #list of nodes with degree = 1:
    leaves = [n for n,v in tree.nodes(data=True) if tree.degree()[n] == 1]
    #The other nodes:
    not_leaves = [n for n,v in tree.nodes(data=True) if tree.degree()[n] != 1]

    #Since the tree must have the same amount of leaves as cliques, we make sure that happens:
    cnt = 0
    while len(leaves)!=k:
        #Because of the flies, we put a limit to the search of the tree:
        if cnt == 1000:
            print("surpassed 1000 tries and can't find random tree with #leaves>=#cliques")
            1/0
        cnt += 1
        #if we obtain a tree with more leaves, we cut them:
        if len(leaves)>k:
            tree.remove_node(leaves.pop(random.randint(0,len(leaves)-1)))
        #otherwise, we try with other tree:
        else:
            tree = nx.random_tree(int(k*3.8))
            leaves = [n for n,v in tree.nodes(data=True) if tree.degree()[n] == 1]
            not_leaves = [n for n,v in tree.nodes(data=True) if tree.degree()[n] != 1]

    tree = clean_waste(tree)
    #First, we make sure node ids from tree aren't repeated in G by making their
    #numbers start when the nodes on G end:
    tree=nx.convert_node_labels_to_integers(tree,len(G))
    leaves = [n for n,v in tree.nodes(data=True) if tree.degree()[n] == 1]
    not_leaves = [n for n,v in tree.nodes(data=True) if tree.degree()[n] != 1]
    #Make leaves have the same name id as one node from each clique in G:
    leaf_name_dic = dict(zip(leaves,cliquel))
    tree= nx.relabel_nodes(tree,leaf_name_dic)
    #Make the not-leaves have a new name so as to continue in order with the rest of nodes:
    not_leaf_names = [len(G) + x for x in range(len(not_leaves))]
    not_leaf_name_dic = dict(zip(not_leaves,not_leaf_names))
    tree=nx.relabel_nodes(tree,not_leaf_name_dic)
    #Combine The tree with G:
    G=nx.compose(G,tree)

    return G

def P(G,i,j):
    """Returns the probability of clique with node i chosing clique with node j to merge.
     Its equivalent to the probability of ending in node j if you started from node
    i, chosing a random path each time, without being able to return from where you came."""
    sp = nx.shortest_path(G, i, j)
    result = 1
    if i==j:
        result=0
    for node in sp[1:-1]:
        result = result*(1/(G.degree[node]-1))
    return result
    # result.update((x, y*2) for x, y in result.items())

# def PairwiseMerges(G,CMdict,i,j): #MUST  BE  USED WITH i ANd j FROM CLIQUEL
#     """Gives the number of node merges between each pair of cliques containing node i and j."""
#     return int(CMdict[i]*P(G,i,j)))

def AddSet(lyn,small):
    """Recieves a list of sets (lyn), and appends to it a set(small). Then all
     sets that have intersections are unified, and a list of sets is returned in
      which no set has elements in common with the other sets."""
    finds=[]
    for x in lyn:
        if x & small:
            x|=small
            finds.append(x)
    if not finds:
        lyn.append(small)
        return lyn
    elif len(finds)>1:
        for y in range(len(finds)-1):
            lyn[lyn.index(finds[0])]|=finds[y+1]
            lyn.remove(finds[y+1])
    return lyn

def MergingNodes(G,operations):
    """Merges the pair of nodes presented in list of sets 'operations'."""
    groups=[]
    for zet in operations:
        groups=AddSet(groups,zet)
    for grup in groups:
        e=random.sample(grup,1)[0]
        harem={n:e for n in grup if n!=e}
        G1=nx.relabel_nodes(G,harem)
    return G1

def Merger_of_AllNodes(G,G1,cliquel):
    """The proces of merging all nodes of graph G. For each clique, random nodes are merged
    with random nodes from other cliques, with a probability of P() of being chosen,
    untill the values of 'sfDeg' of the clique's nodes reaches 0."""
    operations=[] #needed merges between nodes are stored as a list of sets.
    nodesleft=list(G.nodes()) #Keeps count of wich nodes haven't been merged yet
    for i in cliquel:
        while CliqueMerges(G,G1,i)>0:
            #A random node from the clique 1 that has "sfDeg">0 and is in nodesleft list, is picked
            clq1node=[n for n in nx.ego_graph(G1,i).nodes() if G.nodes[n]["sfDeg"]>0 and n in nodesleft]
            #From other avaliable cliques, a random one is chosen
            clqleft=[q for q in cliquel if CliqueMerges(G,G1,q)>0 and q!=i]
            #if there is only one clique that requires merging, then it will merge with other node randomly beacuse poop.
            if not clqleft:
                inp=input("Merge resting nodes?(yes,no) Merges left for each node:\n"+str([G.nodes[n]["sfDeg"] for n in clq1node]))
                if inp in ["True","si","yes","1","true","affirmative","yhea","Yhea","yhea!","yhea men!","yhea nigga men!","nyes","nyes!","k","ok","K","OK","k!"]:
                    for nd1 in clq1node:
                        while G.nodes[nd1]["sfDeg"]>0:
                            tempoptions=list(G.nodes())
                            nd2=random.sample([n for n in tempoptions if not n in nx.ego_graph(G1,i).nodes()],1).pop()
                            operations.append({nd1,nd2})
                            tempoptions.remove(nd2)
                            G.nodes[nd1]["sfDeg"]+=-1
                            G.nodes[nd2]["sfDeg"]=0
                else:
                        break
            clq1node=random.sample(clq1node,1)[0]
            plist=scaleprob([P(G,i,j) for j in clqleft]) #The probability vector using P() is scaled as to add to 1
            num=random.random()  #random float form 0 to 1 will decide wich clique j is chosen.
            cnt=0
            for pos in range(len(clqleft)):
                cnt+=plist[pos]
                if cnt >= num:
                    #A random node from the clique 2 that has "sfDeg">0 and is in nodesleft list, is picked
                    clq2node=[n for n in nx.ego_graph(G1,clqleft[pos]).nodes() if G.nodes[n]["sfDeg"]>0 and n in nodesleft]
                    clq2node=random.sample(clq2node,1)[0]
                    operations.append({clq1node,clq2node})
                    #The problem of choosing the degree value that stays over the other
                    #is that the high degree nodes could easely disappear, for now
                    #I will make it so the highest degree node wins
                    # whowins=random.sample([clq1node,clq2node],1).pop()
                    whowins=max([clq1node,clq2node],key=lambda x:G.nodes[x]["sfDeg"])
                    wholoses=[x for x in [clq1node,clq2node] if x!=whowins].pop()
                    nodesleft.remove(wholoses)
                    G.nodes[whowins]["sfDeg"]+=-1
                    G.nodes[wholoses]["sfDeg"]=0

                    break
    return operations

def GenNetwork(k,NewEdges,minSize,maxSize):
    """Function that generates the network to be used in the simulations,
        with variables being:
        k:          number of initial cliques
        NewEdges:   Number of edges to attach from a new node to existing nodes
                    in B-A model graph. It must satisfy 1 <= NewEdges < minSize*k
        minSize:    minimum size of said cliques
        maxSize:    maximum size of said cliques"""
    #First of all, we obtain a group of cliques:
    #Cliques length between min y maxSize are created and added to G1
    [G1,cliquel] =genCliques(k,minSize,maxSize)
    #G1 is the graph that contains only the initial separated cliques.

    #Now we generate de Barabási Albert graph to obtain the distribution:
    genScaleFreeDegreeDistribution(G1,NewEdges)
    # print(nx.get_node_attributes(G,"sfDeg"))

    #Get all the values of NodeMerges and CliqueMerges for all nodes and cliques:
    # """I'm not really comfortable with storing the values of NodeMerges, CliqueMerges
    # and PairwiseMerges in lists rather than being functions..."""
    # NMdict=dict([(n,NodeMerges(G1,n)) for n in range(len(G1))])
    # CMdict=dict([(n,CliqueMerges(G1,n)) for n in cliquel])

    #The graph is combined with a tree:
    G =genTree(G1,cliquel)

    #Get all the values of PairwiseMerges for each pair of cliques:
    # PMdict=dict([((n,m),PairwiseMerges(G,CMdict,n,m)) for n,m in it.permutations(cliquel,2)])
    #Gottatrythis!!! But probably I will not use this code anymore... print(PMdict[(n,m)]==PMdict[(m,n)])!!!!!!!!!!!!!!!!!!!!!!!!!!!
    operations=Merger_of_AllNodes(G,G1,cliquel)
    G=MergingNodes(G,operations)
    G=nx.convert_node_labels_to_integers(G,len(G))
    inp=input("Show graph?")
    if inp in ["True","si","yes","1","true","affirmative","yhea","Yhea","yhea!","yhea men!","yhea nigga men!","nyes","nyes!","k","ok","K","OK","k!"]:
        nx.draw(G,with_labels=True)
        plt.pyplot.show()
    return G

#GenNetwork(100,4,4,5)







#These poops are useful to visualiza the graphs:
# import matplotlib as plt
# G=nx.complete_graph(range(3,10))
# nx.draw(G,with_labels=True)
# plt.pyplot.show()
