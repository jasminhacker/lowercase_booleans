# Lowercase Booleans

Have you ever felt the need to use `true` and `false` in your Python program? Then this is the perfect module for you! 

## Installation
```
pip install lowercase_booleans
```

## Usage
Just add this to the top of your Python file:
```
from lowercase_booleans import true, false
```
That's it, now you are good to go. Use lowercase booleans to your hearts content.

```
from lowercase_booleans import true, false


def contains(haystack, needle):
    for item in haystack:
        if item == needle:
            return true
    return false


print(contains(range(10), 5))
print(contains("boolean", "c"))
```

## Tests

Simply run
```
pytest test.py
```
After all, we need to make sure that true is still true and false is still false.
100% statement coverage, 100% branch coverage and even 100% path coverage, guaranteed!

(Yes, this is satire in case you were wondering.)
