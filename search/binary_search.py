def main():
    
    data = [10, 30, 100, 120, 500]
    term = 80

    location = search(data, term)
    print(location)

def search(data, term):
    
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

main()
