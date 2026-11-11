def main():
    
    data = [10, 30, 100, 120, 500]
    term = 10

    location = interpolation_search(data, len(data), term)
    print(location)


def iterative_search(data, size, term):
    
    start = 0
    end = size - 1

    while start <= end:
        mid = (start + end)//2
        
        if data[mid] == term:
            return mid
        
        if data[mid] > term:
            end = mid - 1

        elif data[mid] < term:
            start = mid + 1
    return 


def interpolation_search(data, size, term):
    
    start = 0
    end = size - 1

    while start <= end:

        if data[start] == data[end]:
            if data[start] == term:
                return start
            return

        mid = start + ( (term - data[start]) * (end - start) // (data[end] - data[start]) )

        if mid < start or mid > end:
            return
        
        if data[mid] == term:
            return mid
        
        if data[mid] > term:
            end = mid - 1

        elif data[mid] < term:
            start = mid + 1
    return 


def recursive_search(data, size, term, start=0):

    end = size - 1

    if start > end:
        return

    mid = (start + end) // 2
    if data[mid] == term:
        return mid

    if data[mid] > term:
        size = mid
        return recursive_search(data, size, term, start)

    elif data[mid] < term:
        start = mid + 1
        return recursive_search(data, size, term, start)


main()
