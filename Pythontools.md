write a .txt file:
  with open('result.txt', 'a') as f:
    for i in range(100):
      f.write(str(i))
      f.write("\n")
f.close()
Notes: 'a' append new things at the end of result.txt, 'w' rewrite the results.txt, which means it will cover the orginal text. 