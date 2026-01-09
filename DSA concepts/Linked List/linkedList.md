# Linked Lists: A Comprehensive Guide 🔗

## Table of Contents
1. [Introduction](#introduction)
2. [Why Linked Lists?](#why-linked-lists)
3. [Basic Concepts](#basic-concepts)
4. [Types of Linked Lists](#types-of-linked-lists)
5. [Advantages & Disadvantages](#advantages--disadvantages)
6. [Common Operations](#common-operations)
7. [Code Examples](#code-examples)

---

## Introduction

A **Linked List** is a linear data structure where elements (called nodes) are connected using pointers/references. Unlike arrays, linked lists don't store elements in contiguous memory locations.

### Key Idea:
```
Array:     [10] [20] [30] [40]  (contiguous memory)

Linked List:  [10|→] → [20|→] → [30|→] → [40|→] → None
```

---

## Why Linked Lists?

| Feature | Array | Linked List |
|---------|-------|-------------|
| **Access Time** | O(1) ⚡ | O(n) |
| **Insertion** | O(n) | O(1) * |
| **Deletion** | O(n) | O(1) * |
| **Memory** | Fixed size | Dynamic size |
| **Cache Friendly** | Yes ✓ | No ✗ |

*Once you have a reference to the position

---

## Basic Concepts

### Node Structure
Each node in a linked list contains:
- **Data**: The actual value
- **Next pointer**: Reference to the next node (None for last node)

```
┌─────────────┬──────┐
│   Data      │ Next │
├─────────────┼──────┤
│     10      │ ●    │ → Points to next node
└─────────────┴──────┘
```

---

## Types of Linked Lists

### 1️⃣ **Singly Linked List**
Each node points to the next node. Can only traverse forward.

```
Head → [10|→] → [20|→] → [30|→] → None
```

### 2️⃣ **Doubly Linked List**
Each node points to both next and previous nodes. Can traverse both ways.

```
Head ↔ [10|↕] ↔ [20|↕] ↔ [30|↕] ↔ None
```

### 3️⃣ **Circular Linked List**
The last node points back to the first node, forming a circle.

```
    ┌──────────────────────┐
    │                      ↓
    [10|→] → [20|→] → [30|→]
```

---

## Advantages & Disadvantages

### ✅ Advantages
- **Dynamic Size**: Grows and shrinks as needed
- **Efficient Insertions/Deletions**: O(1) when position is known
- **Flexible Memory**: Uses memory only as needed
- **No Wasted Space**: No pre-allocated unused memory

### ❌ Disadvantages
- **No Random Access**: Must traverse from head to reach an element
- **Extra Memory**: Needs storage for pointers
- **Cache Unfriendly**: Nodes scattered in memory
- **Complexity**: More complex than arrays

---

## Common Operations

| Operation | Time Complexity | Space Complexity |
|-----------|-----------------|------------------|
| **Access by Index** | O(n) | O(1) |
| **Insert at Head** | O(1) | O(1) |
| **Insert at Position** | O(n) | O(1) |
| **Delete from Head** | O(1) | O(1) |
| **Delete from Position** | O(n) | O(1) |
| **Search** | O(n) | O(1) |
| **Reverse** | O(n) | O(1) or O(n)* |

*O(1) if done in-place, O(n) if using recursion

---

## Code Examples

All code examples are implemented in separate Python files for better understanding. See the examples directory for:

1. **01_singly_linked_list.py** - Basic singly linked list implementation
2. **02_singly_operations.py** - Common operations on singly linked lists
3. **03_doubly_linked_list.py** - Doubly linked list implementation
4. **04_circular_linked_list.py** - Circular linked list implementation
5. **05_common_problems.py** - Real-world problems and solutions

---

## Quick Reference

### When to Use Linked Lists?
✓ When you need frequent insertions/deletions  
✓ When size is unknown upfront  
✓ When you don't need random access  

### When NOT to Use Linked Lists?
✗ When random access is needed frequently  
✗ When cache performance is critical  
✗ Simple cases where arrays work fine  

---

**Happy Learning!** 🚀
