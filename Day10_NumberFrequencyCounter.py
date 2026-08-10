#NUMBER FREQUENCY COUNTER
from collections import Counter

numbers = [2, 3, 2, 5, 3, 2, 7, 5]

counts = Counter(numbers)

recurring_items = {
    item: count for item, count in counts.items() 
    if count > 1}


for item, count in counts.items():
    print(f"{item} → {count} time(s)")