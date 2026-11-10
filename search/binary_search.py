def main():
    
    data = [10, 30, 100, 120, 500]
    term = 30

    location = recursive_search(data, term, 0, len(data) - 1)
    print(location)


def iterative_search(data, term):
    
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end)//2
        
        if data[mid] == term:
            return mid
        
        if data[mid] > term:
            end = mid - 1

        elif data[mid] < term:
            start = mid + 1
    return 


def recursive_search(data, term, start, end):

    if start > end:
        return

    mid = (start + end) // 2
    if data[mid] == term:
        return mid

    if data[mid] > term:
        end = mid - 1
        return recursive_search(data, term, start, end)

    elif data[mid] < term:
        start = mid + 1
        return recursive_search(data, term, start, end)


main()
