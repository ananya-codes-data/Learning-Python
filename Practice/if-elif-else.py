# ============================================================
# PYTHON IF - ELIF - ELSE PRACTICE
# ============================================================
# Topics:
# - if / elif / else
# - Nested if
# - Logical operators (and / or / not)
# - Comparison operators
# - Input validation
# - Decision trees
# - Multiple conditions
# - Condition ordering
# - Edge cases
#
# IMPORTANT:
# Try to write the decision tree / pseudocode BEFORE coding.
# Do NOT look for solutions immediately.
# ============================================================


# ============================================================
# LEVEL 1 — LOGIC BUILDING
# ============================================================


# ------------------------------------------------------------
# QUESTION 1 — Voting Eligibility (Enhanced)
# ------------------------------------------------------------
"""
Take input for:
    - Citizenship: yes/no
    - Age
    - Voter ID: yes/no

Rules:
    1. Non-citizens cannot vote.
    2. Citizens below 18 cannot vote because they are underage.
    3. Citizens 18+ without voter ID cannot vote.
    4. Citizens 18+ with voter ID can vote.

IMPORTANT:
    Do not ask for voter ID if the person is not a citizen
    or is under 18.
"""
'''
citizenship_check = input("are you a citizen? (yes/no): ")

if citizenship_check.lower() == "yes":
    age_check = int(input("whats your age?: "))

    if age_check >= 18:
        voterid_check = input("do you have a voter id? (yes/no): ")

        if voterid_check.lower() == "yes":
            print("you can vote")
        else:
            print("you cannot vote")
    else:
        print(f"you cannot vote, you can after {18 - age_check} years")
else:
    print("you cannot vote because you are not a citizen")
'''
# ------------------------------------------------------------
# QUESTION 2 — Student Grade + Scholarship
# ------------------------------------------------------------
"""
Take:
    - Marks in 3 subjects
    - Attendance percentage

Calculate the average marks.

Grade:
    90+       -> A
    80–89     -> B
    70–79     -> C
    60–69     -> D
    Below 60  -> F

Scholarship:
    Average >= 90 AND attendance >= 90
        -> Full Scholarship

    Average >= 80 AND attendance >= 85
        -> Partial Scholarship

    Otherwise
        -> No Scholarship

Additional rule:
    If the student fails ANY subject, they cannot receive
    a scholarship regardless of their average.

Think about:
    - Nested if
    - and
    - multiple conditions
"""

maths = int(input("put your maths marks: "))
science = int(input("put your science marks: "))
english = int(input("put your english marks: "))

if (maths or science or english) > 0.6 * 100:
    avg_check = (maths + science + english) / 3
    attendance_check = int(input("whats your attendance percentage: "))

    if avg_check >= 90 and attendance_check >= 90:
        print("Full Scholarship")
    if avg_check >= 80 and attendance_check >= 85:
        print("Partial Scholarship")
    else:
        print("No Scholarship")
else:
    print("No Scholarship because you failed in any subject")

# ------------------------------------------------------------
# QUESTION 3 — Electricity Bill
# ------------------------------------------------------------
"""
Take electricity units consumed.

Pricing:
    0–100 units       -> ₹5/unit
    101–200 units     -> ₹7/unit
    201–500 units     -> ₹10/unit
    Above 500 units   -> ₹15/unit

Additional rules:
    Bill > ₹5,000
        -> 10% surcharge

    Bill > ₹10,000
        -> 15% surcharge

    Senior citizen
        -> 5% discount AFTER surcharge

Take:
    - Units consumed
    - Senior citizen: yes/no

Print:
    - Units
    - Base bill
    - Surcharge
    - Discount
    - Final bill

Think carefully about the ORDER of calculations.
"""


