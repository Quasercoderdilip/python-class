# class sorting_operations : 
#     def __init__(self):
#         print('you can sort the list here');

#     def manual_sorted_ans(self,get_val):#this function is using bubble sort algorithm.
#         self.len_arr = len(get_val)

#         for i in range(self.len_arr):
#             for j in range(0, self.len_arr - i - 1):
#                 if get_val[j] > get_val[j + 1] :
#                     get_val[j], get_val[j+1] = get_val[j+1], get_val[j]

#         return get_val;

#     def sorted_ans(self,get_val):
#         self.sorted_list = sorted(get_val)#built-in sort method.
#         return self.sorted_list;

# storage = [];

# done = 'no'
# while done == 'no' :
#     goal = str(input('enter your goal : '));
#     storage.append(goal);
#     done = str(input('Are you done ? (yes/no)')).strip();


# store = sorting_operations();
# print(store.sorted_ans(storage));


class SortingOperations:
    def __init__(self):
        print("Welcome! You can sort your goals efficiently here.")

    @staticmethod
    def builtin_sort(get_val):
        """Efficiently sorts the list using Python's built-in Timsort."""
        return sorted(get_val)


def collect_goals():
    """Collects goals from the user with minimal memory overhead."""
    storage = []
    while True:
        goal = input("Enter your goal: ").strip()
        if goal:
            storage.append(goal)
        done = input("Are you done? (yes/no): ").strip().lower()
        if done == "yes":
            break
    return storage


def main():
    # Collect user input
    storage = collect_goals()

    # Create a sorting operations instance
    sorter = SortingOperations()

    # Sort the goals using Python's built-in method
    sorted_storage = sorter.builtin_sort(storage)

    # Display the sorted list
    print("\nSorted goals:", sorted_storage)


if __name__ == "__main__":
    main()





