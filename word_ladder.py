import re

#The same function is to compare the similarities between two words 
#and configure the position for each letter.
def same(item, target):
#use zip function to 
    return len([c for (c, t) in zip(item, target) if c == t])


def build(pattern, words, seen, list):
    return [word for word in words
            if re.search(pattern, word) and word not in seen.keys() and
            word not in list]


def find(word, words, seen, target, path):
    # word-> start
    list = []
    for i in range(len(word)):
        list += build(word[:i] + "." + word[i + 1:], words, seen, list)
        print(list)
    if len(list) == 0:
        return False
    list = sorted([(same(w, target), w) for w in list], reverse=True)
    print(list)
    for (match, item) in list:
        if match == len(target) -1:
            path.append(item)
            return True
        seen[item] = True
        path.append(item)
        if find(item, words, seen, target, path):
            return True
        path.pop()


    # for (match, item) in list:
    #     if match >= len(target) - 1:
    #         if match == len(target) - 1:
    #             path.append(item)
    #         return True
    #     seen[item] = True
    # for (match, item) in list:
    #     path.append(item)
    #     if find(item, words, seen, target, path):
    #         return True
    #     else:
    #         path.pop()

def find_bfs(word, words, seen, target, path):
    # word-> start

    list = []
    for i in range(len(word)):
        list += build(word[:i] + "." + word[i + 1:], words, seen, list)
        # print(list)
    if len(list) == 0:
        return False

    list = sorted([(same(w, target), w) for w in list], reverse=True)

    for (match, item) in list:
        if match == len(target) -1:
            path.append(item)
            return True
        seen[item] = True
        path.append(item)
        continue

        if find(item, words, seen, target, path):
            return True
        path.pop()