# ------------------------------------------------------------
# QUESTION 4 — ATM Withdrawal
# ------------------------------------------------------------
"""
Take:
    - Account balance
    - Withdrawal amount
    - PIN correctness

Rules:
    1. Incorrect PIN -> Transaction rejected.
    2. Correct PIN -> Continue checking.
    3. Withdrawal must:
         - Be greater than 0
         - Be a multiple of ₹100
         - Be <= balance
    4. Minimum balance after withdrawal must be ₹500.

Print the specific reason if the transaction is rejected.

Think about:
    - Nested if
    - Validation order
    - Multiple conditions
"""


# ============================================================
# LEVEL 2 — NESTED IF
# ============================================================


# ------------------------------------------------------------
# QUESTION 5 — Job Eligibility System
# ------------------------------------------------------------
"""
Take:
    - Age
    - Degree: yes/no
    - Years of experience
    - Programming skill: yes/no

Basic eligibility:
    Age must be between 21 and 35.
    Candidate must have a degree.

If basic eligibility is satisfied:

    Experience >= 3 AND programming skill
        -> Senior Developer

    Experience >= 1 AND programming skill
        -> Developer

    Experience < 1 AND programming skill
        -> Junior Developer

    No programming skill
        -> Technical Training Required

If age is outside the range:
    -> Not eligible because of age.

If no degree:
    -> Not eligible because degree is required.

IMPORTANT:
    Do not ask for experience/programming skill if the candidate
    already fails the basic eligibility requirements.
"""


# ------------------------------------------------------------
# QUESTION 6 — Bank Loan Approval
# ------------------------------------------------------------
"""
Take:
    - Age
    - Monthly income
    - Credit score
    - Existing loan: yes/no

Basic eligibility:
    Age >= 21
    Income >= ₹25,000

If eligible:

    Credit score >= 750:
        Existing loan:
            Income >= ₹75,000 -> Approve
            Otherwise         -> Reject

        No existing loan:
            -> Approve

    Credit score 650–749:
        Income >= ₹50,000 -> Approve
        Otherwise         -> Reject

    Credit score < 650:
        -> Reject

Print the reason for rejection wherever possible.

Think about:
    - Nested if
    - Range checking
    - Multiple levels of decisions
"""


# ------------------------------------------------------------
# QUESTION 7 — Movie Ticket Pricing
# ------------------------------------------------------------
"""
Take:
    - Age
    - Day of week
    - Movie type: regular/premium
    - Membership: yes/no

Base price:
    Regular -> ₹200
    Premium -> ₹350

Discounts:
    Child (<13)        -> 40%
    Senior citizen     -> 30%
    Wednesday          -> Additional 20%
    Member             -> Additional 10%

Maximum total discount = 50%.

Calculate:
    - Base price
    - Total discount percentage
    - Discount amount
    - Final ticket price

Think about:
    - Multiple independent conditions
    - Accumulating discounts
    - Maximum limit
"""


# ============================================================
# LEVEL 3 — LOGICAL OPERATORS + EDGE CASES
# ============================================================


# ------------------------------------------------------------
# QUESTION 8 — Triangle Classifier
# ------------------------------------------------------------
"""
Take three side lengths.

First determine whether the triangle is valid.

A triangle is valid only if:

    a + b > c
    a + c > b
    b + c > a

If valid, classify it:

    All three equal
        -> Equilateral

    Exactly two equal
        -> Isosceles

    All different
        -> Scalene

Then determine whether it is:

    Right-angled
    Acute
    Obtuse

IMPORTANT:
    Do not classify an invalid triangle.

Hint:
    You may need to sort the sides before checking
    whether it is right/acute/obtuse.
"""


# ------------------------------------------------------------
# QUESTION 9 — Password Strength Checker
# ------------------------------------------------------------
"""
Take a password.

Check whether it contains:

    1. At least 8 characters
    2. Uppercase letter
    3. Lowercase letter
    4. Digit
    5. Special character

Classification:

    5 conditions -> Very Strong
    4 conditions -> Strong
    3 conditions -> Medium
    2 conditions -> Weak
    <2           -> Very Weak

SPECIAL RULE:

    If the password contains the word "password"
    anywhere, classify it as:

        -> Unsafe

    This rule applies regardless of the strength score.

Think about:
    - String methods
    - Boolean variables
    - Multiple conditions
    - Condition priority
"""


