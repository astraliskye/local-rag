Last project resources
- Meal matrix P x F matrix (P = number of records, F = number of features)


1. Find the min and max carb intakes
2. Create "bins" with a size of 20 starting at min carb and up to max carb
	1. Fill each bin with the corresponding meals according to their carb intake
3. Associate bin numbers with corresponding row of the feature matrix

Bin number is the ground truth

Implement 2 clustering algorithms: k-means and dbscan
Goal is to have n clusters
- Tough for dbscan
	- Order clusters in order of SSE
		- Take max sse cluster and perform bisecting k-means for it
		- Take two closest clusters and merge them into one

Compute SSE for each cluster
Compute entropy and purity for each cluster