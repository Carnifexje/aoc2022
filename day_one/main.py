if __name__ == "__main__":
  print(max([sum(map(int, t.split())) for t in open("input.txt").read().split("\n\n")]))
  print(sum(sorted([sum(map(int, t.split())) for t in open("input.txt").read().split("\n\n")])[-3:]))