# ------------------------------------------------------------
# QUESTION 10 — Date Validator
# ------------------------------------------------------------
"""
Take:

    - Day
    - Month
    - Year

Determine whether the date is valid.

Month lengths:

    January   -> 31
    February  -> 28 or 29
    March     -> 31
    April     -> 30
    May       -> 31
    June      -> 30
    July      -> 31
    August    -> 31
    September -> 30
    October   -> 31
    November  -> 30
    December  -> 31

Leap year:

    A year is a leap year if:

        divisible by 400

        OR

        divisible by 4 AND NOT divisible by 100

Examples:

    29/02/2024 -> Valid
    29/02/2023 -> Invalid
    31/04/2025 -> Invalid
    31/12/2025 -> Valid

Think about:
    - Nested if
    - and / or / not
    - Edge cases
"""


# ============================================================
# LEVEL 4 — HARD DECISION PROBLEMS
# ============================================================


# ------------------------------------------------------------
# QUESTION 11 — E-Commerce Discount Engine
# ------------------------------------------------------------
"""
Take:

    - Purchase amount
    - Customer type: regular/premium
    - Coupon: yes/no
    - First order: yes/no

Base discount:

    < ₹1,000       -> 0%
    ₹1,000–4,999   -> 5%
    ₹5,000–9,999   -> 10%
    ₹10,000+       -> 15%

Additional discounts:

    Premium customer -> +5%
    First order     -> +10%
    Coupon          -> +15%

Rules:

    1. Maximum total discount = 30%.
    2. Coupon CANNOT be combined with first-order discount.
    3. Premium discount can always be applied.

Print:

    Original price
    Base discount
    Additional discounts
    Final discount %
    Discount amount
    Final price

Think carefully about interacting conditions.
"""


# ------------------------------------------------------------
# QUESTION 12 — Employee Performance Evaluation
# ------------------------------------------------------------
"""
Take:

    - Performance score (0–100)
    - Attendance %
    - Projects completed
    - Years of experience

Performance:

    90–100 -> Exceptional
    75–89  -> Excellent
    60–74  -> Good
    40–59  -> Average
    <40    -> Poor

Promotion rules:

    Exceptional + attendance >= 90
        -> Immediate Promotion

    Excellent + attendance >= 95 + projects >= 3
        -> Promotion Review

    Good + experience >= 5 + projects >= 5
        -> Promotion Review

    Otherwise
        -> Not Eligible

Additional rule:

    If score < 40:

        Attendance < 75
            -> Performance + Attendance Warning

        Otherwise
            -> Performance Warning

IMPORTANT:
    Performance classification and promotion eligibility
    are separate decision systems.
"""


# ------------------------------------------------------------
# QUESTION 13 — Hospital Emergency Triage
# ------------------------------------------------------------
"""
Take:

    - Age
    - Temperature
    - Heart rate
    - Blood pressure
    - Consciousness: yes/no
    - Chest pain: yes/no

Determine priority.

CRITICAL if:

    Patient is unconscious

    OR

    Chest pain AND abnormal heart rate

    OR

    Very abnormal blood pressure

HIGH PRIORITY if:

    Age > 65 AND temperature > 39

    OR

    Heart rate significantly abnormal

MEDIUM PRIORITY if:

    Temperature > 38

    OR

    Moderate blood pressure abnormality

Otherwise:

    LOW PRIORITY

IMPORTANT:

    Critical conditions must override lower-priority conditions.

Example:
    If patient is unconscious, immediately classify as Critical.
"""


