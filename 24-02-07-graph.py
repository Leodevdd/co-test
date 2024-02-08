from collections import defaultdict

graph = defaultdict(list)

graph = {
    1: [3],
    2: [3, 4],
    3: [1, 2, 4, 5],
    4: [2, 3, 5],
    5: [3, 4]
}
