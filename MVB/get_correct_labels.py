with open('labels.csv', 'r', encoding = 'utf-8') as infile :
  ouf = open('labels.txt', 'w', encoding = 'utf-8')
  x = infile.readline()
  x = infile.readline()
  while len(x) > 0 :
    ouf.write(x.replace(',', ' '))
    x = infile.readline()
