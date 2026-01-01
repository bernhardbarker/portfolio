A small selection of algorithm problems I've solved, alongside unit tests.

### Notebooks

| File | Description |
| --- | --- |
| **[K-Means Clustering](K-Means%20Clustering.ipynb)** | Calculate and visualise manual k-means clustering 
| **[Probability of Table Tennis Win](Probability%20of%20Table%20Tennis%20Win.ipynb)** | Calculate the probability of winning in table tennis using the binomial distribution and recursive probabilities 

### Python files

| File | Problem | Solution |
| --- | --- | --- |
| **[Combination Sum (Medium)](combination_sum.py)** | Find all combinations that sum to a given target; numbers may be chosen multiple times | Iteratively generate combinations summing up to every value from 0 to target
| **[Combination Sum II (Medium)](combination_sum_ii.py)** | Find all combinations that sum to a given target; numbers may only be chosen once | Iteratively generate combinations summing up to every value from 0 to target, with duplicate checking
| **[Count and Say (Medium)](count_and_say.py)** | Find the nth step of Run-Length Encoding (RLE) the same string repeatedly, i.e. replacing consecutive identical characters with the character and the count of the characters | Iteratively generate these strings
| **[First Missing Positive (Hard)](first_missing_positive.py)** | Find the smallest positive integer not present in an unsorted integer array, in O(n) time and O(1) space | Move each element to its "correct" position, then find the first element not in its correct position
| **[Longest Valid Parentheses (Hard)](longest_valid_parentheses.py)** | Find the longest valid parentheses substring | Use a stack to store the starts of each longest valid substring
| **[Search in Rotated Sorted Array (Medium)](search_in_rotated_sorted_array.py)** | Implement binary search for a rotated array (shifted with wrap-around) | First run binary search to find the start of the rotated array, then run another binary search to find the target in either the left or right side of that
| **[Substring with Concatenation of All Words (Hard)](substring_with_concatenation_of_all_words.py)** | Find all concatenated substrings of a given list of fixed-length words within a string | Starting from each index mod word length, go through the string, adding and removing words to find concatenated substrings
| **[Sudoku Solver (Hard)](sudoku_solver.py)** | Solve Sudoku puzzles | Iteratively remove invalid possibilities and then run backtracking by trying each possibility
| **[Trapping Rain Water (Hard)](trapping_rain_water.py)** | Determine how much water can be trapped given an elevation map | For each element, find the tallest height to the left and right and take the minimum of that
| **[Valid Sudoku (Medium)](valid_sudoku.py)**| Determine if a Sudoku grid is valid | Run over each row, column and square, and use a bitmask to check if there are duplicate values
