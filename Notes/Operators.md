# Operators in Python

## 1️⃣ Arithmetic Operators (Math stuff)

Used for calculations.

| Operator | Meaning             | Example  | Result |
| -------- | ------------------- | -------- | ------ |
| `+`      | Addition            | `5 + 2`  | `7`    |
| `-`      | Subtraction         | `5 - 2`  | `3`    |
| `*`      | Multiplication      | `5 * 2`  | `10`   |
| `/`      | Division            | `5 / 2`  | `2.5`  |
| `//`     | Floor division      | `5 // 2` | `2`    |
| `%`      | Modulus (remainder) | `5 % 2`  | `1`    |
| `**`     | Power               | `5 ** 2` | `25`   |

```python
a = 10
b = 3
print(a + b)
print(a % b)
```

## 2️⃣ Assignment Operators (Store values)

Used to assign or update values.

| Operator | Meaning           |
| -------- | ----------------- |
| `=`      | Assign            |
| `+=`     | Add & assign      |
| `-=`     | Subtract & assign |
| `*=`     | Multiply & assign |
| `/=`     | Divide & assign   |

```python
x = 5
x += 3   # same as x = x + 3
print(x)  # 8
```

## 3️⃣ Comparison Operators (True / False)

Used in conditions.

| Operator | Meaning          |
| -------- | ---------------- |
| `==`     | Equal            |
| `!=`     | Not equal        |
| `>`      | Greater than     |
| `<`      | Less than        |
| `>=`     | Greater or equal |
| `<=`     | Less or equal    |

```python
a = 10
b = 5
print(a > b)   # True
print(a == b)  # False
```

## 4️⃣ Logical Operators (Decision making)

Used to combine conditions.

| Operator | Meaning           |
| -------- | ----------------- |
| `and`    | Both must be True |
| `or`     | Any one True      |
| `not`    | Reverse result    |

```python
a = 10
b = 5

print(a > 5 and b > 3)   # True
print(a < 5 or b > 3)    # True
print(not(a > 5))        # False
```

## 5️⃣ Identity Operators (Same object or not)

Checks **memory identity**, not value.

| Operator | Meaning          |
| -------- | ---------------- |
| `is`     | Same object      |
| `is not` | Different object |

```python
a = 10
b = 10
print(a is b)  # True (small integers are cached)
```

⚠️ Rarely used at beginner level.

## 6️⃣ Membership Operators (Belongs to?)

Used with collections like lists, strings, tuples.

| Operator | Meaning        |
| -------- | -------------- |
| `in`     | Exists         |
| `not in` | Does not exist |

```python
nums = [1, 2, 3]
print(2 in nums)       # True
print(5 not in nums)  # True
```

## 7️⃣ Bitwise Operators (Low-level, optional for now)

Mostly **not needed** right now (used in systems/CP).

| Operator | Meaning     |    |
| -------- | ----------- | -- |
| `&`      | AND         |    |
| `        | `           | OR |
| `^`      | XOR         |    |
| `<<`     | Left shift  |    |
| `>>`     | Right shift |    |

You can safely skip these for now 👍

## 🧠 Beginner Priority Order (Very Important)

1️⃣ Arithmetic
2️⃣ Assignment
3️⃣ Comparison
4️⃣ Logical
5️⃣ Membership
⏳ Identity & Bitwise → later

## Mini Practice (try this)

```python
a = 8
b = 3

print(a + b)
print(a > b)
print(a % b == 2)
print(a > 5 and b < 5)
```

Perfect topic 👌 — these three operators confuse *everyone* at first, so let’s lock them in properly.

We’ll talk about:

* `/` **Division**
* `//` **Floor Division**
* `%` **Modulus**

I’ll explain **what they mean**, **how they behave**, and **when to use them**.

## 1️⃣ Division `/` → gives the **exact result**

### What it does

* Divides numbers
* **Always returns a float** (decimal), even if division is perfect

```python
print(10 / 2)
print(7 / 2)
```

Output:

```python
5.0
3.5
```

📌 Even `10 / 2` gives `5.0`, not `5`

### When to use

* When you need **precise values**
* Averages, ratios, percentages, data science calculation

## 2️⃣ Floor Division `//` → gives the **quotient only**

### What it does

* Divides and **removes the decimal part**
* Returns the **largest whole number less than or equal to the result**

```python
print(10 // 2)
print(7 // 2)
```

Output:

```python
5
3
```

👉 It **does NOT round**, it **cuts off**.

### ⚠️ Important with negative numbers

```python
print(-7 // 2)
```

Output:

```python
-4
```

Why?
Because floor means **go down to the nearest integer**, not toward zero

## 3️⃣ Modulus `%` → gives the **remainder**

### What it does

* Returns what’s **left over** after division

```python
print(10 % 2)
print(7 % 2)
```

Output:

```python
0
1
```

Think:

```python
7 ÷ 2 = 3 remainder 1
```

So:

```python
7 % 2 = 1
```

## 🔗 How all three are connected

For any two numbers `a` and `b`:

```python
a = (a // b) * b + (a % b)
```

Example:

```python
a = 7
b = 2

print(a // b)  # 3
print(a % b)   # 1
```

```python
7 = 3 * 2 + 1
```

Always true ✅

## 🧠 Real-life intuition

### 🍕 Pizza example

You have **7 slices**, **2 people**.

* `/` → `7 / 2 = 3.5` slices each
* `//` → `7 // 2 = 3` full slices each
* `%` → `7 % 2 = 1` slice left ove

## 🧪 Common beginner use cases

### 🔹 Check even or odd

```python
num = 10
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### 🔹 Pagination (pages of results)

```python
total_items = 23
items_per_page = 5

pages = total_items // items_per_page
extra = total_items % items_per_page
```

### 🔹 Time conversion

```python
seconds = 367
minutes = seconds // 60
remaining_seconds = seconds % 60
```

## 📌 Quick Comparison Table

| Operator | Name           | Returns   | Example  | Result |
| -------- | -------------- | --------- | -------- | ------ |
| `/`      | Division       | Float     | `7 / 2`  | `3.5`  |
| `//`     | Floor division | Integer   | `7 // 2` | `3`    |
| `%`      | Modulus        | Remainder | `7 % 2`  | `1`    |

## ⚠️ Common beginner mistake

```python
a = input("Enter number: ")
print(a % 2)   # ❌ ERROR
```

Why?
`input()` gives **string**, not number.

✅ Fix:

```python
a = int(input("Enter number: "))
print(a % 2)
```
