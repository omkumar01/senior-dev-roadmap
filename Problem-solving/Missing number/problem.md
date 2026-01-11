# Missing Number Problem

## Problem Statement

Given an unsorted array containing `n-1` natural numbers from the range `1` to `n`, where exactly one number is missing, find and return the missing number.

## Constraints

- **Array Length**: The array contains `n-1` elements
- **Range**: Elements are from `1` to `n` (natural numbers)
- **Missing**: Exactly one number from the range is missing
- **Unsorted**: The array is not sorted
- **Duplicates**: No duplicate elements in the array

## Example

**Input**: `[1, 2, 4, 5]` (n = 5)  
**Output**: `3`

**Input**: `[3, 1, 2, 6, 4]` (n = 6)  
**Output**: `5`

## Approach Suggestions

1. **Sum Method**: Calculate the expected sum and compare with actual sum
2. **XOR Method**: Use XOR properties for efficient computation
3. **Hash Set**: Track all numbers and find the missing one
4. **Sorting**: Sort and find the gap (less efficient)