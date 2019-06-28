# Approximate Distance Oracles Algorithm

Implementation of the Approximate Distance Oracles algorithm.

The algorithm statistics are available in the *results* directory. 

Paper:
[Link][1]

## Graphs used & statistics:

### *Les Misérables*

##### Description:

Undirected network contains co-occurrences of characters in Victor Hugo's novel 'Les Misérables'.
A node represents a character and an edge between two nodes shows that these two characters appeared in the same chapter of the the book. The weight of each link indicates how often such a co-appearance occurred.

##### Metadata:
- Number of nodes: 77
- Number of edges: 254

### *Bitcoin OTC Trust*

##### Description:
This is who-trusts-whom network of people who trade using Bitcoin on a platform called Bitcoin OTC.
Since Bitcoin users are anonymous, there is a need to maintain a record of users' reputation to prevent transactions with fraudulent and risky users.
Members of Bitcoin OTC rate other members in a scale of 0 (total trust) to 20 (total distrust) in steps of 1.

##### Metadata:
- Number of nodes: 5,875
- Number of edges: 21,489

### *Brain Neural Network Sample*

##### Description:
The network contains 306 nodes that represent neurons.
Two neurons are connected if at least one synapse or gap junction exist between them.
The weight is the number of synapses and gap junctions.

##### Metadata:
- Number of nodes: 297
- Number of edges: 2,148

[1]: http://www.cs.jhu.edu/baruch/teaching/600.427/Papers/oracle-STOC-try.pdf