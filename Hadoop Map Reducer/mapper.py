import sys

c1 = sys.argv[1]
c2 = sys.argv[2]

def mapper():
    category = ""
    video_id = ""
    country = ""
    indicator = 0
    for line in sys.stdin:
      line = line.strip()
      parts = line.split(",")
      if parts[0] == "video_id":
          continue
      if parts[17] == c1:
          category = parts[5]
          video_id = parts[0]
          country = parts[17]
          indicator = 1
      print("{}\t{}\t{}\t{}".format(category,video_id,country,indicator))

      if parts[17] == c2:
          category = parts[5]
          video_id = parts[0]
          country = parts[17]
          indicator = 2
      print("{}\t{}\t{}\t{}".format(category, video_id, country, indicator))


if __name__ == "__main__":
    mapper()





