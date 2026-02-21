import analytics
#Please modify the below functions so they fulfill the described process.
#You must use a function from analytics.py in each question to receive credit.
#There is no provided test file. You must make and submit one yourself. (check older test files for reference)


# Modify the below function such that it takes in a list of prices and returns that list with 15% added value
def process_expenses(rawPrices : list):
    for i in range(len(rawPrices )):
        rawPrices[i] = analytics.apply_markup(rawPrices[i], 0.15)
    return rawPrices

# Modify the below function such that it asks the user for n scores and then returns the highest score and the average score of the list.
def analyze_scores(n):
    high = analytics.get_highest(n)
    avg = analytics.get_average(n)
    return high, avg

# Modify the below function such that it takes in a list of strings and returns that list with all spaces removed
#and all letters lower case.
def sanitize_usernames(words : list):
    li = analytics.clean_text(words)
    return li

# Modify the list such that it takes in a list as an argument and returns a version of the list with all values over 100.
def identify_outliers(numbers : list):
    filtered = analytics.filter_threshold(numbers, 100)
    return filtered

# Modify the below function such that it takes in a list of items and asks the user for an item to search for.
#Sanitize the list to only be lower case words with no extra spaces
#Then return the location of the word using binary search if the list is in order and linear search if it is not.
#example items = ["  Apple", "Banana ", "  CHERRY  ", " date "]
def search_and_report(list, target):
    newList = sanitize_usernames(list)
    if all(newList[i] <= newList[i + 1] for i in range(len(newList) - 1)) == True:
        up = len(newList) - 1
        low = 0
        while low <= up:
            mid = (up + low) // 2
            if newList[mid] == target:
                return mid
            elif target < newList[mid]:
                up = mid - 1
            elif target > newList[mid]:
                low = mid + 1
        return -1
    else:
        counter = 0
        for i in newList:
            if i == target:
                return counter
            else:
                counter += 1
        return -1
