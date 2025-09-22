import sys

def main():
    n = int(sys.stdin.readline())
    connections = list(map(int, sys.stdin.readline().split()))
    
    isPipe = [True] * n
    for i in range(n):
        if connections[i] != -1:
            isPipe[connections[i]] = False
    
    ptoc = {}
    distances = {}
    
    for i in range(n):
        if isPipe[i]:
            current = i
            distance = 0
            
            while connections[current] != -1:
                current = connections[current]
                distance += 1
            
            ptoc[i] = current
            distances[i] = distance
    
    cointopipe = {}
    for pipe, coin in ptoc.items():
        if coin not in cointopipe:
            cointopipe[coin] = []
        cointopipe[coin].append(pipe)
    
    findBestPipe = {}
    for coin, pipes in cointopipe.items():
        bestPipe = None
        bestDistance = 1000001
        bestPipeNumber = 100001
        
        for pipe in pipes:
            pipeDistance = distances[pipe]
            
            if pipeDistance < bestDistance or (pipeDistance == bestDistance and pipe < bestPipeNumber):
                bestPipe = pipe
                bestDistance = pipeDistance
                bestPipeNumber = pipe
        
        findBestPipe[coin] = bestPipe
    
    luiginum = int(sys.stdin.readline())
    luigiPipes = list(map(int, sys.stdin.readline().split()))
    
    for pipe in luigiPipes:
        coinRoom = ptoc[pipe]
        marioPipe = findBestPipe[coinRoom]
        print(marioPipe)
if __name__ == "__main__":
    main()