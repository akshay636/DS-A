def winnerOfGame(colors):
  print(colors[1 - 1:1 + 2])
  n = len(colors)
  if n < 3:
      return False

  alice_wins = 0
  bob_wins = 0
  for i in range(1, n - 1):
      if colors[i - 1:i + 2] == "AAA":
          alice_wins += 1
      elif colors[i - 1:i + 2] == "BBB":
          bob_wins += 1

  if alice_wins > bob_wins:
      return True
  else:
      return False
print(winnerOfGame('AKSHAY'))

        