
#include<iostream> 
#include<map> 
#include<list> 
#include<queue> 
 
using namespace std; 
 
template <typename T> 
class Graph { 
    // Adjacency List representation of graph 
    map<T, list<T> > adjList; 
 
public: 
    // Add edge to graph (undirected) 
    void addEdge(T src, T dest) { 
        adjList[src].push_back(dest); 
        adjList[dest].push_back(src);  // Because the graph is undirected 
    } 
 
    // Depth First Search (DFS) - Recursive 
    void dfs(T node, map<T, bool>& visited) { 
        visited[node] = true;  // Mark the current node as visited 
        cout << node << " ";   // Process the node (print) 
 
        // Visit all the neighbors of the current node using iterator 
        typename map<T, list<T> >::iterator it = adjList.find(node); 
        if (it != adjList.end()) { 
            for (typename list<T>::iterator neighbor = it->second.begin(); neighbor != it->second.end(); 
++neighbor) { 
                if (!visited[*neighbor]) { 
                    dfs(*neighbor, visited);  // Recursively visit unvisited neighbors 
                } 
            } 
        } 
    } 
 
    // Breadth First Search (BFS) 
    void bfs(T start, map<T, bool>& visited) { 
        queue<T> q; 
        q.push(start); 
        visited[start] = true; 
 
        while (!q.empty()) { 
            T node = q.front(); 
            q.pop(); 
            cout << node << " ";  // Process the node (print) 
 
            // Visit all the neighbors of the current node using iterator 
            typename map<T, list<T> >::iterator it = adjList.find(node); 
            if (it != adjList.end()) { 
                for (typename list<T>::iterator neighbor = it->second.begin(); neighbor != it->second.end(); 
++neighbor) { 
                    if (!visited[*neighbor]) { 
                        visited[*neighbor] = true; 
                        q.push(*neighbor); 
                    } 
                } 
            } 
        } 
    } 
 
    // Function to call DFS/BFS for each disconnected component 
    void traverseGraph(int choice) { 
        map<T, bool> visited; 
 
        // Initialize visited map for all nodes 
        for (typename map<T, list<T> >::iterator it = adjList.begin(); it != adjList.end(); ++it) { 
            visited[it->first] = false; 
        } 
 
        if (choice == 1) { 
            // BFS for each disconnected component 
            for (typename map<T, list<T> >::iterator it = adjList.begin(); it != adjList.end(); ++it) { 
                if (!visited[it->first]) { 
                    cout << "BFS starting from node " << it->first << ": "; 
                    bfs(it->first, visited); 
                    cout << endl; 
                } 
            } 
        } 
        else if (choice == 2) { 
            // DFS for each disconnected component 
            for (typename map<T, list<T> >::iterator it = adjList.begin(); it != adjList.end(); ++it) { 
                if (!visited[it->first]) { 
                    cout << "DFS starting from node " << it->first << ": "; 
                    dfs(it->first, visited); 
                    cout << endl; 
                } 
            } 
        } 
        else { 
            cout << "Invalid choice!" << endl; 
        } 
    } 
}; 
 
int main() { 
    Graph<int> g; 
    int numEdges, src, dest, choice; 
 
    // Taking user input for number of edges 
    cout << "Enter the number of edges: "; 
    cin >> numEdges; 
 
    // Taking user input for edges 
    for (int i = 0; i < numEdges; i++) { 
        cout << "Enter edge (source destination): "; 
        cin >> src >> dest; 
        g.addEdge(src, dest);  // Add the edge to the graph 
    } 
 
    // Continuous loop for multiple BFS/DFS operations 
    while (true) { 
        // Ask user for traversal choice (BFS or DFS) 
        cout << "Enter 1 for BFS, 2 for DFS, 0 to exit: "; 
        cin >> choice; 
 
        if (choice == 0) { 
            cout << "Exiting the program...\n"; 
            break;  // Exit the loop and the program 
        } 
 
        // Traverse the graph based on user input 
        g.traverseGraph(choice); 
 
        // Ask if the user wants to continue 
        char continueChoice; 
        cout << "Do you want to perform another traversal? (y/n): "; 
        cin >> continueChoice; 
 
        if (continueChoice == 'n' || continueChoice == 'N') { 
            cout << "Exiting the program...\n"; 
            break;  // Exit the loop and the program 
        } 
    } 
 
    return 0; 
} 

/*Enter the number of edges: 4 
Enter edge (source destination): 0 1 
Enter edge (source destination): 0 3 
Enter edge (source destination): 1 2 
Enter edge (source destination): 3 4 
Enter 1 for BFS, 2 for DFS, 0 to exit: 1 
BFS starting from node 0: 0 1 3 2 4 
Do you want to perform another traversal? (y/n): y 
Enter 1 for BFS, 2 for DFS, 0 to exit: 2 
DFS starting from node 0: 0 1 2 3 4 /*