# ------------------------------------------------------------
# QUESTION 14 — Driving License Eligibility
# ------------------------------------------------------------
"""
Take:

    - Age
    - Citizenship: yes/no
    - Learner's license: yes/no
    - Driving test passed: yes/no
    - Medical clearance: yes/no

Rules:

    Non-citizen
        -> Not eligible

    Citizen:

        Age < 18
            -> Not eligible

        Age 18–20
            -> Two-wheeler license only

        Age >= 21
            -> Can apply for all categories

Before issuing the license:

    Learner's license is required.
    Medical clearance is required.
    Driving test must be passed.

If any requirement fails:
    Print the SPECIFIC reason.

Think about:
    - Nested if
    - Multiple eligibility pathways
"""


# ------------------------------------------------------------
# QUESTION 15 — University Admission System
# ------------------------------------------------------------
"""
Take:

    - Entrance exam score
    - Board percentage
    - Interview score
    - Sports quota: yes/no
    - Income category: general/ews
    - Subject eligibility: yes/no

FIRST:

    Subject eligibility must be YES.

If not:
    -> Rejected immediately.

GENERAL CATEGORY:

    Entrance >= 85
    AND Board >= 75
    AND Interview >= 70

    -> Selected

EWS:

    Entrance >= 75
    AND Board >= 70
    AND Interview >= 60

    -> Selected

SPORTS QUOTA:

    If sports quota == yes:

        Entrance >= 60
        AND Board >= 60
        AND Interview >= 50

        -> Selected

Sports quota cannot bypass subject eligibility.

Think about:
    - Multiple pathways
    - Nested conditions
    - Priority of conditions
"""


# ============================================================
# LEVEL 5 — VERY HARD
# ============================================================


# ------------------------------------------------------------
# QUESTION 16 — Smart ATM
# ------------------------------------------------------------
"""
Build a complete ATM decision system.

Take:

    - PIN
    - Account balance
    - Withdrawal amount
    - Account type
    - Number of previous failed PIN attempts

Rules:

    1. Lock account after 3 incorrect PIN attempts.

    2. Savings account:
           Minimum balance = ₹500

    3. Current account:
           Minimum balance = ₹2,000

    4. Withdrawal must be a multiple of ₹100.

    5. Maximum withdrawal depends on account type.

    6. Balance must be sufficient.

    7. Withdrawal cannot violate minimum balance.

    8. Withdrawal cannot exceed daily withdrawal limit.

If successful:
    Display:
        - Amount withdrawn
        - Remaining balance
        - Transaction successful

If rejected:
    Display the specific reason.

IMPORTANT:
    Do NOT write one giant if condition.

Design a logical sequence of checks.
"""


# ------------------------------------------------------------
# QUESTION 17 — Restaurant Order System
# ------------------------------------------------------------
"""
Take:

    - Customer type
    - Food category
    - Order amount
    - Delivery distance
    - Coupon: yes/no

Determine:

    1. Whether delivery is available.
    2. Delivery charge.
    3. Discount.
    4. Final amount.
    5. Whether delivery is free.

Rules:

    Premium + order >= ₹500
        -> Free delivery

    Regular + order >= ₹1,000
        -> Free delivery

    Distance > 10 km
        -> Delivery unavailable

    Coupon + Premium
        -> Different discount

Add your own reasonable rules for:
    - Delivery charges
    - Minimum order
    - Coupon discount

Think about:
    - Nested conditions
    - Multiple interacting conditions
"""


# ------------------------------------------------------------
# QUESTION 18 — Train Ticket Fare Calculator
# ------------------------------------------------------------
"""
Take:

    - Age
    - Class
    - Distance
    - Tatkal: yes/no
    - Senior citizen: yes/no

Calculate fare based on:

    1. Distance slab
    2. Class
    3. Age
    4. Senior citizen discount
    5. Tatkal surcharge

Special rules:

    - Children have different pricing.
    - Senior discount applies only to eligible ages.
    - Tatkal surcharge is applied AFTER discounts.
    - Certain classes do not allow specific discounts.

Print:

    Base fare
    Age adjustment
    Senior discount
    Tatkal surcharge
    Final fare

IMPORTANT:
    Pay attention to the order of calculations.
"""


# ============================================================
# LEVEL 6 — CHALLENGE PROBLEMS
# ============================================================


