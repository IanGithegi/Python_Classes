# Find diff

Find the difference between two string inputs and return the differing character

e.g:

```bash
>>> find_diff("aabbccdd", "aabbccdde")
>>> "e"
```
> Should return e, as e is the differing character

Ensure valid checks for string inputs.

## Constraints

1. Assume two strings str1, str2, where str2 contains the same set of characters in str1 with one additional character.
2. Can we assume the strings are ASCII? - Yes
3. Is case important? - The strings are lower case
4. Can we assume the inputs are valid? - No, check for None
5. Can we assume this fits memory? - Yes

Run tests with py.test:
```
py.test test_find_diff.py
```

