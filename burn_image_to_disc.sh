for f in "$@"
do
	echo -n "Started burning '`basename "$f"`'. This may take a while..." | growlnotify -a Automator
	hdiutil burn "$f"
	echo -n "Finished burning '`basename "$f"`'!" | growlnotify -a Automator
done
