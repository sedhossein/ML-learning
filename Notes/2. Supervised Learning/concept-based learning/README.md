# 1. Supervised 
 
## 1.1. Classification
- concept-based learning
- instance-based learning
- rule-based learning
- KNN
- Bayesian
- Decision-tree


## 1.2. Regression
- Hierarchical
- K-means


### 1.1.1 concept-based learning
- make collection of members and team them together based on labels or same properties
- find them with training machine with positive and negative sample data set
```text
c(x): X->{0,1}
if x is a member of concept, c(x)=1
if x is not a member of concept, c(x)=0
```
- learning the C(x) is: ```making H(x) function to having to get C(x)=H(x), H(x) is a Hypothesis.```

- consistent hypothesis ``` a Hypothesis is consistent if just for all of the X we have: h(x)=c(x) ```
 
- type of valid values for hypothesis is (?, 0, <exact value>), `?` means optional value, its don't care.
 `0` is not accept anything for value. and `<exact value>` is only valid value
 samples :
 ```text
<?,?,?> all positive 
<0,0,0> all negative
<?, cold, 0>
```

#### concepts:
- version graph `(pic2 and pic3)`
- FIND-S algorithm
- candidate Elimination algorithm `(pic6, pic9)`
- consistent(h, D) `(pic7)`
- version space `(pic7, pic8)`
- list them eliminate `(pic7)`


#### summary
- instance: collection with same properties 
- target concept: the function that will be learn => C(x)
- learning output: h(x) to having  `h(x)=c(x)` for all x
- learning input: collection of x samples with target function <x,c(x)>
- collection of all hypothesises is `H`




### 1.1.2 concept-based learning


