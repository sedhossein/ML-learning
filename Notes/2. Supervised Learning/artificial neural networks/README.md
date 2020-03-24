### ANI

#### intro
- Can learn everything/function
- Resistant against noises
- We can decide on connections
- Adaptation power with area changes
- Can work with minimal data
- Can learn on noisily data
- Its inspiration based on nature 
- we doing learning curve/cycle based on threshold

#### concepts
- Neurons
- Activation functions
- Feed forward network
- Recurrent network


### type of ANI Architecture
- Perceptron
    - good to linear separation
    - two learning model
    1. perceptron rule
        - change weights randomly
        - consider learning rate
    2. delta rule
        - gradient descent 
        - Back propagation(BP) Algorithm
            - compute sigmoid function
    
            
- Multi-layer perceptron(MLP)
    - more hidden internal layers, more nodes, more connection, need more time to learn, more data to learn, more power
    - over fitting is near u!
        - use validation set  based on training set
        - weight decay
        - k-fold cross validation
- Simulated annealing
- Hybrid global learning
- genetic algorithms
- recurrent network
- Radial basis function(RBF)
    - single hidden layer(radial unit)
    - gaussian 
- Hopfield 
    - face detection
    - Hebb
- Kohonen(SOM-self organizing maps)

- ...

* we need pre-process before using these data + normalization

---

### evolutionary algorithms
-  fitness function
-  select between lot of solutions
-  can process parallel
-  not guaranty to find best solution
-  using in social networks, ML, optimizations, automatic programming
- types
    - Genetic Algorithm(GA)
        - phenotype
        - genotype
        - generate population
        - with fitness function, check them. choose the best ones and make new population
        - best Hypothesises choose directly, and some of them using after crossover and mutation to make new childes 
            - crossover:
                - single point(randomly point in parent)
                - two point => mask: 0011111000
                - uniform point => mask: 1010101100101
             - mutation
                - change the one random bit in parent
        - work with bit strings
        - search
            - challenge: crowding -> solution: 1.ranking  2. fitness sharing
        - schema: evaluation population
        - 
    - Genetic Programming(GP)
        - memetic
        - layered GP-LAGEP
            - https://peaple.cs.nctu.edu.tw/~jylin/lagep/lagep.html
        - usage:
            - web mining
            - social network analyze
        
        

###  genetic
- history: 
    - Lamarck Theory
    - Baldwin Theory
- parallel:
    - demes
    - migration
    