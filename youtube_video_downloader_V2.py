from pytube import YouTube, Playlist
from pytube.cli import on_progress


# Download a single video
def vedio_downloader():
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
            vedio.streams.get_highest_resolution().download()
            break
        elif check_vedio == "n":
            choose = str(input("Tryagin....(y/n)? ") or "y")
            if choose == "y":
                vedio_downloader()
            else:
                print("Have a nice day...")
                break
        else:
            print("please choose....(y/n)")


# Download Playlist
def playlist_downloader():
    link  = input("\nEnter Link   : ")
    p = Playlist(link)

    print(f"Playlist Title: {p.title}")
    while True:
        check_playlist = str(input("Is this the Playlist you want.....(y/n) ") or "y")
        if check_playlist == "y":
             for video in p.videos:
                print(f"Vedio Title  : {video.title}")
                video.streams.get_highest_resolution().download()
        elif check_playlist == "n":
            choose = str(input("Tryagin....(y/n)? ") or "y")
            if choose == "y":
                playlist_downloader()
            else:
                print("Have a nice day...")
                break
        else:
            print("please choose....(y/n)")
   

# the main program 
def main():
    print("Welcome to Youtube Downloader....")
    print("What do you want to download.")

    while True:
        choice = input("[1] video\n[2] Playlist\n==> Enter (1) or (2): ")
        if choice.isdigit():
            if int(choice) == 1:
                vedio_downloader()
                break
            elif int(choice) ==2:
                playlist_downloader()
                break
            else:
                print("\n\t\t    Invalid Input")
                print("\tHINT: 1,2 are the only valid inputs.\n")
        else:
            print("\n\tInvalid input please try agin **[only intgers are allowed]\n")
        
            

main()
