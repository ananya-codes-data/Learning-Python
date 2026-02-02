# Python Learning Checklist

## 🧱 1. Python Fundamentals & Execution Model

* [ ] What is Python and where is it commonly used?
* [ ] Why is Python called an interpreted language?
* [ ] How does Python execution work (source → bytecode → interpreter)?
* [ ] How do you write and run a Python program?
* [ ] What is indentation and why is it mandatory?
* [ ] What are keywords and identifiers?
* [ ] What are comments and why are they important?
* [ ] What is `__name__` and how does `__main__` work?
* [ ] Difference between script execution and module import

## 🧠 2. Variables, Typing & Memory Model

* [ ] What are variables in Python?
* [ ] How does dynamic typing work?
* [ ] How does variable assignment actually work?
* [ ] Everything in Python is an object — what does this mean?
* [ ] What does `id()` represent?
* [ ] Why can `id()` change or remain the same?
* [ ] What is Python’s memory model?
* [ ] What is reference counting?
* [ ] How does garbage collection work?

## 📦 3. Built-in Data Types (Core + Internals)

### Numbers & Booleans

* [ ] `int`, `float`, `complex` — when to use which?
* [ ] Boolean values and logical operators

### Strings

* [ ] How are strings stored in memory?
* [ ] Why are strings immutable?
* [ ] How does string slicing work?
* [ ] Basics of regex — when should you use it?
* [ ] Indexing and slicing
* [ ] Common string methods and use cases
* [ ] `%` vs `.format()` vs f-strings

### Collections

* [ ] What are Lists? How are they implemented internally?
* [ ] Lists vs arrays — what’s the difference?
* [ ] Why are lists mutable?
* [ ] What are Tuples and why are they immutable?
* [ ] When should you use Tuple over List?
* [ ] What are Sets? How are they different from Lists and Tuples? and their real use cases?
* [ ] What are Dictionaries?
* [ ] How dictionaries are implemented internally
* [ ] Why dictionary keys must be immutable?
* [ ] List vs Tuple vs Set vs Dictionary
* [ ] How do you iterate efficiently over different data types?

## 🔁 4. Control Flow & Iteration

* [ ] How do `if / elif / else` work internally?
* [ ] What are `for` and `while` loops?
* [ ] How does `range()` work?
* [ ] Loop `else` — when does it execute?
* [ ] Difference between `break`, `continue`, and `pass`
* [ ] What does it mean for an object to be iterable?
* [ ] How does iteration work internally?
* [ ] What happens when you loop over a dictionary?
* [ ] How does `enumerate()` work?
* [ ] How does `zip()` work?

## ⚡ 5. Comprehensions & Pythonic Patterns

* [ ] What are list comprehensions?
* [ ] Why are comprehensions faster than loops?
* [ ] What are Dictionary comprehensions?
* [ ] What are Set comprehensions?
* [ ] What are Generator expressions?
* [ ] When should you NOT use comprehensions?

## 🔧 6. Functions & Functional Programming

* [ ] How do functions work internally?
* [ ] Parameters vs arguments
* [ ] Positional vs keyword arguments
* [ ] Default arguments and their pitfalls
* [ ] Why mutable default arguments are dangerous
* [ ] `*args` and `**kwargs` (internal view)
* [ ] Difference between `print()` and `return()`
* [ ] What are lambda functions?
* [ ] Difference between lambda and normal functions?
* [ ] Lambda functions — use cases and limitations
* [ ] `map()`, `filter()`, `reduce()` — How do they work and when to use them?

## 🚨 7. Error & Exception Handling

* [ ] Difference between error and exception
* [ ] Syntax error vs runtime error
* [ ] Common beginner exceptions
* [ ] How `try / except / else / finally` works
* [ ] How exception propagation works?
* [ ] How Python handles exceptions internally?
* [ ] How to raise custom exceptions?
* [ ] When should you create your own exception class?

## 🏷 8. Special Attributes & Execution Flow

* [ ] What is `__name__` in Python?
* [ ] How does `if __name__ == "__main__"` work?
* [ ] What is `__file__`?
* [ ] What is `__doc__`?
* [ ] Difference between module and script execution?

