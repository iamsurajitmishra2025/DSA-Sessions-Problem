"""
Given a list of movie lengths & the duration of flight, return a pair of 2 movies whose combined length is the highest among all other possible pairs and is less than the flight duration.
E.g,
1. MovieLenghts : [27, 1, 10, 39, 12, 52, 32, 66, 76]
    Flight Duration : 77
    Ans: [10, 66]

2. MovieLenghts : [30, 20, 50]
    Flight Duration : 70
    Ans: [30, 20]
"""


def f():
    pass

from typing import List

def find_movie_pair(movie_length: List[int], flight_duration: int):

    max_sum = 0
    n = len(movie_length)
    if n == 0: print([])
    pairs = []
    for i in range(n):
        for j in range(n):
            if movie_length[i] == 1:
                continue
            if movie_length[i] != movie_length[j]:
                sum_durations = movie_length[i] + movie_length[j]
                if sum_durations < flight_duration and sum_durations > max_sum:
                    max_sum = sum_durations
                    pairs = [movie_length[i], movie_length[j]]

    print(pairs)

def find_movie_pair_better(movie_length: List[int], flight_duration: int):
    movie_length.sort() # nlogn
    n = len(movie_length)
    i, j = 0, n-1
    pair = []
    max_sum = 0
    while i <= j:
        sum_durations = movie_length[i] + movie_length[j]
        if sum_durations >= flight_duration:
            j -= 1
        else:
            if sum_durations < flight_duration and sum_durations > max_sum:
                pair = [movie_length[i], movie_length[j]]
                max_sum = sum_durations
            i += 1

    print(pair)

find_movie_pair([30, 20, 50, 40], 70)
find_movie_pair_better([30, 20, 50, 40], 70)



