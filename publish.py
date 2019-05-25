import sys, os
from dotenv import load_dotenv
load_dotenv()
INPUTDIR = os.path.join(sys.path[0], 'content')
OUTPUTDIR = os.path.join(sys.path[0], 'output')
PUBLISHCONF = os.path.join(sys.path[0], 'publishconf.py')
os.system('pelican %s -o %s -s %s' % (INPUTDIR, OUTPUTDIR, PUBLISHCONF))
