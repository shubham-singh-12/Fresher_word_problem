**Fresh Word Problem**
This Python script `fresh_word_problem.py` is designed to find the longest and second-longest compound words within a given list of words.

**Libraries Used**
**1.Trie (T)**
* `Trie` is a data structure used for efficiently storing and searching for strings.
* It's implemented in the Trie.py file.
* The Trie data structure is used for storing words and efficiently finding prefixes of words.

**2. collections.deque**
* `deque` is a double-ended queue implementation provided by the Python `collections` module.
* It's used for efficiently managing a queue of compound word candidates in the `CompoundWordFinder` class.
* The `deque` allows for fast insertion and removal of elements from both ends of the queue.

**3. time**
* `time` is a Python module that provides various time-related functions.
* It's used for measuring the execution time of the script.


**Classes and Functions**

**1. CompoundWordFinder Class**
* `CompoundWordFinder` is a class designed for finding the longest and second-longest compound words within a list of words.
* It contains the following methods:

**a. __init__()**
 Constructor method that initializes a `CompoundWordFinder` object with a Trie and a deque.

**b. buildTrie(filePath: str = None****)**
 Method for building a Trie from words in a file.
**Parameters**:
**filePath (str)**: Path to the file containing words. Defaults to None.
This method reads words from the specified file, inserts them into the Trie, and divides them into word-suffix pairs to add to the deque.

**c. findLongestCompoundWords()**
* Method for finding the longest and second-longest compound words.
* Returns:
* tuple: A tuple containing the longest and second-longest compound words found.
* This method iterates through the deque of word-suffix pairs, checking if the suffixes are valid words in the Trie. It updates the longest and second-longest compound words accordingly.

**5. Execution**
* The main execution block of the script creates an instance of CompoundWordFinder, builds a Trie from words in the input file, finds the longest and second-longest compound words, and prints the results along with the execution time.

**5. Usage**
To use the script, follow these steps:

* Ensure you have Python installed on your system.
* Place the input file containing words (e.g., `Input_01.txt`) in the same directory as the script.
* Run the script using the command `python Fresh_word_Problem.py`.
* The script will output the longest and second-longest compound words found, along with the execution time.