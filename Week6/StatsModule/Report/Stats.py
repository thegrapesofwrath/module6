# from Stats import Report
import matplotlib.pyplot as plt
import numpy as np
import math

class Report:

    def __init__(self,randomVariable,weights) -> None:
        self.randomVariable = randomVariable
        self.weights = weights
        self.mean = self.weightedAverage(self.randomVariable,self.weights)
        self.median = np.median(self.randomVariable)
        self.mode = max(weights)
        self.variance = self.weightedVariance(self.randomVariable,self.weights,self.mean)
        self.standardDeviation = math.sqrt(self.variance)
        self.npSkew = self.nonparametricSkew(self.mean,self.median,self.standardDeviation)
        self.pearsonsMoment = self.pearsonsMomentWeighted(self.randomVariable,self.weights,self.mean,self.standardDeviation)
    
    def __repr__(self) -> str:
        return f"""
Mean: {self.mean}\tMedian: {self.median}\tMode:{self.weights.index(self.mode)}
NonParametric Skew: {self.npSkew}
Pearsons Moment: {self.pearsonsMoment}
        """

    def weightedAverage(self,randomVariable: list, weights: list) -> float:
        sumOfWeightsAndVariables = 0
        sumOfWeights = 0
        for i in range(0,len(randomVariable)):
            sumOfWeightsAndVariables = (randomVariable[i] * weights[i]) + sumOfWeightsAndVariables
            sumOfWeights = weights[i] + sumOfWeights
        return sumOfWeightsAndVariables/sumOfWeights

    def weightedVariance(self,randomVariable: list, weights: list, mean) -> float:
        sumOfWeightsAndVariables = 0
        sumOfWeights = 0
        for i in range(0,len(randomVariable)):
            sumOfWeightsAndVariables =((randomVariable[i] - mean)**2 * weights[i]) + sumOfWeightsAndVariables
            sumOfWeights = weights[i] + sumOfWeights
        return sumOfWeightsAndVariables/sumOfWeights

    def nonparametricSkew(self,mean,median,standardDeviation) -> float:
        return (mean - median) / standardDeviation

    def pearsonsMomentWeighted(self,randomVariable: list,weights: list, mean, standardDeviation) -> float:
        return (self.weightedAverage([x**3 for x in randomVariable],[x for x in weights]) - 3*mean*standardDeviation**2 - mean**3) / standardDeviation**3