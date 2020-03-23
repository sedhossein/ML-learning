### classification
    - target: make label for discrete data
    - make a model to classification data based on learning data
####steps
    1. making model: each tuple sample, has a label. collection of these samples making data. and show models with: decision tree, ...
    2. using model: estimate model accuracy

### inductive learning
    - learning  with superviser
    - f is target function
    - we could found hypothesis function(h)
        - be like f
        - have traning set with some examples
        
### deductive learning
    - make and learn `h` function to be equal with `f` 
    - `h` is consistent if be comlpete equal `f` in any examples
    - like curve fitting
    
 --- 
 
### decision tree(a way to classification data)
-   its powerful to show discrete data
-   Resistant o noise
-   able to learning conjunctive statements
-   famous in inductive learning algorithms
-   has nodes, leaf, non leaf nodes, attribute, branch    
- #### usage :
    - in issues that we have single answer like category or class names
    - the examples could have <property, value> pair
    - in discrete data
    - in situations that need Disjunctive Descriptor
- #### properties
    - Resistant again noise
    - support id-then rule
    - good for big data, data mining
    - can Combination rules to make statements
    - when our training data is not too much

#### some tips:
    * training set, test set  are different values (pic1)
    * we wanna have minimal and compact tree
    * maybe we have many tree, its depend on our way to make tree
    * ordinal attributes used to make tree for discret adjectives
    * continuos attributes used to make tree with discretization(binary/multi-way split)

    
### learning decision tree
base algorithm of decision tree is named CLS(concept learning system) 
- Greedy
- ID3 Inducing Decision trees
    - top-to-down
    - Greedy
    - minimal tree to detecting consistently of new samples correctly
    - we like less deep
    - if we have M property, deep of tree is M maximum
    - using labeled samples
    - information gain(search formula)
    - entropy(search formula)
- C4.5
    - spilt info
    - gain ration
    - gini index

### preventing over fitting
(noise, low training data, too big data, bad training and test dataset)
 1. post pruning(offered)
    1. reduced error pruning
 2. before complete tree, stop it(its hard!)
 
  
### summary
0. decision tree is a way to classification
    - good speed
    - prevent again noise
    - need too much data
1. create classification model: to describe different categories
2. using model to classification: to classify new data
3. see pic2 and pic3
4. we have three index to compare:
    1. information gain
    2. gain ratio
    3. gini index
- over fitting is dangerous!