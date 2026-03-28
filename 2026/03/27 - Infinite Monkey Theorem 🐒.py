import math

def infinite_monkey(target, attempt):
    windows = []
    similarities = []

    for i in range(len(attempt) - len(target) + 1):
        windows.append(attempt[i:i+len(target)])

    for item in windows:
        matches = 0
        for i in range(len(target)):
            if item[i] == target[i]:
                matches += 1
        
        similarity = matches / len(target) * 100
        similarities.append(similarity)

    similarity = max(similarities)
    best_index = similarities.index(similarity)

    if similarity == 0:
        attempts = None
    else:
        attempts = round((100 / similarity) ** len(target))

    return {
        "best_index": best_index,
        "similarity": round(similarity, 2),
        "attempts": attempts
    }