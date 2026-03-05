import csv
import itertools
from typing import Dict, List, Set, Tuple, Optional

def load_dataset(path: str) -> Tuple[List[str], Dict[str, str], Set[Tuple[str, str]]]:
    students: List[str] = []
    city: Dict[str, str] = {}
    friends: Set[Tuple[str, str]] = set()

    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["Student"].strip()
            students.append(name)
            city[name] = row["City"].strip()

            raw_friends = row["Friends"].strip().strip('"')
            if raw_friends:
                for fr in raw_friends.split(";"):
                    fr = fr.strip()
                    if fr:
                        friends.add((name, fr))  # directed pair
    return students, city, friends

def valid_adj(a: str, b: str, city: Dict[str, str], friends: Set[Tuple[str, str]]) -> bool:
    if (a, b) in friends or (b, a) in friends:
        return False
    if city[a] == city[b]:
        return False
    return True

def valid_arrangement(arr: Tuple[str, ...], city: Dict[str, str], friends: Set[Tuple[str, str]]) -> bool:
    return all(valid_adj(arr[i], arr[i+1], city, friends) for i in range(len(arr)-1))

def brute_force(students: List[str], city: Dict[str, str], friends: Set[Tuple[str, str]]) -> Tuple[Optional[Tuple[str, ...]], int]:
    checked = 0
    for perm in itertools.permutations(students):
        checked += 1
        if valid_arrangement(perm, city, friends):
            return perm, checked
    return None, checked

def constraint_degree(s: str, students: List[str], city: Dict[str, str], friends: Set[Tuple[str, str]]) -> int:
    friend_count = sum(1 for x in students if (s, x) in friends or (x, s) in friends)
    same_city = sum(1 for x in students if city[x] == city[s] and x != s)
    return friend_count + same_city

def heuristic_backtracking(students: List[str], city: Dict[str, str], friends: Set[Tuple[str, str]]) -> Optional[List[str]]:
    ordered = sorted(students, key=lambda s: constraint_degree(s, students, city, friends), reverse=True)

    def backtrack(arr: List[str], used: Set[str]) -> Optional[List[str]]:
        if len(arr) == len(students):
            return arr

        for s in ordered:
            if s in used:
                continue
            if not arr or valid_adj(arr[-1], s, city, friends):
                used.add(s)
                res = backtrack(arr + [s], used)
                if res:
                    return res
                used.remove(s)
        return None

    return backtrack([], set())

if __name__ == "__main__":
    dataset_path = "dataset_task2.csv"
    students, city, friends = load_dataset(dataset_path)

    print("=== TASK 2: Classroom Seating Arrangement Solver ===")
    print("Students:", students)
    print("Cities:", city)
    print("Friend constraints:", sorted(list(friends)))
    print()

    bf_ans, bf_checked = brute_force(students, city, friends)
    print("--- Brute Force ---")
    print("Checked permutations:", bf_checked)
    print("Valid arrangement:", bf_ans)
    print()

    h_ans = heuristic_backtracking(students, city, friends)
    print("--- Heuristic (Backtracking + Most-Constrained-First) ---")
    print("Valid arrangement:", h_ans)
