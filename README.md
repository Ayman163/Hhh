# Student Habit Tracker 📋

A simple C++ console application that helps students track their daily habits.

---

## 📌 Project Description

This program allows students to manage their habits by adding new habits,
updating progress, searching for a specific habit, and viewing all habits
with their completion percentage.

---

## ✨ Features

- Add a new habit with a name and target days
- Update completed days for any habit
- View all habits with progress percentage
- Search for a habit by ID
- Input validation (duplicate ID, full list, empty list)
- Progress cap so completed days never exceed target days

---

## 🧠 Concepts Used

| Concept | Where I Used It |
|---|---|
| `struct` | To store each habit (id, name, tardays, comdays) |
| Arrays | `ha h[100]` to store up to 100 habits |
| Functions | `addHabit()`, `updateHabit()`, `showHabits()`, `searchHabit()` |
| `while(true)` loop | To keep the menu running |
| `switch` statement | To handle menu choices |
| `for` loop | To search and display habits |
| `if / else` | For input validation |
| `cin.ignore()` + `getline()` | To read names that have spaces |

---

## 🔄 Development History

### v0.1 — First Try
The first version I wrote. The menu and switch were inside a `for` loop
which was wrong because the loop needs `count > 0` to run, so the menu
never showed. I also put an array inside the struct by mistake `int ha[100]`
which is not needed. The update and show functions were empty.

### v0.3 — Adding Functions
I learned about functions so I moved the code into separate functions:
`addHabit()`, `updateHabit()`, `showHabits()`, `searchHabit()`.
I also changed the `for` loop to `while(true)` so the menu always shows.
But I had a bug: I wrote `int count = 0` twice which causes a compile error.
The `showHabits()` function also used `i` without a loop.

### v0.5 — Functions Working
I fixed the double `count` variable bug and fixed `showHabits()`
by adding a proper `for` loop. Also removed the wrong array from inside
the struct. Now all 4 functions work correctly.

### v0.7 — Better Variable Name
I renamed `count` to `habitCount` to make the code clearer
and more descriptive. Also, using `count` with `using namespace std`
can cause a conflict with `std::count` from the standard library.

### v0.8 — Fixing Name Input
I noticed that if the habit name has spaces like "Read Book",
`cin >>` only reads the first word. I fixed this by using:
```cpp
cin.ignore();
getline(cin, h[habitCount].name);
```
`cin.ignore()` clears the leftover newline `\n` from the buffer
that `cin >>` leaves behind. Without it, `getline` would read an
empty line and skip the name input.
I also added `#include <string>` to be more explicit.

### v1.0 — Final Version
Added several improvements:
- **Full list check:** `if (habitCount >= 100)` to prevent writing
  outside the array bounds
- **Duplicate ID check:** a `for` loop before adding to make sure the
  same ID is not used twice
- **Cap completed days:** `if (h[i].comdays > h[i].tardays)` so
  completed days never exceed the target
- **Empty list check:** `if (habitCount == 0)` in `showHabits` so it
  shows a message instead of printing nothing
- **Progress percentage:** `percent = comdays * 100 / tardays`
  to show how far the student is from their goal
- **Better formatting:** added `---` lines to make the output cleaner

---

## 🛠️ How to Run

1. Open the project in any C++ compiler
   (Code::Blocks, Visual Studio, Dev-C++)
2. Compile `main.cpp`
3. Run the program
4. Use the menu to interact with the tracker

---

## 📷 Sample Output

<img width="300" height="477" alt="sample output" src="https://github.com/user-attachments/assets/52157267-44ad-45e1-a298-1b3ab58907a8" />

---

## 👨‍💻 Author

- **Name:** Ayman
- **Course:** Structural Programming with C++
- **University:** University of Fallujah
- **Year:** 2025–2026
