def main():

    data = [60, 1, 88, 10, 100]
    term = 10

    result = ordered_search(data, term)
    print(result)

def unordered_search(data, term):
    for index in range(len(data)):
        if data[index] == term:
            return index
    return

def ordered_search(data, term):
    for index in range(len(data)):

        if data[index] == term:
            return index

        if data[index] > term:
            return
    return

main()
