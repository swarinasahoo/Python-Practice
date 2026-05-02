def demo_adding_methods(): 
    print('1. Adding and expanding') 
    fruits = ['apple', 'banana', 'cherry']
    
    # append() : Adds element - date
    fruits.append('date')
    # extend() : Adds multiple elements - elderberry, fig
    more_fruits = ['elderberry', 'fig']
    fruits.extend(more_fruits)
    
    # insert() : Adds element at specific index - grape at index 1
    fruits.insert(1, 'grape')
    
    print(f'Final Lists : {fruits}')


def demo_removal_methods(): 
    print('2. Removing elements') 
    tools = ['hammer', 'screwdriver', 'wrench', 'pliers']
    
    # remove() : Removes first occurrence of element - date
    tools.remove('wrench')
    
    # pop() : Removes and returns element at index - index 2 (cherry)
    removed_tools = tools.pop(2)
    
    # clear() : Removes all elements from the list
    tools.clear()
    
    print(f'Removed Tools: {removed_tools}')
    print(f'Final Lists after removal: {tools}')
    
def demo_search_methods(): 
    print('3. Searching for elements')
    
    votes = ['yes', 'no', 'yes', 'maybe', 'no']

    votes.count('yes')  # count() : Returns number of occurrences of element - 'yes'
    
    no_index = votes.index('no')
    print(f'Number of "yes" votes: {votes.count("yes")}')
    print(f'First occurrence of "no" is at index: {no_index}')


def demo_organization_methods(): 
    print('4. Organizing lists') 
    numbers = [5, 2, 9, 1, 5, 6]
    
    # sort() : Sorts the list in ascending order
    numbers.sort()
    
    # reverse() : Reverses the order of the list
    numbers.reverse()
    
    # copy() : Creates a shallow copy of the list
    numbers_copy = numbers.copy()
    
    print(f'Sorted and Reversed Numbers: {numbers}')
    print(f'Copy of Numbers: {numbers_copy}')


# Command to run all the methods in the script
if __name__ == "__main__":
    demo_adding_methods()
    print('---')
    demo_removal_methods()
    print('---')
    demo_search_methods()
    print('---')
    demo_organization_methods()