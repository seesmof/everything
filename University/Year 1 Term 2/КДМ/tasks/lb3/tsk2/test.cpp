#include "D:\repos\university\lib.h"

void dijkstra(vector<vector<pair<ll, ll>>> &graph, ll start, ll end)
{
    ll n = graph.size();
    vector<ll> distance(n, INT_MAX);
    vector<ll> parent(n, -1);
    vector<bool> visited(n, false);
    distance[start] = 0;
    for (ll i = 0; i < n - 1; i++)
    {
        ll min_distance = INT_MAX;
        ll current_vertex = -1;
        for (ll j = 0; j < n; j++)
        {
            if (!visited[j] && distance[j] < min_distance)
            {
                min_distance = distance[j];
                current_vertex = j;
            }
        }
        if (current_vertex == -1)
            break;
        visited[current_vertex] = true;
        for (auto neighbour : graph[current_vertex])
        {
            ll v = neighbour.first;
            ll weight = neighbour.second;
            int distance_through_current = distance[current_vertex] + weight;
            if (distance_through_current < distance[v])
            {
                distance[v] = distance_through_current;
                parent[v] = current_vertex;
            }
        }
    }
    if (parent[end] != -1)
    {
        cout << "Shortest path from " << start + 1 << " to " << end + 1 << ": ";
        vector<ll> path;
        for (ll v = end; v != -1; v = parent[v])
        {
            path.push_back(v);
        }
        reverse(all(path));
        for (ll v : path)
        {
            cout << v + 1 << " ";
        }
        cout << endl;
    }
    else
        cout << "There is no path from " << start + 1 << " to " << end + 1 << endl;
    cout << "Minimal path to " << end + 1 << ": " << distance[end] << endl;
}

int main()
{
    ll n, m;
    cout << "Enter number of vertices: ";
    cin >> n;
    cout << "Enter number of edges: ";
    cin >> m;
    vector<vector<pair<ll, ll>>> graph(n);
    for (ll i = 0; i < m; i++)
    {
        ll u, v, w;
        cin >> u >> v >> w;
        graph[u - 1].push_back(make_pair(v - 1, w));
        graph[v - 1].push_back(make_pair(u - 1, w));
    }
    ll start, end;
    cin >> start >> end;
    dijkstra(graph, start - 1, end - 1);
    return 0;
}