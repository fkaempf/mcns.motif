import os
import random
from time import time
import pandas as pd
import numpy as np
import networkx as nx
import graph_tool.all as gt
from motif_counts import *
from tqdm.auto import tqdm
from collections import defaultdict
from tqdm import tqdm

df = pd.read_feather('/Users/fkampf/Documents/mcns.network.analysis/mcns_fw_edge_comp.feather')

# 1) build a unique list of all node labels
labels = np.unique(np.concatenate([df['pre'].values, df['post'].values]))

# 2) create the graph and a string vertex‐property to store the label
g = gt.Graph(directed=True)
v_label = g.new_vp("string")
g.vp["label"] = v_label

# 3) add one vertex per label, keep a Python dict to map label→vertex
label2v = {}
for L in labels:
    v = g.add_vertex()
    label2v[L] = v
    v_label[v] = str(L)

# 4) create a float edge‐property for your weights
e_weight = g.new_ep("float")
g.ep["weight"] = e_weight

# 5) add all edges with their weights
edge_list = [
    (label2v[src], label2v[tgt], float(w))
    for src, tgt, w in df[['pre','post','weight_m']].itertuples(index=False)
]
g.add_edge_list(edge_list, eprops=[g.ep["weight"]])

V = list(range(g.num_vertices()))
E = {
    (int(e.source()), int(e.target()))
    for e in g.edges()
    if g.ep['weight'][e] >= 5
}

aaa = collect_three_neuron_motifs(V, E, motifs)