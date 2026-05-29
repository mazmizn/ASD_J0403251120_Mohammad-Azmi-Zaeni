#Nama: Mohammad Azmi Zaeni
#NIM: J0403251120
#Kelas: TPL A1
#==============================

def createGraph(V, edges):
    adj = {
        'A': [],
        'B': [],
        'C': [],
        'D': []
    }

    # Add each edge to the adjacency list
    for it in edges:
        u = it[0]
        v = it[1]
        adj[u].append(v)

        # since the graph is undirected
        adj[v].append(u)
    return adj

if __name__ == "__main__":
    V = 8

    #List of edges (u, v)
    edges = [['A','B'],['A','C'],['C','D'],['B','D']]

    #Build the graph using edges
    adj = createGraph(V, edges)

    print("Adjacency List Representation:")
    for kamar, tetangga in adj.items():

        #Print the vertex
        print(f"{kamar}:", end=" ")
        for j in adj[kamar]:

            #Print its adjacent
            print(j, end=" ")
        print()