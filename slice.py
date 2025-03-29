def solution(A, K):
    if not A:  # Handle empty array
        return A
    
    N = len(A)
    K = K % N  # Optimize rotations
    print(K % N )
    print(A[-K:])
    print(A[:-K] )
    
    return (A[-K:], A[:-K])  # Right rotate using slicing



def main():
    ans = solution(A, K)
    return ans


if __name__ == "__main__":
    main()