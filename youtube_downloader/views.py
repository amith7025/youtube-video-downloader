from django.http import HttpResponse
from django.shortcuts import render
from pytube import YouTube


def home(request):
    return render(request,'index.html')


def result(request):
    djtext = request.POST.get('youtubelink','default')
    dpath = request.POST.get('pathname','default')
    dq144 = request.POST.get('q144','default')
    dq240 = request.POST.get('q240','default')
    dq360 = request.POST.get('q360','default')
    dq480 = request.POST.get('q480','default')
    dq720 = request.POST.get('q720','default')
    print(djtext,dq144,dq240,dq360,dq480,dq720)
    flag = False
    if dq144 == '144p':
       flag = download_video(text=djtext,quality=dq144,path=dpath)

    elif dq240 == '240p':
      flag = download_video(text=djtext,quality=dq240,path=dpath)

    elif dq360 == '360p':
     flag = download_video(text=djtext,quality=dq360,path=dpath)

    elif dq480 == '480p':
       flag = download_video(text=djtext,quality=dq480,path=dpath)

    elif dq720 == '720p':
      flag =  download_video(text=djtext,quality=dq720,path=dpath)

    if flag:
       return render(request,'result.html')
    else:
       return render(request,'error.html')

def download_video(text:str,quality:str,path:str):
    yt = YouTube(text)
    video_streams = yt.streams.filter(file_extension="mp4", progressive=True).order_by("resolution")
        # Print available resolutions
    for stream in video_streams:
        print(stream.resolution)
    selected_stream = video_streams.filter(res=quality).first()



    if selected_stream:
        selected_stream.download(output_path=path)
        #print("Download complete!")
        return True
    else:
        return False
    
