# def count_words(words):
#     count = 0
#     for word in words:
#         if "dan" in word.lower():
#             count += 1
#     return count


# def count_words(words):
#     count = 0
#     for word in words:
#         if "dan" in word.lower():
#             print(word, "is being counted")
#             count += 1
#     return count


def count_words(words):
    count = 0
    for word in words:
        if "dan" in word.lower():
            count += 1
    return count


def count_words(words):
    count = 0
    for word in words:
        if word.lower() == "dan":
            count += 1
    return count


def count_words(words):
    count = 0
    for word in words:
        # only count words that are exactly "Dan"
        if word == "Dan":
            count += 1
    return count


words = ["Dan", "danger", "Leo"]
print(count_words(words))
