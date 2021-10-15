import time
from pytube import YouTube
from pytube.cli import on_progress

link  = input("\nEnter Link   : ")
vedio = YouTube(link, on_progress_callback=on_progress)

print(f"Vedio Title  : {vedio.title}")
print(f"Vedio Views  : {vedio.views} view")
print(f"Vedio length : {int(vedio.length/60)} min")
print(f"Vedio Rating : {vedio.rating}\n")
	
while True:
	check_vedio = str(input("Is this the vedio you want.....(y/n) ") or "y")
	if check_vedio == "y":
		print("Downloading.......")
		vedio.streams.get_highest_resolution().download(output_path="D:\Web Development\Css Course\Vedioes")
		break
	elif check_vedio == "n":
		print("Exiting......")
		break
	else:
		print("please choose....(y/n)")












