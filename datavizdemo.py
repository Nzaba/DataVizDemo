# -*- coding: utf-8 -*-
"""DataVizDemo.ipynb

Automatically generated by Colaboratory.

"""

import networkx as nx
import random
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import pandas as pd
from math import *
import gzip
import csv
import operator

"""\# **Network graphs in Python with networkx**

1. **Graph** - A representation of a set of objects where some pairs of objects are connected by links. The interconnected objects are represented by points termed as vertices, and the links that connect the vertices are called edges
2. **Vertex** - Each node of the graph is represented as a vertex
3. **Edge** − Edge represents a path or connection or relationship between two vertices (nodes)
4. **Real world example** - Facebook. Each person on Facebook is a node and is connected through edges.

# Step 1

- Generate a network object by placing 50 nodes uniformly at random in a unit cube (1 by 1 by 1). 
- **Radius**: Two nodes will be connected if the distance between the nodes is at most 0.25
"""

#create a random graph
G = nx.random_geometric_graph(50, 0.25)

"""# Step 2

- Use a for loop to construct the graph according to specifications made in the previous step
- Map the nodes and edges on the Cartesian plane aka X, Y coordinate space
"""

#Add edges as disconnected lines in a single trace and nodes as a scatter trace
edge_x = []
edge_y = []
for edge in G.edges():
    x0, y0 = G.nodes[edge[0]]['pos']
    x1, y1 = G.nodes[edge[1]]['pos']
    edge_x.append(x0)
    edge_x.append(x1)
    edge_x.append(None)
    edge_y.append(y0)
    edge_y.append(y1)
    edge_y.append(None)

edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=0.5, color='#888'),
    hoverinfo='none',
    mode='lines')

node_x = []
node_y = []
for node in G.nodes():
    x, y = G.nodes[node]['pos']
    node_x.append(x)
    node_y.append(y)

node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers',
    hoverinfo='text',
    marker=dict(
        showscale=True,
        # colorscale options
        #'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
        #'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
        #'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
        colorscale='YlGnBu',
        reversescale=True,
        color=[],
        size=10,
        colorbar=dict(
            thickness=15,
            title='Node Connections',
            xanchor='left',
            titleside='right'
        ),
        line_width=2))

"""# Step 3

- Color nodes by number of connections
- Can also set size to be proportional to number of connections by changing node_trace.marker.size = node_adjacencies
"""

node_adjacencies = []
node_text = []
for node, adjacencies in enumerate(G.adjacency()):
    node_adjacencies.append(len(adjacencies[1]))
    node_text.append('# of connections: '+str(len(adjacencies[1])))

node_trace.marker.color = node_adjacencies
node_trace.text = node_text

"""# Step 4: Make plot"""

# Create Network Graph
fig = go.Figure(data=[edge_trace, node_trace],
             layout=go.Layout(
                title='<br>Network with 100 nodes and radius = 0.25',
                titlefont_size=16,
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20,l=5,r=5,t=40),
                annotations=[ dict(
                    text=" ",
                    showarrow=False,
                    xref="paper", yref="paper",
                    x=0.005, y=-0.002 ) ],
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                )
fig.show()