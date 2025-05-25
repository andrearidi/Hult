import random
from dataclasses import dataclass, field
from typing import List, Set

@dataclass
class SyntheticUser:
    name: str
    role: str
    needs: List[str] = field(default_factory=list)

def gather_users() -> List[SyntheticUser]:
    while True:
        try:
            count = int(input("How many synthetic users do you want to define? "))
            if count <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    users: List[SyntheticUser] = []
    for i in range(count):
        name = input(f"\nUser {i+1} name: ")
        role = input(f"User {i+1} role/expertise: ")
        user = SyntheticUser(name=name, role=role)
        while True:
            try:
                n_needs = int(input(f"How many existing needs for {name}? "))
                if n_needs < 0:
                    print("Please enter zero or a positive number.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")
        for j in range(n_needs):
            need = input(f"  - Need {j+1}: ")
            user.needs.append(need.strip())
        users.append(user)
    return users

def simulate_interactions(users: List[SyntheticUser]) -> Set[str]:
    discovered: Set[str] = set()
    for user in users:
        for other in users:
            if user is other:
                continue
            for need in user.needs:
                # Basic heuristic: pair existing needs with the other's role
                discovered_need = f"{need} for {other.role}".strip()
                discovered.add(discovered_need)
    return discovered

def main() -> None:
    print("Synthetic User Market Needs Simulator")
    users = gather_users()
    results = simulate_interactions(users)
    print("\nDiscovered market needs:")
    for r in sorted(results):
        print(f" * {r}")

if __name__ == "__main__":
    main()
