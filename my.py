import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def test_sorting_algorithm(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    return end_time - start_time

def main():
    array_sizes = [100, 1000, 10000]  # различные размеры массива для тестирования
    for size in array_sizes:
        random_array = [random.randint(0, 1000) for _ in range(size)]
        
        # Сортировка пузырьком
        bubble_time = test_sorting_algorithm(bubble_sort, random_array.copy())
        print(f"Время сортировки пузырьком для массива размером {size}: {bubble_time} сек")
        
        # Сортировка слиянием
        merge_time = test_sorting_algorithm(merge_sort, random_array.copy())
        print(f"Время сортировки слиянием для массива размером {size}: {merge_time} сек")
        print()

if __name__ == "__main__":
    main()
