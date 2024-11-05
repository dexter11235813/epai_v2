from collections import defaultdict, Counter

def merge_with_defaultdict(*dicts):
    merged_dicts = defaultdict(int)

    for _dict in dicts:
        for word, freq in _dict.items():
            merged_dicts[word] += freq

    return dict(sorted(merged_dicts.items(), key=lambda x: x[1], reverse=True))

def merge_with_counter(*dicts):
    mereged_dicts = Counter()

    for _dict in dicts:
        mereged_dicts.update(_dict)

    return dict(mereged_dicts.most_common())