import sys
import queue

# 104,334 words

l_range = lambda b, e: list(map(chr, range(ord(b), ord(e) + 1)))
LETTERS = l_range('a', 'z') + ["'"]

def read_words(filename: str) -> set[str]:
    lines = list(open(filename).readlines())
    return set(map(str.rstrip, lines))

def neighbors(words: set[str], word: str) -> list[str]:
    ns = []
    for r in range(len(word)):
        before = word[:r]
        after = word[r + 1:]
        for l in LETTERS: # 26 * 2
            w = before + f"{l}" + after
            if w in words:
                ns.append(w)

    return ns

def bfs(words: set[str], word: str, target_word: str) -> list[str]:
    q = queue.Queue()
    parent = { word: None } # word: parent
    q.put(word)
    finished = False
    while not q.empty():
        w = q.get()

        for n in neighbors(words, w):
            if n in parent:
                continue
            else:
                parent[n] = w
                q.put(n)
                if n == target_word:
                    finished = True
                    q = queue.Queue()
                    break

    if not finished:
        return []

    # backtrack
    curr = target_word
    path = [ curr ]
    while parent[curr] is not None:
        curr = parent[curr]
        path.append(curr)

    path.reverse()
    return path

def main(args):
    filename = args[1]
    start_word = args[2]
    target_word = args[3]
    words = read_words(filename)
    path = bfs(words, start_word, target_word)
    if len(path) == 0:
        print('No solution')
        sys.exit(0)
    else:
        print(*path, sep='\n')

if __name__ == '__main__':
    args = sys.argv
    if len(args) < 4:
        # /usr/share/dict/words
        print('not enough args! expected (<dictionary>, <start word>, <target word>)')
    main(args)
