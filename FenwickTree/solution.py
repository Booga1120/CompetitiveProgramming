import sys

def main():
    input = sys.stdin.buffer.read().decode('ascii')
    lines = input.split('\n')
    
    n, q = map(int, lines[0].split())
    
    fenwick = [0] * (n + 1)
    
    def update(idx, delta):
        idx += 1
        while idx <= n:
            fenwick[idx] += delta
            idx += idx & (-idx)
    
    def query(idx):
        result = 0
        while idx > 0:
            result += fenwick[idx]
            idx -= idx & (-idx)
        return result
    
    results = []
    for i in range(1, q + 1):
        parts = lines[i].split()
        op = parts[0]
        idx = int(parts[1])
        
        if op == '+':
            delta = int(parts[2])
            update(idx, delta)
        else:
            results.append(query(idx))
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()