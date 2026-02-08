# Data types

## 🧩 What are data types?

A **data type** tells Python:

* what kind of value you’re storing
* what operations you can perform on it

```python
x = 10
```

Python knows `x` is an **integer**, so math is allowed.

## 🔑 Main Built-in Data Types (Beginner → Data Science)

### 1️⃣ Numeric Types

#### 🔹 `int` — Integer

Whole numbers (positive or negative)

```python
a = 10
b = -5
```

#### 🔹 `float` — Decimal numbers

```python
x = 3.14
y = 10.0
```

#### 🔹 `complex` — (advanced, rarely used)

```python
z = 3 + 4j
```

📌 **Data science uses mostly `int` & `float`**

### 2️⃣ `str` — String (Text)

Used for text data.

```python
name = "Ananya"
city = 'Delhi'
```

* Strings are **immutable**
* Indexing starts from `0`

```python
print(name[0])  # A
```

### 3️⃣ `bool` — Boolean

Only two values:

```python
True
False
```

```python
is_active = True
print(10 > 5)  # True
```

Used heavily in **conditions & filtering**.

## 🗂️ Collection Data Types

### 4️⃣ `list` — Ordered & Mutable

```python
nums = [1, 2, 3, 4]
nums[0] = 100
```

✔ Can change
✔ Allows duplicates
✔ Very common in data work

### 5️⃣ `tuple` — Ordered & Immutable

```python
point = (10, 20)
```

❌ Cannot change values
✔ Faster & safer than lists

### 6️⃣ `set` — Unordered & Unique

```python
unique_nums = {1, 2, 3, 3}
print(unique_nums)  # {1, 2, 3}
```

✔ Removes duplicates automatically
❌ No indexing

### 7️⃣ `dict` — Key-Value Pairs ⭐

```python
student = {
    "name": "Ananya",
    "age": 22,
    "course": "Data Science"
}
```

* Access using keys

```python
print(student["name"])
```

📌 **Extremely important for APIs, JSON, data processing**

## 🧪 Special Data Type

### 8️⃣ `NoneType`

```python
x = None
```

* Means “no value yet”
* Common in functions & missing data

## 🔍 Check data type

```python
x = 10
print(type(x))
```

Output:

```python
<class 'int'>
```

## ⚠️ Very Common Beginner Mistake

```python
age = input("Enter age: ")
print(type(age))   # str ❌
```

Fix:

```python
age = int(input("Enter age: "))
```

## 🧠 Mutability (VERY important)

| Type  | Mutable? |
| ----- | -------- |
| int   | ❌       |
| float | ❌       |
| str   | ❌       |
| list  | ✅       |
| tuple | ❌       |
| set   | ✅       |
| dict  | ✅       |

## 🎯 Data Science Focus (Remember this)

| Purpose         | Data Type      |
| --------------- | -------------- |
| Numbers         | `int`, `float` |
| Text            | `str`          |
| Rows of data    | `list`         |
| Unique values   | `set`          |
| Structured data | `dict`         |
| Missing values  | `None`         |

Later you’ll meet:

* `numpy.ndarray`
* `pandas.Series`
* `pandas.DataFrame`

(built **on top of these basics**)

## 📝 Mini Practice

```python
x = 10
y = "5"
z = [1, 2, 3]

print(type(x))
print(type(y))
print(type(z))
```

## **list vs tuple vs set**

## 🧺 1️⃣ List

### What it is

An **ordered**, **mutable** collection that allows **duplicates**.

```python
nums = [1, 2, 3, 3]
```

### Key features

* ✅ Ordered (index-based)
* ✅ Mutable (can change)
* ✅ Allows duplicates
* ✅ Most commonly used

```python
nums[0] = 100
nums.append(4)
```

### When to use

* When data **changes**
* Storing rows of data
* Iteration & indexing needed

## 📦 2️⃣ Tuple

### What it is

An **ordered**, **immutable** collection that allows **duplicates**.

```python
point = (10, 20)
```

### Key features

* ✅ Ordered
* ❌ Immutable (cannot change)
* ✅ Allows duplicates
* ⚡ Faster than list

```python
# point[0] = 50  ❌ ERROR
```

### When to use

* Fixed data (coordinates, config)
* Data should **not be modified**
* Used as dictionary keys

## 🎯 3️⃣ Set

### What it is

An **unordered**, **mutable** collection of **unique values**.

```python
nums = {1, 2, 3, 3}
```

Output:

```python
{1, 2, 3}
```

### Key features

* ❌ Not ordered
* ❌ No indexing
* ✅ Mutable
* ❌ No duplicates

```python
nums.add(4)
```

### When to use

* Removing duplicates
* Membership testing
* Mathematical operations

## 🧠 Side-by-Side Comparison

| Feature           | List   | Tuple | Set   |
| ----------------- | ------ | ----- | ----- |
| Syntax            | `[ ]`  | `( )` | `{ }` |
| Ordered           | ✅     | ✅    | ❌    |
| Mutable           | ✅     | ❌    | ✅    |
| Allows duplicates | ✅     | ✅    | ❌    |
| Indexing          | ✅     | ✅    | ❌    |
| Performance       | Medium | Fast  | Fast  |
| Use as dict key   | ❌     | ✅    | ❌    |

## 🔍 Simple Example (Same data)

```python
data_list  = [1, 2, 3, 3]
data_tuple = (1, 2, 3, 3)
data_set   = {1, 2, 3, 3}
```

Result:

```python
List  → [1, 2, 3, 3]
Tuple → (1, 2, 3, 3)
Set   → {1, 2, 3}
```

## ⚠️ Common Beginner Confusions

### ❓ Why can’t sets be indexed?

Because sets are **unordered** — Python doesn’t know which element is “first”.

### ❓ Why use tuple if list exists?

* Data safety (no accidental changes)
* Faster
* Required in some cases (dict keys)

## 🧠 Data Science Perspective

| Task              | Best Choice |
| ----------------- | ----------- |
| Dataset rows      | List        |
| Fixed columns     | Tuple       |
| Unique categories | Set         |
| Remove duplicates | Set         |
| API / config data | Tuple       |

## 📝 Mini Practice

```python
nums = [1, 2, 2, 3]

print(len(nums))
print(len(set(nums)))
```

👉 This trick is used **all the time** to find unique values.
