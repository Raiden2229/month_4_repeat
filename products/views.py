from django.shortcuts import render
from django.http import HttpResponse


def data_time(request):
    if request_method == "GET":
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return HttpResponse (current_time)



def first_products(request):
    if request.method == 'GET':
        return HttpResponse("кимчи, соллонтхан, пибимпап, сундубу чиге, самгетхан")
    
def second_products(request):
    if request.method == 'GET':
        return HttpResponse("")
    
def third_products(request):
    if request.method == 'GET':
        return HttpResponse('<img src="https://www.google.com/url?sa=t&source=web&rct=j&url=https%3A%2F%2Fwww.reddit.com%2Fr%2FSoulsSliders%2Fcomments%2Fswz6xe%2Fis_jetstream_sam_from_metal_gear_rising_possible%2F&ved=0CBQQjRxqFwoTCJiyxtC32ZEDFQAAAAAdAAAAABA9&opi=89978449">' <p>надеюсь это пойдет</p>)