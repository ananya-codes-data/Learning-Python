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
