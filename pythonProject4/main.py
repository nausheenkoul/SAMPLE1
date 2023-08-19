def longest_common_substring(str1, str2):
    m = len(str1)
    n = len(str2)

    # Create a 2D array to store the lengths of common substrings
    # dp[i][j] will store the length of common substring ending at str1[i-1] and str2[j-1]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    max_length = 0  # To keep track of the maximum length found
    end_index = 0  # To keep track of the ending index of the longest common substring

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i

    # Extract the longest common substring using its ending index and length
    longest_common_substr = str1[end_index - max_length:end_index]

    return longest_common_substr


# Example usage
str1 = "abcdef"
str2 = "acbcf"
print(longest_common_substring(str1, str2))  # Output: "bc"
