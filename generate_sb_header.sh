FN=`basename "$1"`
BASE=${FN%.*}
sdef "$1" | sdp -fh --basename "$BASE" -o ~/Desktop
