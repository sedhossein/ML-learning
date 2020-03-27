## Clustering/Grouping

- Grouping data based on their similarity and distance between the collection members.
Minimum distance with maximum similarity can make groups/clusters.

- Is an Unsupervised learning

- In other words, It determine the distance function between data samples

- Used in
    - Title detecting
    - Grouping search results
    - Web mining
    - Data mining
    - Bioinformatics
    - Marketing
    - Management
    - Remote sensing
    
    
### Basic Concepts
- Distance: Dissimilarity between data (numeric value)
- Cluster Centroid: Average of data in one group/cluster(its new property for each group)
- Similarity: is vice versa distance ([0, 1])
    - numeric
        - data matrix(n*p) => distance matrix(n*n)
     - binary
        - contingency table 
        - pic1
     - ordinal
        - z-score
        - Minkowski(manhattan, euclidean)
        - pic3, pic4, pic5, pic6
        - 
- Distance between clusters 
    - single link
    - complete link
    - average link
    - centroid
    - mediod
        
- Property
    - Nominal
    - Binary
        - symmetric: each two data has equal value(men/women)
        - Asymmetric: two data has not equal value(+ or - result for virus)
    - Ordinal
        - has meaning ordinal(small, medium, large)
    - Numeric
        - numbers
    - Interval Scaled
        - intervals
        - real zero does not meaning
    - Ratio Scaled
        - real zero has meaning
    - Mixed Types
    
- purity
- RI(rand index)
- F-measure

    
### clustering methods
- partitioning
    - k-meaning
        - cluster shown with centroid(seed points)
        - number of clusters are Specified
        - has problem in non-convex
    - k-medoids/PAM(Partition around medoids)
        - has less performance on big data
        - has better result in noisily data
        - cluster shown with medoid
    
- hierarchical 
    - DIANA
        - unlike AGNES
    - AGNES
        - single-link
        - Dendrogram diagram
- Density-based
    - DBSACN
    - OPTICS
    - DenClue
- Model-based
    - EM
    - SOM
    - COBWEB
- Constraint-based
    - COD(obstacles)



