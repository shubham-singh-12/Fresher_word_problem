# Importing a Trie data structure
import Trie as T

# Importing deque from collections module for efficient queue operations
from collections import deque

# Importing time module for measuring execution time
import time


class CompoundWordFinder:
    def __init__(self) -> None:
        """
        Initializes a CompoundWordFinder object with a Trie and a deque.
        """

        # Initialize a Trie data structure
        self.trie = T.Trie()

        # Initialize a deque for processing compound word candidates
        self.queue = deque()

    def buildTrie(self, filePath: str = None) -> None:
        """
        Builds a Trie from words in a file.

        Args:
            filePath (str): Path to the file containing words. Defaults to None.
        """
        try:
            with open(filePath, mode='r') as f:
                for line in f:
                    # Process each word in the file

                    # Remove newline character from the end of the word
                    word = line.rstrip('\n')

                    # Get prefixes of the word from the Trie
                    prefixes = self.trie.get_prefixes(word)
                    for prefix in prefixes:
                        # Divide the word into word-suffix pairs and add them to the queue
                        self.queue.append((word, word[len(prefix):]))

                        # Insert the word into the Trie
                    self.trie.insert(word)
        except FileNotFoundError:

            # Handle file not found error
            print("File not found!")
        except Exception as e:

            # Handle other errors
            print("Error occurred while processing file:", e)

    def findLongestCompoundWords(self) -> tuple:
        """
        Finds the First Longest and Second-Longest compound words.

        Returns:
            tuple: A tuple containing the First Longest and Second-Longest compound words.
        """

        # Initialize variable to store the longest compound word
        longest_word = ''

        # Initialize variable to store the length of the longest compound word
        longest_length = 0

        # Initialize variable to store the second-longest compound word
        second_longest = ''


        # Iterate through the queue until it's empty
        while self.queue:

            # Get the next word-suffix pair from the queue
            word, suffix = self.queue.popleft()

            # Check if the suffix is a valid word in the Trie and if the current word is longer than the longest one found so far
            if suffix in self.trie and len(word) > longest_length:

                # Update the second-longest word
                second_longest = longest_word

                # Update the longest word
                longest_word = word

                # Update the length of the longest word
                longest_length = len(word)
            else:

                # If the suffix is not a valid word, get prefixes of the suffix and add new word-suffix pairs to the queue
                prefixes = self.trie.get_prefixes(suffix)
                for prefix in prefixes:
                    # Add word-suffix pair to the queue
                    self.queue.append((word, suffix[len(prefix):]))

        # Return the longest and second-longest compound words
        return (longest_word, second_longest)


# The Main execution block
if __name__ == "__main__":
    # Create an instance of CompoundWordFinder
    word_finder = CompoundWordFinder()

    # Record the start time
    start_time = time.time()

    # Build Trie from words in the input files
    # word_finder.buildTrie("Input_01.txt")
    word_finder.buildTrie("Input_02.txt")

    # Find the longest and second-longest compound words
    first_longest, second_longest = word_finder.findLongestCompoundWords()

    # Record the end time
    end_time = time.time()

    # Print results
    print("Longest Compound Word:", first_longest)
    print("Second Longest Compound Word:", second_longest)

    # Print the execution time
    print("Time taken: ", str(end_time - start_time), "seconds")
