# ```
# Universidade de Brasília (UnB) - Intro. Artificial Inteligence
# Marcella Pantarotto (13/0143880)
# Carlos Eduardo da Silva Andrade (19/0025905)
# ```

import random
from random import randint
import itertools

# initialIdividual is an example individual to clone, for creating the initialPopulation
# the array associated to initialIndividual is the individual's chromosome
# eache city, inside the chromosome, is a gene
initialIndividual = ["SP", "BA", "RJ", "LIMA", "BOG", "SANT", "CARAC", "BH", "POA"]
initialPopulation = []
amountPopulation = 20
iterations = 1000
tripDistPopulations = []
allGenerations = {}

SP = { 'BA': {'distance': 17},
           'RJ': {'distance': 3},
           'LIMA': {'distance': 35},
           'BOG': {'distance': 43},
           'SANT': {'distance': 26},
           'CARAC': {'distance': 44},
           'BH': {'distance': 5},
           'POA': {'distance': 8},
           'BSB': {'distance': 9}}
 
BA = { 'SP': {'distance': 17},
           'RJ': {'distance': 20},
           'LIMA': {'distance': 31},
           'BOG': {'distance': 47},
           'SANT': {'distance': 11},
           'CARAC': {'distance': 51},
           'BH': {'distance': 22},
           'POA': {'distance': 8},
           'BSB': {'distance': 23}}
 
RJ = { 'SP': {'distance': 3},
           'BA': {'distance': 20},
           'LIMA': {'distance': 38},
           'BOG': {'distance': 45},
           'SANT': {'distance': 29},
           'CARAC': {'distance': 45},
           'BH': {'distance': 3},
           'POA': {'distance': 11},
           'BSB': {'distance': 9}}
 
LIMA = { 'SP': {'distance': 35},
           'BA': {'distance': 31},
           'RJ': {'distance': 38},
           'BOG': {'distance': 19},
           'SANT': {'distance': 25},
           'CARAC': {'distance': 27},
           'BH': {'distance': 36},
           'POA': {'distance': 33},
           'BSB': {'distance': 32}}

BOG = {'SP': {'distance': 43},
           'BA': {'distance': 47},
           'RJ': {'distance': 45},
           'LIMA': {'distance': 19},
           'SANT': {'distance': 43},
           'CARAC': {'distance': 10},
           'BH': {'distance': 43},
           'POA': {'distance': 46},
           'BSB': {'distance': 37}}
 
SANT = {'SP': {'distance': 26},
           'BA': {'distance': 11},
           'RJ': {'distance': 29},
           'LIMA': {'distance': 25},
           'BOG': {'distance': 43},
           'CARAC': {'distance': 49},
           'BH': {'distance': 30},
           'POA': {'distance': 19},
           'BSB': {'distance': 30}}
 
CARAC = {'SP': {'distance': 44},
           'BA': {'distance': 51},
           'RJ': {'distance': 45},
           'LIMA': {'distance': 27},
           'BOG': {'distance': 10},
           'SANT': {'distance': 49},
           'BH': {'distance': 42},
           'POA': {'distance': 48},
           'BSB': {'distance': 35}}
 
BH = {'SP': {'distance': 5},
           'BA': {'distance': 22},
           'RJ': {'distance': 3},
           'LIMA': {'distance': 36},
           'BOG': {'distance': 43},
           'SANT': {'distance': 30},
           'CARAC': {'distance': 42},
           'POA': {'distance': 13},
           'BSB': {'distance': 6}}
 
POA = {'SP': {'distance': 8},
           'BA': {'distance': 8},
           'RJ': {'distance': 11},
           'LIMA': {'distance': 33},
           'BOG': {'distance': 46},
           'SANT': {'distance': 19},
           'CARAC': {'distance': 48},
           'BH': {'distance': 13},
           'BSB': {'distance': 16}}
 
BSB = {'SP': {'distance': 9},
           'BA': {'distance': 23},
           'RJ': {'distance': 9},
           'LIMA': {'distance': 32},
           'BOG': {'distance': 37},
           'SANT': {'distance': 30},
           'CARAC': {'distance': 35},
           'BH': {'distance': 6},
           'POA': {'distance': 16}}
 
