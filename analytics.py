def get_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def get_highest(numbers):
    return max(numbers) if numbers else 0

def apply_markup(price, percentage):
    return price * (1 + percentage)

def clean_text(words_list):
    cleaned_list = []
    for word in words_list:
        clean_word = word.strip().lower()#Deletes whitespace from each end and make lowercase
        cleaned_list.append(clean_word)
    return cleaned_list

def filter_threshold(numbers, limit):
    filtered_results = []
    for n in numbers:
        if n > limit:
            filtered_results.append(n)
    return filtered_results