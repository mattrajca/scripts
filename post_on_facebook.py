import os
import sys
import urllib

URL = urllib.quote_plus(sys.argv[1])
os.system('open "http://www.facebook.com/sharer.php?u=' + URL + '"')
