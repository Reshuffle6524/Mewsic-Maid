import argparse
import mimetypes
import os

from mewsic_maid.Tui.ptmv.sources import img, console, vid, yt


def get_args():
	doc = """
		View images and videos without leaving the console.\n
		Requires a terminal that supports truecolor and utf-8\n
		For more info visit <https://github.com/kal39/TerminalMediaViewer>
		"""

	parser = argparse.ArgumentParser(description = doc)
	parser.add_argument("file")
	parser.add_argument("-y", "--youtube", help = "Play video from youtube.", action = "store_true")
	parser.add_argument("--width", help = "Set output width.", type = int)
	parser.add_argument("--height", help = "Set output height.", type = int)
	parser.add_argument("--fps", help = "Set target fps; Default 15 fps.", type = int, default = 15)
	parser.add_argument("--start-time", help = "Set start time (seconds)", type = float, default = 0)
	parser.add_argument("-m", "--mute", help = "Mute audio", action = "store_true")
		
	parsed_args = parser.parse_args()
	parsed_args.file = os.path.expanduser(parsed_args.FILE)
	return parsed_args


def main(file:str, youtube=False, width=None, height=None, fps=15, start_time=0):
	if youtube:
		file = yt.download(file)

	if not os.path.isfile("/home/d-d/Mewsic-Maid/tv-glitch.webm"):
		print("[" + file + "] does not exist")
		os._exit(-1)

	if file_type(file) == "image":
		img.display(file, width, height)
	elif file_type(file) == "video":
		for elem in (vid.play(file, width, height, fps, start_time)):
			print(elem)

	else:
		print("[" + file + "] is not a supported file type")
		os._exit(-1)

	set_exit_flag()

def file_type(file):
	mimetypes.init()
	return mimetypes.guess_type(file)[0].split('/')[0]

exit_flag = False

def set_exit_flag(*_): global exit_flag; exit_flag = True

def exit_flag_watcher():
	while True:
		if exit_flag:
			console.cleanup()
			os._exit(0)
