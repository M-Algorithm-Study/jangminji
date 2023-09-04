import sys
sys.stdin  = open('input.txt', 'r')
N = int(input())
total_evolution = 0
max_evolution = 0
max_poketmon = ""
for _ in range(N):
    pokemon = input()
    K, M = map(int, input().split())
    pokemon_evolution = 0
    while K <= M:
        M -= K
        M += 2
        pokemon_evolution += 1
    total_evolution += pokemon_evolution

    if max_evolution < pokemon_evolution:
        max_evolution = pokemon_evolution
        max_poketmon = pokemon
print(total_evolution)
print(max_poketmon)