# ------------------------------------------------------------
# QUESTION 19 — Insurance Premium Calculator
# ------------------------------------------------------------
"""
Take:

    - Age
    - Gender
    - Smoking status
    - Annual income
    - Existing disease: yes/no
    - Policy amount

Determine:

    - Base premium
    - Risk category
    - Risk surcharge
    - Discount
    - Final premium

Design your own reasonable rules.

Suggested decision structure:

    Age group
        |
        v
    Smoking?
        |
        v
    Existing disease?
        |
        v
    Income category
        |
        v
    Calculate final premium

Try to use nested if statements instead of putting
everything into one condition.
"""


# ------------------------------------------------------------
# QUESTION 20 — FizzBuzz++
# ------------------------------------------------------------
"""
Take a number n.

For every number from 1 to n:

    Divisible by 3 -> Fizz
    Divisible by 5 -> Buzz
    Divisible by both -> FizzBuzz

Now extend it:

    Divisible by 7 -> Bang

Therefore:

    3 and 7
        -> FizzBang

    5 and 7
        -> BuzzBang

    3, 5 and 7
        -> FizzBuzzBang

Otherwise:
        -> Print the number

IMPORTANT:
    Condition ordering matters.

Think about:
    Why should some conditions be checked before others?
"""


# ------------------------------------------------------------
# QUESTION 21 — Rock Paper Scissors
# ------------------------------------------------------------
"""
Take:

    - Player 1 choice
    - Player 2 choice

Choices:

    rock
    paper
    scissors

Determine:

    - Winner
    - Draw

Also handle:

    - Invalid input
    - Uppercase/lowercase differences

Examples:

    rock
    Rock
    ROCK

should all represent the same choice.

BONUS:
    Extend the game to Rock-Paper-Scissors-Lizard-Spock.
"""


# ------------------------------------------------------------
# QUESTION 22 — Login System
# ------------------------------------------------------------
"""
Build a login system.

Take:

    - Username
    - Password
    - OTP

Decision flow:

    Wrong username
        -> Reject immediately

    Correct username
        -> Check password

    Wrong password
        -> Reject

    Correct password
        -> Check OTP

    Wrong OTP
        -> Reject

    Correct OTP
        -> Login successful

Additional rule:

    After 3 failed login attempts:
        -> Account locked

Think about:

    - Nested if
    - Attempt counter
    - Multiple validation stages
    - State
    - Condition ordering
"""

# ============================================================
# BONUS CHALLENGE — Build Your Own
# ============================================================

# Create your own real-world decision system.

# Choose ONE:

#     1. Food delivery app
#     2. College admission
#     3. Banking system
#     4. Online shopping
#     5. Movie booking
#     6. Cab booking
#     7. Hotel booking
#     8. Job recruitment
#     9. Insurance
#     10. Airport security

# Requirements:

#     - At least 8 inputs
#     - At least 3 levels of nested decisions
#     - At least 5 different outcomes
#     - Use AND / OR / NOT
#     - Handle invalid input
#     - Handle edge cases
#     - Print specific reasons for rejection
#     - Do NOT use a giant single if condition

# BONUS:
#     Draw the decision tree before writing the Python code.

# ============================================================
# IMPORTANT PRACTICE RULES
# ============================================================


# For EVERY problem:

# 1. Understand the requirements.

# 2. Identify the inputs.

# 3. Identify all possible outputs.

# 4. Write the conditions in plain English.

# 5. Draw a decision tree if the problem is complicated.

# 6. Write pseudocode.

# 7. Only THEN write Python code.

# 8. Test normal cases.

# 9. Test boundary cases.

# 10. Test invalid inputs.

# 11. Try to break your own program.

# 12. Refactor your code if the conditions become messy.


# Example of boundary testing:

# If age >= 18:

#     Test 17
#     Test 18
#     Test 19


# For:

#     score >= 90

# Test:

#     89
#     90
#     91


# The goal isn't just to make the program work.

# The goal is to understand WHY your conditions

# are written in that particular order.