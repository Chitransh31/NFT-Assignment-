# Neuro Fuzzy Techniques Assignment
Supervised learning using Error Back Propagation(Extended delta rule).
seeds_dataset.txt contains my dataset.
finaldatasettrain_merge.txt is my training set which is a subset of my dataset.
test2.txt is my testing set which is also a subset of my dataset.
main.py contains the actual code.

Problem Statement:
https://archive.ics.uci.edu/ml/datasets/seeds
Measurements of geometrical properties of kernels belonging to three different varieties of wheat. A
soft X-ray technique and GRAINS package were used to construct all seven, real-valued attributes.
Data Set Information:
The examined group comprised kernels belonging to three different varieties of wheat: Kama,
Rosa and Canadian, 70 elements each, randomly selected for
the experiment. High quality visualization of the internal kernel structure was detected using a
soft X-ray technique. It is non-destructive and considerably cheaper than other more
sophisticated imaging techniques like scanning microscopy or laser technology. The images were
recorded on 13x18 cm X-ray KODAK plates. Studies were conducted using combine harvested
wheat grain originating from experimental fields, explored at the Institute of Agrophysics of the
Polish Academy of Sciences in Lublin.
The data set can be used for the tasks of classification and cluster analysis.

Attribute Information:
To construct the data, seven geometric parameters of wheat kernels were measured:
1. area A,
2. perimeter P,
3. compactness C = 4*pi*A/P^2,
4. length of kernel,
5. width of kernel,
6. asymmetry coefficient
7. length of kernel groove.
All of these parameters were real-valued continuous.

Modify your program so that it can read patterns from a file. Then test your network
by training it with the delta rule on some subset of the data, until the error measure
drops below some acceptable threshold. How well is it able to classify the training
data? Next, test the network&#39;s generalization ability by testing it on patterns from the
data set that were not included in the training data. Does it still produce correct
classifications for these novel patterns? Experiment with different sizes of
training/testing sets, different termination thresholds, and different learning rates.
