def skip_elements(elements):
    # Initialize variables
    new_list = []
    i = 0
    for x in elements:
        if elements[i] == x:
            # Add this element to the resulting list
            new_list.append(x)
            # Increment i
            i += 2
    return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []


