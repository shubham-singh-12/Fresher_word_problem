# `TrieNode` represent a node in a trie
class TrieNode:
    """
    A TrieNode represents a single node in the Trie data structure.
    It contains a character, a dictionary of children nodes, and a flag to indicate if it's a terminal node.
    """

    def __init__(self, character=None, is_terminal: bool = False) -> None:
        """
        Initializes a TrieNode with the given character and terminal flag.
        """
        self.character = character
        self.children = {}
        self.is_terminal = is_terminal


class Trie:
    """
    Trie data structure for efficient string storage and retrieval.
    """

    def __init__(self) -> None:
        """
        Initializes an empty Trie with a root node.
        """
        self.root = TrieNode('')

    def insert(self, word: str) -> None:
        """
        Inserts a word into the Trie.
        """
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode(char)
            current_node = current_node.children[char]
        current_node.is_terminal = True

    def __contains__(self, word: str) -> bool:
        """
        Checks if the Trie contains a given word.
        """
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node.is_terminal

    def get_prefixes(self, word) -> list:
        """
        Returns all the possible prefixes of a word existing in the Trie.
        """
        prefix = ''
        prefixes = []
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return prefixes
            current_node = current_node.children[char]
            prefix += char
            if current_node.is_terminal:
                prefixes.append(prefix)
        return prefixes
