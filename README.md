# SpearmanFootruleDistance
The sum of absolute values of the differences in the ranks.

<h2>Reference</h2>

An efficient approach for the rank aggregation problem : doi:10.1016/j.tcs.2006.05.024


<h2>Rank Aggregation Problem</h2>

1. Objects under cosideration are ordered according to several different criterion.

2. One looks for a ranking that is as close as possible to or, in a broader sense, combines—the rankings obtained in the first step.

<h2>Implementation</h2>

1. We're given the rankings that are to be combined. We're also given the proposed ranking.

2. Use spearman footrule to get the distance between the proposed ranking and the given rankings.

3. The ranking that minimizes the sum of the distances from proposed ranking to all the given rankings is returned as the output of the rank aggregation problem.

<h2>Assumptions</h2>

1. We've a full list of ranking present i.e given 3 items we've a score for each of them aka no partial ranking.

2. If there are score collisions, all the items with same score are assigned the same rank (minimum of the group) and an appropriate number of ranks are skipped 
e.g

Item Score Rank

A : 100 : 1

B : 100 : 1

C : 100 : 1

D : 65 : 4

<h2>Interesting reads</h2>

1. Kendall tau distance

2. http://www10.org/cdrom/papers/pdf/p577.pdf