all_distances = {
 "SP" : SP,
 "BA" : BA,
 "RJ" : RJ,
 "LIMA" : LIMA,
 "BOG" : BOG,
 "SANT" : SANT,
 "CARAC" : CARAC,
 "BH" : BH,
 "POA" : POA,
 "BSB" : BSB
}

all_generations = {
  #'index': {'list': [population], 'distance' = n},
}

# function the receives the initial chromosome array and shuffles it (shuffles the order of genes)
def shuffleChromosome(chromosome):
  random.shuffle(chromosome)

# function that creates a copy of the initial chromosome array, makes copies, shuffles the chromosome's gene order and, finally, adds this copy to the initialPopulation list
def createBrothers(individual):
  for x in range(amountPopulation):
    brother = individual[:]             # creates a new individual as a copy of the original individual
    shuffleChromosome(brother)          # changes the the chromosome, so the 2 indivuals are not clones
    initialPopulation.append(brother)   # adds the new individual to the Initial Population

# function that calculates the distance of the all trip, starting and ending at BSB, and going from one city to another
def totalTripDistance(chromosome):
  tripDistance = 0
  incomingCity = "BSB"    # initializing the trip with BSB
    
  for gene in chromosome:   # gene = city ; chromosome = array of cities
    # getting distance values from one city to another
    for x in all_distances[incomingCity][gene]:   
      tripDistance = tripDistance + int(all_distances[incomingCity][gene][x])     # adds up of distances
      incomingCity = gene   # gets the next city

      if incomingCity == chromosome[-1]:    # checks to see if it's in the last position of the array
        tripDistance = tripDistance + int(all_distances[incomingCity]["BSB"][x])  # adds up ofthe last city back to BSB

  return tripDistance

def getSmallestDistance(population):
  distances = []

  for individual in population:
    distances.append(totalTripDistance(individual))

  smallest = min(distances)
  return smallest

# function that returns the trip with the smallest trip distance
def getIndividualWtihSmallestDistance(population):
  distances = []

  # getting the distance of each individual from in a population
  for individual in population:
    distances.append(totalTripDistance(individual))

  smallest = min(distances)                       # getting the smallest distance

  smallest_position = distances.index(smallest)   # getting the index of smallest distance
  # adding BSB to the begging and to the end of the smallest distance trip
  ind = population[:][smallest_position]
  ind.insert(0,"BSB")
  ind.append("BSB")

  return ind

def getSmallestDistanceInPopulations(list):
  smallest = min(list)
  return smallest

def fitnessFunction(individual):
  # bigger the trip distance -> smaller fitness value
  # smaller the trip distance -> bigger fitness value
  fitness = 1 / (totalTripDistance(individual) + 1)
  return fitness

def tournamentSelection(population, k):
  best = None
  num_individuals = len(population)
  
  for i in range(k):
    N = random.randint(0, num_individuals-1)      # getting a random index
    individual = population[N]                    # selecting a individual from the population
    
    # using fitness function to choose the best choice of individual pick for crossover
    if (best == None) or fitnessFunction(individual) > fitnessFunction(best):
      best = individual

  return best

# function that returns a intersectons of 2 chromosomes
def intersection(chromo1, chromo2):
  # input: chromo1 -> the array of chromosome we want to remove genes from
  # input: chromo2 -> array with the genes we want to remove in chromo1

  # returns all genes in chromo1 that are not in chromo2
  return [gene for gene in chromo1 if gene not in chromo2]

# function that gets 2 random index numbers
def random_swath(list_size):
  r2 = randint(1, list_size - 1)      # get random index number for r1
  r1 = randint(0, r2 - 1)             # get random index number for r2
  return r1,r2

# function that does crossover with Order 1 operator
def order1_crossover(parent1, parent2):
  # input: parent1 -> parent used as ‘cutter'
  # input: parent2 -> parent used as ‘filler’

  i, j = random_swath(len(parent1))     # get 2 random index numbers for the crossover section
  child = []                            # new array form the child
  length = len(parent1)                 # get length of parents array (both parents have the same size)
  crossover_section = parent1[i:j+1]    # [i, j + 1) = [i, j]

  fillers = intersection(parent2, crossover_section)    # get all genes in parent2 that are not in crossover_section

  for index in range(length):
      if i <= index <= j:               # if index belongs to crossover section 
          child.insert(index, parent1[index])   # copy crossover section
      else:                             # outsise crossover section
          filler = fillers.pop(0)       # pop returns 1st gene and deletes it
          child.insert(index, filler)   # adds gene to childs

  # returns the offspring child of parent1 and parent2 that preserves relative order of symbols of the parents.
  return child  

