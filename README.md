# ClusterUsIncomePerCounty

The repo analyses the mean income in US counties.

## Unsupervised Learning K-Means

In `analysis.ipynb` pytorch and sklearn K-means are used for clustering below we can see the Elbow method to determine the optimal number of centroids.

![ElbowMethod](/plots/ElbowMethod.jpg)

Afterwards, a visualisation of the results are done using a shape file of the US with k=3 and k=5.<br/>
**k=3**
![ElbowMethod](/plots/ClusteringUsIncomeK3PerCountyCentralised.png)
**k=5**
![ElbowMethod](/plots/ClusteringUsIncomeK5PerCountyCentralised.png)

## Brownie
A simple smart contract has been implemented `brownie/init/contracts/USIncome.sol` to simulate pushing the data to the Ethereum Blockchain via the `brownie/init/scripts/UsIncome.py`. The basic idea behind this was to learn how to save data on the Ethereum chain and look for possible use cases in the space of GOV3.0.