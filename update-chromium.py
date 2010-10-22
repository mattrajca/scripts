#!/usr/bin/env python

import urllib2
import os

snapshots_url = "http://build.chromium.org/buildbot/snapshots/chromium-rel-mac/"

latest = urllib2.urlopen(snapshots_url + "LATEST").read()
print "Latest build: " + latest

full_url = snapshots_url + latest + "/chrome-mac.zip"

desktop_path = "~/Desktop"
zip_path = desktop_path + "/chrome-mac.zip"

# Download latest build
os.popen("curl -o " + zip_path + " " + full_url)
os.popen("unzip -d " + desktop_path + " " + zip_path)
os.popen("rm " + zip_path)

os.popen("killall Chromium")

name = "Chromium.app"
dest_path = "/Applications/Browsers/" + name
source_path = desktop_path + "/chrome-mac/" + name

os.popen("rm -dr " + dest_path)

os.popen("mv " + source_path + " " + dest_path)
os.popen("rm -dr " + desktop_path + "/chrome-mac")
