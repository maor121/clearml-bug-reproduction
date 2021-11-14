"""
An auxiliary script implementing a minimal multiprocessing example(s) for
testing.
"""

import multiprocessing

def run():
    pool = multiprocessing.Pool(2)
    results = pool.map(str, [1, 2, 3, 4])
    pool.close()
