"""Compute a team's score for a (fictitious) word game.

In this game, two players independently find words in a matrix of letters.
Each player's words are added to a text file with one word per line. Duplicates
are removed from each player's list. For each word that appears on both players'
lists, the team's score increases by the number of letters in the word minus 2
(words less than three characters long are not worth any points).
"""


from argparse import ArgumentParser
import sys


# Replace this comment with your implementation of the PlayerWords class and the
# main() function.
#Do not make attribute for file, make attribute for words that is set
# Self has one attribute words (set), gets it from init method
# Player has attribute word, data type set
class PlayerWords:
    """A class to represent a player's unique set of words found in the word 
    game.
    
    Attributes:
        words (set): A set of strings containing the unique words found by the 
        player.
    """
    def __init__(self, file_path):
        """Initialize the PlayerWords instance by reading words from a given
        file path.
        
        Args:
            file_path (str): The path to a text file containing words found by 
            a player.
            
        Side effects:
            Reads from a file and stores the words in a set attribute.
        """
        with open(file_path, "r") as f:
            self.words = set(word.strip() for word in f.readlines())
        
    def score(self, other):
        """Calculate the score for common words between this player and another 
        player.
        
        The score for each common word is the number of letters in the word 
        minus 2. Words less than three characters long are not worth any points.
        
        Args:
            other (PlayerWords): Another PlayerWords instance to compare words 
            with.
            
        Returns:
            int: The total score for all common words found by both players.
        """
        # Find the common words between both players
        common_words = self.words.intersection(other.words)
        # Calculate the score based on the length of each common word
        return sum(max(len(word) - 2, 0) for word in common_words)

def main(wordfile1, wordfile2):
    """Create PlayerWords instances for two players, compute the team's score,
    and print it.
    
    Args:
        wordfile1 (str): Path to a text file containing words found by player 1.
        wordfile2 (str): Path to a text file containing words found by player 2.
    
    Side effects:
        Prints the team's score to the console.
    """
    # Create PlayerWords instances for each file
    player1 = PlayerWords(wordfile1)
    player2 = PlayerWords(wordfile2)
    # Compute the team's score
    team_score = player1.score(player2)
    # Print out the team's score
    print(f"Your team scored {team_score} points!")

def parse_args(arglist):
    """Parse command line arguments.
    
    Expect two mandatory arguments:
        - str: path to a text file containing words found by player 1.
        - str: path to a text file containing words found by player 2.
    
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace.
    """
    parser = ArgumentParser()
    parser.add_argument("wordfile1", help="file containing player 1's words")
    parser.add_argument("wordfile2", help="file containing player 2's words")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.wordfile1, args.wordfile2)
