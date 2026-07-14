from collections import defaultdict

def create_wildcard_map(word_list: list[str]) -> dict:
    wildcard_map = defaultdict(list)
    for word in word_list:
        for i in range(len(word)):
            wildcard = word[:i] + "*" + word[i+1:]
            wildcard_map[wildcard].append(word)
    return wildcard_map

if __name__ == "__main__":
    test_list = ["hot", "dot", "dog", "lot", "log", "cog"]
    result = create_wildcard_map(test_list)
    
    # Verification
    print(f"Words for *ot: {result.get('*ot')}")
    assert "hot" in result.get("*ot", []) and "dot" in result.get("*ot", []), "Mapping failed"
    print("Success: Preprocessing module verified.")