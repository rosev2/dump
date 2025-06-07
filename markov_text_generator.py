import random
import sys

class MarkovChain:
    def __init__(self, n=2):
        if n < 1:
            raise ValueError("n must be >= 1")
        self.n = n
        self.model = {}

    def train(self, words):
        if len(words) < self.n:
            return
        for i in range(len(words) - self.n):
            key = tuple(words[i:i+self.n])
            next_word = words[i+self.n]
            self.model.setdefault(key, []).append(next_word)

    def generate(self, length=50):
        if not self.model:
            return ""
        start = random.choice(list(self.model.keys()))
        generated = list(start)
        for _ in range(length - self.n):
            key = tuple(generated[-self.n:])
            next_words = self.model.get(key)
            if not next_words:
                break
            generated.append(random.choice(next_words))
        return ' '.join(generated)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 markov_text_generator.py <text_file> [length] [n]", file=sys.stderr)
        sys.exit(1)
    path = sys.argv[1]
    length = int(sys.argv[2]) if len(sys.argv) > 2 else 50
    n = int(sys.argv[3]) if len(sys.argv) > 3 else 2
    with open(path, 'r', encoding='utf-8') as f:
        words = f.read().split()
    chain = MarkovChain(n)
    chain.train(words)
    result = chain.generate(length)
    print(result)

if __name__ == '__main__':
    main()
