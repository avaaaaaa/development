LETTERS = [chr(i) for i in range(65, 91)]
POINTS = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
LETTER_TO_POINTS = {k: v for k, v in zip(LETTERS, POINTS)}


def score_word(word):
    word = word.upper()
    return sum(
        [LETTER_TO_POINTS.get(char, 0) for char in word]
    )

def play_word(player, word, player_to_words, player_to_points):
    try:
        player_to_words[player].append(word)
        update_total_points(player, word, player_to_points)
    except KeyError:
        print(f"player \"{player}\" not found")

def calculate_total_points(player_to_words):
    player_to_points = dict()
    for k in player_to_words.keys():
        player_words = player_to_words[k]  # words for each player
        player_points = map(score_word, player_words)  # points for each word
        total = sum(player_points)  # sum of all points
        player_to_points[k] = total  # entry for dictionary
    return player_to_points

def update_total_points(player, word, player_to_points):
    player_to_points[player] += score_word(word)


brownie_points = score_word("brownie")
print(brownie_points)

player_to_words = {
    "player1": ["blue", "tennis", "exit"],
    "wordNerd": ["earth", "eyes", "machine"],
    "Lexi Con": ["eraser", "belly", "husky"],
    "Prof Reader": ["zap", "coma", "period"]
}

player_to_points = calculate_total_points(player_to_words)
print(player_to_points)

play_word("Lexi Con", "follow", player_to_words, player_to_points)
print(player_to_points)
