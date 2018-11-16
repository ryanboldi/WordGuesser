#Written by Ryan Boldi
import random

geneSet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
target = "Hello World!"
targetLen = len(target)
popSize = 10
#prob that letter will be random not crossover
mutationRate = 0.05
#how many random words in every population
randomness = 0

bestWord = ""
bestFit  = 0

def randomGene():
    #makes one random gene (word)
    gene = "".join([random.choice(geneSet) for i in range (targetLen)])
    return gene

def randomLetter():
    #gives only one random letter
    return (random.choice(geneSet))

def getFitness(word):
    #gets the fitness for any given word
    return sum(1 for expected,actual in zip (target, word) if expected == actual)

def makePop():
    #makes a population of random words of size popSize
    words = [randomGene() for i in range(popSize)]
    return words

def evalPopFits(words):
    #returns an array of fitnesses for the array of words given
    fits = []
    for i in words:
        fits.append(getFitness(i))
    return fits

def sort(words,fits):
    #sorts words based on their fitnesses (best first)
    sort = [x for _,x in sorted(zip(fits,words))]
    return sort[::-1]

def breed(words):
    #takes the top highest word fitnesses and breeds them using crossover
    newWords = []
    #the other 2 will be random new words
    for i in range(popSize-randomness):
        newWord = []
        for j in range (targetLen):
            if random.random() < mutationRate:
                newWord.append(randomLetter())
            else:
                newWord.append(random.choice(words)[j])
        newWords.append("".join(newWord))
    return newWords

def getNewPop(Pop):
    #gets a new Pop, after mutation and crossover
    new = sort(Pop, evalPopFits(Pop))
    new = breed(new[:2])
    [new.append(randomGene()) for i in range(randomness)]
    return new
    
def getBestWord(Pop):
    #gets the best word from each Pop, and keeps track of the global best word
    global bestFit
    global bestWord
    
    best = -1
    word = ""

    for i in (Pop):
        if getFitness(i) > best:
            print(i)
            word = i
            best = getFitness(i)
            if getFitness(i) > bestFit:
                bestWord = i
                bestFit = getFitness(i)
    return word
                

def main():
    Pop = makePop()
    count = 0
    while bestWord != target:
        count += 1
        Pop = getNewPop(Pop)
        #print(getBestWord(Pop))
        getBestWord(Pop)   
    
    print("Only took " + str(count) + " Tries")
    
if __name__ == "__main__":
    main()
        

    