from typing import List

Vector = List[float]

height_weight_age = [70, 170, 40] #인치, 파운드, 나이
grades = [95,80,75,62] #점수1, 점수2, 점수3, 점수4

def add(v:Vector, w:Vector) -> Vector:
    print(type(v) ,type(w))
    assert len(v) == len(w), "vectors must be the same length"
    return [v_i + w_i for v_i, w_i in zip(v,w)]

assert add([1,2,3],[4,5,6]) == [5,7,9]

def subtract(v: Vector, w: Vector)-> Vector:
    assert len(v) == len(w), "vectors must be the same length"
    return [v_i - w_i for v_i, w_i in zip(v,w)]

assert subtract([5,7,9],[4,5,6]) == [1,2,3]

def vector_sum(vectors: List[Vector]) -> Vector:
    assert vectors, "no vectors provided!" # vectors가 비어있는지 확인
    
    # 모든 벡터의 길이가 동일한지 확인
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "different sizes!"
    
    return [sum(vector[i] for vector in vectors)
            for i in range(num_elements)]
    
assert vector_sum([[1,2],[3,4],[5,6],[7,8]]) == [16,20]



def scalar_multiple(c: float, v:Vector) -> Vector:
    return [c * v_i for v_i in v]
    
assert scalar_multiple(2,[1,2,3])==[2,4,6]


def vector_mean(vectors: List[Vector]) -> Vector:
    n = len(vectors)
    return scalar_multiple(1/n, vector_sum(vectors))

assert vector_mean([[1,2],[3,4],[5,6]]) == [3,4]

    
def dot(v: Vector, w: Vector) -> float:
    assert len(v) == len(w), "vectors must be same length"
    return sum(v_i * w_i for v_i, w_i in zip(v,w))

assert dot([1,2,3],[4,5,6]) == 32


def sum_of_squares(v: Vector) -> float:
    return dot(v,v)

assert sum_of_squares([1,2,3]) == 14

import math

def magnitude(v: Vector) -> float:
    return math.sqrt(sum_of_squares(v))

assert magnitude([3,4])==5


def squared_distance(v: Vector, w: Vector) -> float:
    return sum_of_squares(subtract(v,w))


def distance(v: Vector, w: Vector) -> float:
    return magnitude(subtract(v,w))


Matrix = List[List[float]]

A = [[1,2,3],
     [4,5,6]]

b = [[1,2],
     [3,4],
     [5,6]]

from typing import Tuple

def shape(A: Matrix) -> Tuple[int, int]:
    #열의 개수, 행의 개수를 반환
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

assert shape([[1,2,3],[4,5,6]]) == (2,3) # 2* 3 



def get_row(A: Matrix, i: int) -> Vector:
    return A[i]

def get_column(A: Matrix, j: int ) -> Vector:
    return [A_[i] for A_i in A]

from typing import Callable

def make_matrix(num_rows: int, 
                num_cols: int,
                entry_fn: Callable[[int, int], float]) -> Matrix:
    return [[entry_fn(i,j)
             for j in range(num_cols)]
             for i in range(num_rows)]
    
def identity_matrix(n: int) -> Matrix:
    return make_matrix(n,n,lambda i, j: 1 if i==j else 0)

assert identity_matrix(5) == [[1,0,0,0,0],
                              [0,1,0,0,0],
                              [0,0,1,0,0],
                              [0,0,0,1,0],
                              [0,0,0,0,1]]

friendships = [(0,1),(0,2),(1,2),(1,3),(2,3),(3,4),
               (4,5),(5,6),(5,7),(6,8),(7,8),(8,9)]

