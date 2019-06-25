# Randomized Algorithms

Implementation of the Approximate Distance Oracles algorithms. 

Paper:
[Link][1]

### Graphs used & statistics:

#### Les Misérables

##### Description:

Undirected network contains co-occurrences of characters in Victor Hugo's novel 'Les Misérables'.
A node represents a character and an edge between two nodes shows that these two characters appeared in the same chapter of the the book. The weight of each link indicates how often such a co-appearance occurred.

##### Metadata:
- Number of nodes: 77
- Number of edges: 254

##### Statistics:
- Pre-processing time: 0.032.67 seconds
- Average Dijkstra time: 0.0291 seconds
- Average query time: 0.002 seconds
- Average stretch: 2.499
- Max stretch value: 3.364
- Min stretch value: 1.48

#### Bitcoin OTC Trust

##### Description:
This is who-trusts-whom network of people who trade using Bitcoin on a platform called Bitcoin OTC.
Since Bitcoin users are anonymous, there is a need to maintain a record of users' reputation to prevent transactions with fraudulent and risky users.
Members of Bitcoin OTC rate other members in a scale of 0 (total trust) to 20 (total distrust) in steps of 1.

##### Metadata:
- Number of nodes: 5,875
- Number of edges: 21,489

##### Statistics:
- Pre-processing time: 104.912 seconds
- Average query time: 0.0017 seconds
- Average Dijkstra time: 0.287 seconds
- Average stretch: 4.959
- Max stretch value: 15.928
- Min stretch value: 4.865

#### Brain Neural Network Sample

##### Description:
The network contains 306 nodes that represent neurons.
Two neurons are connected if at least one synapse or gap junction exist between them.
The weight is the number of synapses and gap junctions.

##### Metadata:
- Number of nodes: 297
- Number of edges: 2,148

##### Statistics:
- Pre-processing time: 0.28 seconds
- Average query time: 0.0018 seconds
- Average Dijkstra time: 0.767
- Average stretch: 2.027
- Max stretch value: 3.909
- Min stretch value: 0.829

[1]: http://www.cs.jhu.edu/baruch/teaching/600.427/Papers/oracle-STOC-try.pdf