list_of_Fav = ['machine learning', 'cyber security', 'data analysis', 'full stack developer', 'flask', 'react dev']

fav = []
done = 'no'

while True:
    # Display the list with indices
    print("\nAvailable Options:")
    for index, ele in enumerate(list_of_Fav):
        print(f"{index}: {ele}")

    try:
        # Prompt the user for their favorite item index
        get_fav = int(input('Enter the number of your favorite element: '))
        if 0 <= get_fav < len(list_of_Fav):
            fav.append(list_of_Fav[get_fav])
        else:
            print("Invalid number, please choose a valid index.")
            continue
    except ValueError:
        print("Please enter a valid number.")
        continue

    # Ask if the user is done
    done = input('Are you done? (yes/no): ').strip().lower()
    if done == 'yes':
        break
    elif done != 'no':
        print("Invalid input, assuming 'no'.")

# Filter the list_of_Fav to include only the items in fav
list_of_Fav = [item for item in list_of_Fav if item in fav]

# Display the final results
print(f"\nFavorite items: {fav}")
print(f"Changed original list: {list_of_Fav}")
