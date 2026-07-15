from collections import deque, defaultdict

def create_wildcard_map(word_list: list[str]):
    wildcard_map = defaultdict(list)
    for word in word_list:
        for i in range(len(word)):
            wildcard = word[:i] + "*" + word[i+1:]
            wildcard_map[wildcard].append(word)
    return wildcard_map

def ladder_length(begin_word: str, end_word: str, word_list: list[str]) -> int:
    if end_word not in word_list:
        return 0

    wildcard_map = create_wildcard_map(word_list + [begin_word])

    queue = deque([(begin_word, 1)]) 
    visited = set([begin_word]) 

    while queue:
        current_word, current_length = queue.popleft()

        # FIXED: Check target word here instead of the neighbor loop
        if current_word == end_word:
            return current_length

        for i in range(len(current_word)):
            wildcard = current_word[:i] + "*" + current_word[i+1:]
            for neighbor in wildcard_map.get(wildcard, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, current_length + 1))

    return 0


if __name__ == "__main__":
    begin_word = "hit"
    end_word = "cog"
    word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
    result = ladder_length(begin_word, end_word, word_list)
    print(f"Length of the shortest transformation sequence: {result}") # 