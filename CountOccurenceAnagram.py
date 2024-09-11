def search(self, pat, txt):
    start, end = 0, 0
    res = {}
    pattern = {}
    k = len(pat)
    count = 0

    # Build the frequency dictionary for the pattern
    for x in pat:
        pattern[x] = pattern.get(x, 0) + 1

    # Sliding window over the text
    while end < len(txt):
        res[txt[end]] = res.get(txt[end], 0) + 1

        # If window size is less than k, move the end pointer
        if end - start + 1 < k:
            end += 1

        # If window size is exactly k
        elif end - start + 1 == k:
            if res == pattern:
                count += 1

            # Shrink the window from the start
            if res[txt[start]] == 1:
                res.pop(txt[start])
            else:
                res[txt[start]] -= 1

            start += 1
            end += 1

    # Return the final count after processing the entire text
    return count
