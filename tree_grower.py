# # NOT BEING USED RIGHT NOW

# import os
# # Set any environment variables to limit MKL threads
# import numpy as np
# import heapq
# import pickle as pkl
# import random
# import matplotlib.pyplot as plt
# import ensemble_factory as ef
# from sklearn import datasets

# def make_uniform_child_generator(n):
#     def uniform_child_generator():
#         while True:
#             yield n
#     return uniform_child_generator()
            
# def make_default_eval(trainx, trainy, valx, valy):
#     def default_eval(ensemble):
#         ensemble.fit(trainx, trainy)
#         return ensemble._loss(valx, valy)
#     return default_eval

# def make_mutator(mutate_prob=0.05, classifier=True):
#     mutate_with = ef.BASE_CLASSIFIERS if classifier else ef.BASE_REGRESSORS
#     def mutate(top):
#         layer = [top]
#         while len(layer) != 0:
#             new_layer = []
#             for ensemble in layer:
#                 if hasattr(ensemble, 'sub_ensembles'):
#                     new_layer.extend(ensemble.sub_ensembles)
#                     if random.random() < mutate_prob:
#                         # print("mutating")
#                         ensemble.sub_ensembles.append(random.choice(ef.BASE_CLASSIFIERS)())
#             layer = new_layer
#     return mutate

# def make_default_base_initialize(classifier=True):
#     def default_base_initialize():
#         pop = []
#         for method in (ef.BASE_CLASSIFIERS if classifier else ef.BASE_REGRESSORS):
#             pop.append(method())
#         return pop
#     return default_base_initialize

# class TreeGrower:
#     def __init__(self, evaluate, maxsize, num_child_nodes_generator, run_name='default'):
#         #self.num_features = x.shape[1]
#         #self.num_outputs = y.shape[0]
#         self.population = dict()
#         self.evaluate = evaluate
#         for member in initialize():
#             print(self.evaluate(member))
#             self.population.setdefault(self.evaluate(member), []).append(member)
#         self.crossover = crossover
#         self.mutator = mutator
#         self.num_child_nodes_generator = num_child_nodes_generator

#         self.popsize = popsize
#         self.keep = keep
#         self.run_name = run_name

#     def run(self, iters):
#         best_loss = 1e15
#         for n in range(iters):
#             parents = []
#             new_pop = dict()
#             for key in sorted(self.population):
#                 if len(parents) >= self.keep:
#                     break
#                 to_add = self.population[key][:min(self.keep-len(parents), len(self.population[key]))]
#                 new_pop[key] = to_add
#                 parents.extend(to_add)
#             if len(parents) < self.keep:
#                 pass
#             # TODO investigate other sampling methods than random sample... perhaps weighted sample?
#             for i in range(self.popsize - self.keep):
#                 parents = random.sample(parents, next(self.num_child_nodes_generator))
#                 new_child = self.crossover(random.sample(parents, next(self.num_child_nodes_generator)))
#                 self.mutator(new_child)
#                 new_pop.setdefault(self.evaluate(new_child), []).append(new_child)
#             self.population = new_pop
#             #print(n, self.population.keys())
#             if min(self.population.keys()) < best_loss:
#                 best_loss = min(self.population)
#                 print(n, "New best loss", best_loss)
#             if n % 10 == 0:
#                 pkl.dump(self.population, open(self.run_name+'-temp.pkl', 'wb'))
#                 os.rename(self.run_name+'-temp.pkl', self.run_name+'.pkl')
#         return self.population[min(self.population)]

# def unison_shuffled_copies(a, b):
#     p = np.random.permutation(len(a))
#     return a[p], b[p]

# if __name__ == "__main__":
#     is_classifier = True

#     iris = datasets.load_iris()
#     iris_x = iris.data
#     iris_y = []
#     for y in iris.target:
#         one_hot = np.zeros(3)
#         one_hot[y] = 1
#         iris_y.append(one_hot)
#     iris_y = np.array(iris_y)

#     iris_x, iris_y = unison_shuffled_copies(iris_x, iris_y)

#     genetic = Genetic(make_default_eval(iris_x[:100], iris_y[:100], iris_x[100:], iris_y[100:]), 30, 5, make_default_base_initialize(classifier=True), 
#                     make_joint_crossover([make_boost_crossover(is_classifier), make_simple_stack_crossover(is_classifier),bag_crossover], [1/3, 1/3, 1/3]),
#                     make_mutator(mutate_prob=0.05, classifier=True), make_uniform_child_generator(2), run_name='test' )
#     ens = genetic.run(5)[0]

#     ef.visualize_ensemble(ens)
#     print(ens)
#     plt.show()

