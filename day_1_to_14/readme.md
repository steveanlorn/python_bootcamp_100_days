# Recap Day 1 - 14
Recap of Python bootcamp day 1 to 14.  
Replit code: https://replit.com/@steveanlorn


## How to Define a Function
```python
def function_name(param_1, param_2):
    """This is a docstring"""
    # do something
    
    # return None
    # return

    # return one value
    # return True

    # return multiple value
    # return a, b, c

function_name(a, b)
function_name(param_2 = b, param_1 = a)
```

---

## Scope
```python
a_global_var = 10

def function_name():
    # can be accessed in the function
    a_local_var = 11

    # write something to global varibale
    global a_global_var
    a_global_var = 12

# no block scope in Python
if something:
    age = 3
print(age)
```

---

## Variable
- Variable type (includes function parameter, function return value) is determined by what data type passed in.
example:  
```python
age = 13
age = "13"
```
- And since determined by its value, so far I don't see example to declare a variable without assignment.  
- A devition operator automatically convert variable type to float.

---

## Importing Module
- To use code from different file in same level of directory, need to use import it.  
- Import keyword not needed to be put in the beginning of file. But suggested to be put in the beginning of file based on https://pep8.org

```python
import something

something.data
```

---

## List
- List in Python can contain different types of data. 
- Accessing element of list from last: list[-1]

```python
empty_list = []
a_list = [1, 2, 3, "3", True, [10.3, 10.2]]
```

---

## Dictionaries
- A key value data structure.

```python
an_empty_map = {}
a_map = {
    "name": "Steve",
    "age": 17,
}
a_map["name"]
```

---

## Misc

- Scripring language do not need a main func to run. 
- Identation in python act as the code scope sign.
- Extra identation may produce error.
- Naming convention in Python tends to be snake_case.
- Extracting a character on string by index:
```python
# output: H
"Hello"[0]
```
- Can separate thousand by underscore: `123_456_789`

---

## IF

```python
if statement:
    # code
elif not statement > 1:
    # code
else:
    # code
```

---

## Loop

```python
for fruit in fruits:
    # do something

for n in range(start, stop, step):
    # do something

while something:
    # do something
```

---

## Printing

```python
print(something)
print(f"my age is {age}")
```

----

## Docstring
- Can be used as function comment
```python
"""This is a docstring"""
```
