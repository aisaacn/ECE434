Isaac Austin
ECE 434 - Homework 4

Start by running ./on.sh to setup the ports

To display an image, use 

	sudo fbi -noverbose -T 1 -a boris.png

To rotate an image 90 degrees, use

	convert rotate "90" boris.png boris90.png

To display video, use

	mvplayer hst_1.mpg

To rotate and display a video, use

	mvplayer -vf rotate hst_1.mpg

To display an image with text, use

	./text.sh (might take a while)

Inside text.sh is a convert command that edits the original boris.png file
	to include text and specify font.


