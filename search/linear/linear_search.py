def main():

    data = [60, 1, 88, 10, 100]
    term = 60

    result = unordered_search(data, term)
    print(result)

def unordered_search(data, term):
    for item in range(len(data)):
        if data[item] == term:
            return item
    return

main()
