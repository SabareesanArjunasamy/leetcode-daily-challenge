class FreqStack:

    def __init__(self):
        self.stks = []
        self.freq = defaultdict(int)
        
    def push(self, val: int) -> None:
        self.freq[val] += 1
        if self.freq[val] > len(self.stks):
            self.stks.append([val])
        else:
            self.stks[self.freq[val]-1].append(val)
            
    def pop(self) -> int:
        while not self.stks[-1]:
            self.stks.pop()
        val = self.stks[-1].pop()
        self.freq[val] -= 1
        return val