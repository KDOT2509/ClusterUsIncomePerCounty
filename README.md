# ClusterUsIncomePerCounty

The repo analyses the mean income in US counties.

## Unsupervised Learning K-Means

In `analysis.ipynb` pytorch and sklearn K-means are used for clustering below we can see the Elbow method to determine the optimal number of centroids.

![ElbowMethod](/plots/ElbowMethod.png)

Afterwards, a visualisation of the results are done using a shape file of the US with k=3 and k=5.

![ElbowMethod](/plots/ClusteringUsIncomeK3PerCountyCentralised.png)

![ElbowMethod](/plots/ClusteringUsIncomeK5PerCountyCentralised.png)

## Brownie
