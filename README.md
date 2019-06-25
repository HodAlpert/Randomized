# Randomized Algorithms

Implementation of the Approximate Distance Oracles algorithms. 

Paper:
[Link][1]

### Graphs used & stats:

#### Les Misérables

##### Description:

Undirected network contains co-occurrences of characters in Victor Hugo's novel 'Les Misérables'.
A node represents a character and an edge between two nodes shows that these two characters appeared in the same chapter of the the book. The weight of each link indicates how often such a co-appearance occurred.

##### Metadata:
Number of nodes: 77

Number of edges: 254

##### Statistics:
Pre-processing time: 0.032.67 seconds

Total average stretch: 2.499

Average query time: 0.002 seconds

Max stretch value: 3.364

Min stretch value: 1.48

#### Bitcoin OTC Trust
##### Description:
This is who-trusts-whom network of people who trade using Bitcoin on a platform called Bitcoin OTC.
Since Bitcoin users are anonymous, there is a need to maintain a record of users' reputation to prevent transactions with fraudulent and risky users.
Members of Bitcoin OTC rate other members in a scale of 0 (total trust) to 20 (total distrust) in steps of 1.

##### Metadata:
Number of nodes: 5,875
Number of edges: 21,489

##### Statistics:
Pre-processing time: 104.912 seconds
Total average stretch: 4.959
Average query time: 0.0017 seconds
Max stretch value: 15.928
Min stretch value: 4.865

[1]: http://www.cs.jhu.edu/baruch/teaching/600.427/Papers/oracle-STOC-try.pdf