def main():

    data = [60, 1, 88, 10, 100]
    term = 10

    result = unordered_search(data, term)
    print(result)

def unordered_search(data, term):
    for index in range(len(data)):
        if data[index] == term:
            return index
    return

main()
