#!/usr/bin/python

import sys, getopt

def main(argv):
   inputfile = ''
   outputfile = ''
   meme = ''
   try:
      opts, args = getopt.getopt.getopt(argv,"hi:o:",["ifile=","ofile=","meme="])
   except getopt.GetoptError:
      print 'test.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
      elif opt in ("-m", "--meme"):
          meme = arg
   print 'Input file is "', inputfile
   print 'Output file is "', outputfile
   print 'meme is "', meme

if __name__ == "__main__":
   main(sys.argv[1:])
