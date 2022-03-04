from django.http import HttpResponse
from django.shortcuts import render


async def home(request):
    if request.method == 'POST':
        text1 = request.POST['text1']
        lang = request.POST['lang']
        a1 = text1.split('?v=')
        from youtube_transcript_api import YouTubeTranscriptApi
        
        a = YouTubeTranscriptApi.get_transcript(a1[1])

        str = ''
        for i in a:
            str += i['text']

        from googletrans import Translator
        a2 = Translator()

        # arr = []
        # for i in range(1, len2+1):
        #         b = a2.translate([0:15000], dest='gu')
        #         # b = a2.translate([(15000*i-1):(15000*i+1)], dest='gu')
        #         arr.append(b.text)
        b = a2.translate(str[0:15000], dest=lang)
        b1 = a2.translate(str[15000:30000], dest=lang)
        b2 = a2.translate(str[30000:], dest=lang)
        # b3 = a2.translate(str[45000:], dest=lang)

        # return render(request, f'home.html', {'hello': str, 'text': a1[1], 'answer': b.text + b1.text + b2.text})
        return render(request, f'base.html', {'hello': str, 'text': a1[1],'text1' :text1, 'answer': b.text + b1.text + b2.text , 'lang': lang})
    return render(request, f'base.html')


def eng(request):
    if request.method == 'POST':

        aksh = request.POST['aksh']

        from googletrans import Translator
        a2 = Translator()

        # arr = []
        # for i in range(1, len2+1):
        #         b = a2.translate([0:15000], dest='gu')
        #         # b = a2.translate([(15000*i-1):(15000*i+1)], dest='gu')
        #         arr.append(b.text)

        b = a2.translate(aksh[0:15000], dest='gu')
        b1 = a2.translate(aksh[15000:30000], dest='gu')
        b2 = a2.translate(aksh[30000:], dest='gu')
        b3 = a2.translate(aksh[45000:], dest='gu')
        # b1 = a2.translate(b.text, dest='hi')
        # print([1:100], type())
        # return render(request, f'base.html', {'hello': arr})
        return render(request, f'base.html', {'hello1': b.text})
        # return render(request, f'base.html', {'hello1': b.text + b1.text + b2.text})
    # print('rudra', request.GET['text123'])
