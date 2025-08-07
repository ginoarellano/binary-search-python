# 🔎 Binary Search in Python

A beginner-friendly Python script that demonstrates how binary search works on a sorted list.

---

## 📌 Details

**Author**: Gino Arellano  
**Course**: SBIT-3H  
**Language**: Python  
**Topic**: Binary Search Algorithm

---

## 🧠 How It Works

- You define a sorted list: `[1, 2, 3, 4, 5, 6]`
- The program asks the user to input a number to search
- It uses the binary search algorithm to find the number’s index
- Returns the result

---

## 💻 Code Snippet

```python
Enter the number you want to search for: 4  
Found 4 at index 3

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1```

