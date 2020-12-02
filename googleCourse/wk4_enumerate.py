def skip_elements(elements):
    results = []
    for index, elem in enumerate(elements):
        if index % 2 == 0:
            results.append(elem)
    return results


print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))  # Should be ['a', 'c', 'e', 'g']
print(skip_elements(
    ['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))  # Should be ['Orange', 'Strawberry', 'Peach']
