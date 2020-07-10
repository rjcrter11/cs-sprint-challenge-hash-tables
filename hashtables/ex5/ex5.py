# Your code here


def finder(files, queries):

    cache = {}
    result = []

    for query in queries:
        if query not in cache:
            cache[query] = query

    for file in files:
        file_name = file.split('/')[-1]

        if file_name in cache:
            result.append(file)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
