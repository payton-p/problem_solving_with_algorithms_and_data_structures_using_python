from chapter07_graphs.graph import Graph


def build_word_ladder_problem_graph(word_file):
    """Build a graph of words for the Word Ladder Problem."""

    dictionary = {}
    graph = Graph()
    file = open(word_file, "r")

    # Create buckets of words that differ by one letter.
    for line in file:
        word = line[:-1]

        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i + 1:]
            if bucket in dictionary:
                dictionary[bucket].append(word)
            else:
                dictionary[bucket] = [word]

    # Add vertices and edges for words in the same bucket.
    for bucket in dictionary.keys():
        for word1 in dictionary[bucket]:
            for word2 in dictionary[bucket]:
                if word1 != word2:
                    graph.add_edge(word1, word2)

    return graph


def main():
    # Build graph.
    graph = build_word_ladder_problem_graph("word_file1.txt")
    print(graph.get_vertices())


if __name__ == "__main__":
    main()
