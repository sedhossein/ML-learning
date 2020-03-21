Reference-style: 
![alt text][logo]
[logo]: https://wordstream-files-prod.s3.amazonaws.com/s3fs-public/styles/simple_image/public/images/machine-learning1.png?SnePeroHk5B9yZaLY7peFkULrfW8Gtaf&itok=yjEJbEKD what is ML

---
### Meaning
mitchel(1997):
`A computer program is said to LEARN from experience E with respect to some class of tasks T and performance measure P, if its performance at tasks in T, as measured by P, improves with experience E`

Witten and Frank(2000):
`Things learn when they change their behavior in a way that makes them perform better in the future`

##### So 2 things is main:
1. getting (better/more perforce) after learning
2. getting experiment

---
#### 3 main ways in ML
- data mining
- implement complex systems like (auto driving, voice detection)
- self learning systems like recommended systems


### Why machine learning
- better performance, better choosing
- unknown atmosphere
- make complex systems
- too many devices, too many data, too many information

--- 
### Types of learning
- incremental / Batch
- online / Offline
- Inductive / Deductive
- Symbolic / Numerical

### Evaluation the leaning algorithms
- accuracy
- truth of solution and quality 
- order time

### type of algorithms of learning
- Supervised Learning
    1. Classification
    2. Regression
- Unsupervised Learning
    1. clustering
- Semi-supervised learning
    1. Reinforcement learning
    
##### some sample of learning ways:
1. Inductive Learning => (decision trees, Supervised)
2. Connectionist Learning => (AN)
3. Bayesian Learning => (based on statistics and probabilities)
4. Reinforcement Learning => (based on experiment with power of semi-supervised)
5. Evolutionary Learning => (genetic algorithms)

---



(We could find Hypothesis function) H: x-> y

####  Supervised Learning:
   - Regression (If H was Continuously data)
   - Classification (If H was Discrete data)

---

## design learning system
1. choose type of experience for learning(direct or indirect)
2. choose our expectation(is it a function? a rule? a grammar? a model? ...)
3. choose Manner to display
4. choose learning algorithm
5. Evaluation criteria
6. basic knowledge from environment

### choose type of experience for learning
- Direct, like determination the suitable of each action in Chess based on current situation
- Indirect, like collection of action continuous in chess and found their value
##### indirect problems(in Chess example):
- Credit Assignment:
too difficult and beinig historical, its not in single step.
almost learning with Direct feedback is more simple.

### choose Manner to display
- based on logical sentences (make rules)
    - C <= x^y^z
- attribute-value language (each property has special value)
    - L-{(a1, v1)^(a2, v2)^....^(an,vn)}
- explicit constrained language
- grammar, network, templates


### learner control on sample dataset
- with a handler/coach
- the learner ask right decision from coach  
- without coach the learner do learning itself randomly

#### Tips
1. `=>` our sample data for learning could be like production actions, not in special states
2. `=>` choosing Hypothesis function is a trade of between accuracy and sample data counts. to getting same the Hypothesis like actual function, we need more dataset to learn.


### Some Good Questions to learn
1. for ht special issue, from which algorithm could use?
2. how much training data for learning is needed? 
3. how choosing next training data
4. how the nosily data, have effect on learning accuracy
5. what are the learning power limitations?
6. how basic knowledge help tp learning ?
