# Python Learning Checklist

## 🧱 1. Python Fundamentals & Execution Model

* [ ] What is Python and where is it commonly used? and why is it popular in Data Science?
* [ ] Why is Python called an interpreted language?
* [ ] Interpreted vs compiled languages (Python vs C/Java)
* [ ] How does Python execution work (source → bytecode → interpreter)?
* [ ] How do you write and run a Python program?
* [ ] How Python programs are run (REPL, script, notebook)
* [ ] What is indentation and why is it mandatory?
* [ ] Indentation rules and why Python enforces them
* [ ] What are keywords, identifiers and naming conventions?
* [ ] What are comments and why are they important?
* [ ] Comments and docstrings — when and how to use them
* [ ] What is `__name__` and how does `__main__` work?
* [ ] Difference between script execution and module import
* [ ] Writing readable code (PEP 8 basics)

## 🧠 2. Variables, Typing & Memory Model

* [ ] What are variables in Python?
* [ ] Variables as references, not containers
* [ ] Dynamic typing and late binding
* [ ] How does dynamic typing work?
* [ ] How does variable assignment actually work?
* [ ] Everything in Python is an object — what does this mean?
* [ ] `id()`, object identity, and equality
* [ ] Mutable vs immutable objects (mental model)
* [ ] What does `id()` represent?
* [ ] Why can `id()` change or remain the same?
* [ ] What is Python’s memory model?
* [ ] What is reference counting?
* [ ] Garbage collection and circular references
* [ ] How does garbage collection work?
* [ ] Why this matters for large datasets

## 📦 3. Built-in Data Types (Core + Internals)

### Numbers & Booleans

* [ ] `int`, `float`, `complex` — when to use which? — real-world usage
* [ ] Boolean values and logical operators
* [ ] Floating-point precision issues
* [ ] Boolean logic and truthy / falsy values

### Strings (for data cleaning)

* [ ] How are strings stored in memory?
* [ ] Why are strings immutable? Strings as immutable sequences
* [ ] How does string slicing work?
* [ ] Basics of regex — when should you use it?
* [ ] Regex for data extraction
* [ ] Indexing and slicing and step logic
* [ ] Common string methods and use cases, particularly for data extraction
* [ ] `%` vs `.format()` vs f-strings

### Collections

* [ ] What are Lists? How are they implemented internally and what about the performance?
* [ ] Lists vs arrays — what’s the difference? (Python vs NumPy)
* [ ] Why are lists mutable?
* [ ] What are Tuples and why are they immutable?
* [ ] Tuples — immutability and safety
* [ ] When should you use Tuple over List?
* [ ] What are Sets? How are they different from Lists and Tuples? and their real use cases?
* [ ] Sets — uniqueness, hashing, fast lookups
* [ ] What are Dictionaries? Tell me about the key-value mapping.
* [ ] How dictionaries are implemented internally (hash tables)
* [ ] Why dictionary keys must be immutable?
* [ ] List vs Tuple vs Set vs Dictionary
* [ ] How do you iterate efficiently over different data types?
* [ ] Choosing the right data structure for a problem

## 🔁 4. Control Flow & Iteration

* [ ] `if / elif / else` logic and short-circuiting
* [ ] How do `if / elif / else` work internally?
* [ ] What are `for` and `while` loops?
* [ ] How does `range()` works internally?
* [ ] Loop `else` — when does it execute?
* [ ] Difference between `break`, `continue`, and `pass`
* [ ] Iterables vs iterators
* [ ] What does it mean for an object to be iterable?
* [ ] How does iteration work internally?
* [ ] Iterating over lists, dicts, sets, and files
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
* [ ] Readability vs cleverness trade-offs

## 🔧 6. Functions & Functional Programming

* [ ] Function call stack and scope
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
* [ ] `map()`, `filter()`, `reduce()` — How do they work, when to use them and when to avoid?
* [ ] Writing modular, reusable functions
* [ ] Separating data loading, processing, and execution logic
* [ ] Refactoring scripts into reusable modules

## 🚨 7. Error & Exception Handling

* [ ] Difference between error and exception
* [ ] Syntax error vs runtime error
* [ ] Common Python exceptions in data work
* [ ] How `try / except / else / finally` works
* [ ] How exception propagation works?
* [ ] How Python handles exceptions internally?
* [ ] How to raise custom exceptions?
* [ ] Writing your own exception classes
* [ ] When should you create your own exception class?
* [ ] Defensive coding for messy data

## 🏷 8. Modules, Packages & Execution Context

* [ ] What is `__name__`?
* [ ] How `if __name__ == "__main__"` works
* [ ] `__file__` and module locations
* [ ] `__doc__` and documentation
* [ ] Import styles and best practices
* [ ] What is a virtual environment?
* [ ] `venv` vs `conda` (conceptual differences)
* [ ] `requirements.txt` vs `environment.yml`
* [ ] Why reproducibility matters in data science