# function that does crossover with 1 Point operator
def onePoint_crossover(individual1, individual2):
  child = []

  while len(child) < len(individual1):
    for pair in zip(individual1, individual2):  # getting pair os element[i] from both parents
      gene = random.choice(pair)                # selecting one of the pair of elements
      # making sure that child hasn't that gene already
      if (gene not in child):
        child.append(gene)  
        break
    # making sure that child is not a clone from one os the parents
    if (child == individual1) or (child == individual2):
      child = []
      continue

  return child

# function that returns a par of parent using the tournament selection function
def selectParents(): 
  x = tournamentSelection(initialPopulation, 2)   # k = 2 
  y = tournamentSelection(initialPopulation, 2)
  
  while(x == y):    # verifying that the parents are always diferent individuals
    y = tournamentSelection(initialPopulation, 2)

  return x, y

# mutation function with a
def mutation(individual, iterations):
  mutantIndividual = individual[:]
  
  # get total number of genes of the individual
  num_genes = len(mutantIndividual)
 
  for x in range(iterations):              # repeat process N times
    r1,r2 = random_swath(num_genes)        # get random index number for r2
   
    # randomise elements from r1 to r2
    for y in range(5):
      i1 = randint(r1, r2)
      i2 = randint(r1, r2)
      # swap individuals
      mutantIndividual[i1], mutantIndividual[i2] = mutantIndividual[i2],mutantIndividual[i1]
  
  return mutantIndividual

# function that creates a list of size 20 to hold a new population
def createPopulation():
  # each sublist will be an independent list and when a value is added to it, it will remain in the expected way
  newPopulation = [[] for _ in range(amountPopulation)]
  return newPopulation

# function that adds a new individual to a certain population
def addToPopulation(population, index, child):
  if population[index] != None:
    population.insert(index, child)
  del population[-1]
  return population

# function that adds new populations to the all_generations dictionary
def addToAllGeneratons(index, newPopulation, distance):
  all_generations[index] = {'population': newPopulation, 'distance': distance}
  return all_generations

def main():
  createBrothers(initialIndividual)

  # ==================================================================================================
    # ORDER 1 CROSSOVER: to generate 10 individuals and mutation to generate 10 more

  for it in range(iterations):
    newPopulation_order1 = createPopulation()
    half = int(amountPopulation / 2)

    for i in range(half):
      x, y = selectParents()
      child = order1_crossover(x,y)
      addToPopulation(newPopulation_order1, i, child)
      child_mutated = mutation(child, 10)
      addToPopulation(newPopulation_order1, i+(half-9), child_mutated)

    tripDistPopulations.append(getSmallestDistance(newPopulation_order1))
    addToAllGeneratons(it, newPopulation_order1, getSmallestDistance(newPopulation_order1)) 

  print("The best solution with Order 1 Crossover + Mutation is:")
  print("Trip: ", getIndividualWtihSmallestDistance(newPopulation_order1))
  print("Distance: ", getSmallestDistanceInPopulations(tripDistPopulations), "x10² KMs")

# ==================================================================================================
  #  1 POINT CROSSOVER: to generate 10 individuals and mutation to generate 10 more

  for it in range(iterations):
    newPopulation_1point = createPopulation()
    half = int(amountPopulation / 2)

    for i in range(half):
      x, y = selectParents() 
      child = onePoint_crossover(x ,y)
      addToPopulation(newPopulation_1point, i, child)
      child_mutated = mutation(child, 10)
      addToPopulation(newPopulation_1point, i+(half-9), child_mutated)
      
    tripDistPopulations.append(getSmallestDistance(newPopulation_1point))
    addToAllGeneratons(it, newPopulation_1point, getSmallestDistance(newPopulation_1point)) 

  print("\nThe best solution with 1 Point Crossover + Mutation is:")
  print("Trip: ", getIndividualWtihSmallestDistance(newPopulation_1point))
  print("Distance: ", getSmallestDistanceInPopulations(tripDistPopulations), "x10² KMs")

  # ==================================================================================================

if __name__ == '__main__': # calling main function
  main()     # function call