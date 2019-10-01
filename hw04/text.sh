# Here's how to use imagemagick to display text
# Make a blank image
SIZE=320x240
TMP_FILE=/tmp/frame.png

# From: http://www.imagemagick.org/Usage/text/
convert boris.png -fill black -font Times-Roman -pointsize 240 \
      -size $SIZE \
      -draw "text 0,200 'Isaac Austin'" \
      $TMP_FILE

sudo fbi -noverbose -T 1 -a $TMP_FILE

# convert -list font