## 🧩 9. Python Data Model & Dunder Methods

* [ ] What are dunder (magic) methods?
* [ ] `__str__` vs `__repr__`
* [ ] `__eq__`, `__lt__`, `__hash__`, `__gt__` — What are they? why they matter?
* [ ] How Python decides object comparison behavior?
* [ ] Hashing and dictionary behavior
* [ ] How `len()` works internally?
* [ ] How iteration uses `__iter__` and `__next__`?
* [ ] Why pandas objects rely heavily on dunder methods

## 🔄 10. Iterators, Generators & Context Managers

* [ ] What is an iterator? (Iterator protocol)
* [ ] What is a generator? (Generators and `yield`)
* [ ] Iterator vs generator
* [ ] Why generators are memory efficient?
* [ ] What is a context manager?
* [ ] How `with` works internally
* [ ] What are `__enter__` and `__exit__`?
* [ ] Reading large files safely

## 🧠 11. Advanced Python Concepts

* [ ] What is a closure?
* [ ] Why closures are useful?
* [ ] Closures and lexical scoping
* [ ] Closure vs lambda
* [ ] What is a decorator?
* [ ] How decorators work internally?
* [ ] Writing decorators with arguments
* [ ] What is monkey patching?
* [ ] How `functools.lru_cache` works
* [ ] What is `@dataclass` and why use it?
* [ ] How type hints work
* [ ] Type hints and static typing
* [ ] How `mypy` helps

## ⚙ 12. Concurrency, GIL & Performance

* [ ] What is the Global Interpreter Lock (GIL)?
* [ ] Why the GIL exists
* [ ] How GIL affects multithreading
* [ ] CPU-bound vs I/O-bound tasks
* [ ] Threading vs multiprocessing
* [ ] When should you use multiprocessing?
* [ ] What is asynchronous programming?
* [ ] How `asyncio` works

## 🧠 13. Object-Oriented Programming (OOP)

### Core Concepts

* [ ] What is OOP and why is it used?
* [ ] Class vs object
* [ ] What is `__init__`?
* [ ] `__init__` and object lifecycle
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
* [ ] Designing data-centric classes

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
* [ ] Memory layout (views vs copies)
* [ ] When NOT to use NumPy

### Pandas

* [ ] Series vs DataFrame
* [ ] Reading CSV / Excel / JSON
* [ ] Handling missing values
* [ ] Removing duplicates
* [ ] Data type conversions
* [ ] String operations
* [ ] `groupby` internals
* [ ] `merge` vs `join` vs `concat`
* [ ] Time-series operations

### SciPy (Conceptual)

* [ ] What SciPy is used for
* [ ] SciPy vs NumPy — responsibilities
* [ ] `scipy.stats` basics (distributions, tests)
* [ ] Optimization & linear algebra (high-level awareness)
* [ ] When SciPy is preferred over pure NumPy

### SQL + Python

* [ ] When to use SQL vs pandas
* [ ] Connecting Python to a database
* [ ] Running SQL queries in Python
* [ ] Loading SQL data into pandas
* [ ] Writing pandas data back to SQL

## 📈 15. Visualization & Statistics

* [ ] Matplotlib vs Seaborn
* [ ] Choosing the right chart
* [ ] Avoiding misleading visualizations
* [ ] Mean vs median vs mode
* [ ] Variance & standard deviation
* [ ] Correlation vs causation
* [ ] Explaining stats to non-technical stakeholders

## 🧪 16. Mini Projects (Must-Do)

* [ ] Clean a messy real-world dataset
* [ ] SQL + pandas analysis project
* [ ] Exploratory data analysis (EDA)
* [ ] Time-series trend analysis
* [ ] Explain a full pandas solution end-to-end
* [ ] Validate assumptions and data quality
* [ ] Add basic assertions or checks to your analysis

## 📓 17. Jupyter Notebooks & Data Science Workflow

* [ ] Jupyter notebooks vs Python scripts
* [ ] Notebook best practices (cells, naming, ordering)
* [ ] Avoiding hidden state and execution order bugs
* [ ] When NOT to use notebooks
* [ ] Converting notebooks to scripts

## 📦 18. Working with Large & Real-World Data

* [ ] Reading large CSVs efficiently
* [ ] Chunking data with pandas
* [ ] Memory-aware data loading
* [ ] File formats: CSV vs Parquet (conceptual)
* [ ] Trade-offs between storage, speed, and memory

## 🧪 19. Reliability, Testing & Trusting Your Results

* [ ] Using assertions in data pipelines
* [ ] Writing simple tests for data functions
* [ ] Detecting silent data issues
* [ ] Building confidence in analytical results

> **Rule to tick a checkbox ✅**
>
> * You can explain it in your own words
> * You can write code without copy-paste
> * You can answer *why / what-if* follow-ups