## 🧩 9. Python Data Model & Dunder Methods

* [ ] What are dunder (magic) methods?
* [ ] `__str__` vs `__repr__`
* [ ] `__eq__`, `__lt__`, `__hash__`, `__gt__` — What are they? why they matter?
* [ ] How Python decides object comparison behavior?
* [ ] How `len()` works internally?
* [ ] How iteration uses `__iter__` and `__next__`?

## 🔄 10. Iterators, Generators & Context Managers

* [ ] What is an iterator?
* [ ] What is a generator?
* [ ] Iterator vs generator
* [ ] Why generators are memory efficient
* [ ] What is a context manager?
* [ ] How `with` works internally
* [ ] What are `__enter__` and `__exit__`?

## 🧠 11. Advanced Python Concepts

* [ ] What is a closure?
* [ ] Why closures are useful
* [ ] Closure vs lambda
* [ ] What is a decorator?
* [ ] How decorators work internally
* [ ] Writing decorators with arguments
* [ ] What is monkey patching?
* [ ] How `functools.lru_cache` works
* [ ] What is `@dataclass` and why use it?
* [ ] How type hints work
* [ ] How `mypy` helps

## ⚙ 12. Concurrency, GIL & Performance

* [ ] What is the Global Interpreter Lock (GIL)?
* [ ] Why the GIL exists
* [ ] How GIL affects multithreading
* [ ] Threading vs multiprocessing
* [ ] When should you use multiprocessing?
* [ ] What is asynchronous programming?
* [ ] How `asyncio` works

## 🧠 13. Object-Oriented Programming (OOP)

### Core Concepts

* [ ] What is OOP and why is it used?
* [ ] Class vs object
* [ ] What is `__init__`?
* [ ] What is `self`?

### Attributes & Methods

* [ ] Instance variables vs class variables
* [ ] Instance vs class vs static methods
* [ ] When to use `@classmethod`
* [ ] When to use `@staticmethod`

### Encapsulation

* [ ] Public vs protected vs private
* [ ] Name mangling
* [ ] Does Python really have private variables?

### Inheritance

* [ ] Single vs multiple inheritance
* [ ] Method overriding
* [ ] How `super()` works
* [ ] Method Resolution Order (MRO)
* [ ] Diamond problem and Python’s solution

### Polymorphism & Abstraction

* [ ] Duck typing
* [ ] Operator overloading
* [ ] Overloading vs overriding
* [ ] Abstract Base Classes
* [ ] `abc` module use cases

### OOP Pitfalls

* [ ] Class variable shared-state bug
* [ ] Mutable default attributes
* [ ] Inheritance vs composition

## 📊 14. Python for Data Analytics & SQL

### NumPy

* [ ] Why NumPy is faster than lists
* [ ] What is an ndarray?
* [ ] Vectorization vs loops
* [ ] Broadcasting rules
* [ ] When NOT to use NumPy

### Pandas

* [ ] Series vs DataFrame
* [ ] Reading CSV / Excel / JSON
* [ ] Handling missing values
* [ ] Removing duplicates
* [ ] String cleaning
* [ ] `groupby` internals
* [ ] `merge` vs `join` vs `concat`
* [ ] Time-series operations

### SQL + Python

* [ ] When to use SQL vs pandas
* [ ] Connecting Python to a database
* [ ] Running SQL queries in Python
* [ ] Loading SQL data into pandas
* [ ] Writing pandas data back to SQL

## 📈 15. Visualization & Statistics

* [ ] Matplotlib vs Seaborn
* [ ] Choosing the right chart
* [ ] Common visualization mistakes
* [ ] Mean vs median vs mode
* [ ] Variance & standard deviation
* [ ] Correlation vs causation
* [ ] Explaining stats to non-technical stakeholders

## 🧪 16. Mini Projects (Must-Do)

* [ ] Clean a messy real-world dataset
* [ ] SQL + pandas analysis project
* [ ] Time-series trend analysis
* [ ] Explain a full pandas solution end-to-end

> **Rule to tick a checkbox ✅**
>
> * You can explain it in your own words
> * You can write code without copy-paste
> * You can answer *why / what-if* follow-ups
