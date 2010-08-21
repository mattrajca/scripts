URL=`curl http://pastie.caboo.se/pastes/create \
	-H "Expect:" \
	-F "paste[parser]=plaintext" \
	-F "paste[body]=$@" \
	-F "paste[authorization]=burger" \
	-s -L -o /dev/null -w "%{url_effective}"`

echo -n "$URL" | pbcopy
echo -n "Copied the Pastie URL to the pasteboard" | growlnotify -a Automator
