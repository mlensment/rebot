import argparse
__author__ = 'nixCraft'

parser = argparse.ArgumentParser(description='This is a demo script by nixCraft.')
parser.add_argument('-f', '--frame', help = 'Path of the frame to parse', required = False)
args = parser.parse_args()

## show values ##
print ("Input file: %s" % args.frame )
