from django.shortcuts import render
from django.http import HttpResponse
from random import choice

def index(request):
    return render(request,'index.html')


def show(request):

    Name = request.GET.get('text' , 'default')
    gfs = ['Neha','Chhavi' ,'Preety', 'Shurbhi', 'Angoori', 'anita', 'Sonam', 'Pooja', 'Kirti', 'Priya', 'Muskaan', 'Bhavana'
        , 'Prabha', 'Pinki', 'Shweta']

    complement = ['arrey ye to tatti h', 'Handsome boy', 'Number 1 in flirting',
                  'Dharti pe Boj', 'kya H ye Naam enter karvaya h kya Enter kar rha h "tatti"',
                  'Smarty londe', 'choribaaz', 'Dieheart Gabru', 'Bihaari hai sala', 'katai zeher',
                  'Chugalkhor', 'auntiyon pe buri nazar daalna band kar de', 'saale kutega tu to',
                  'andi bandi sandi aage samaj jaa', 'sala Feku', 'Hot man', 'maccho man', 'chal chakke'
        , 'Oe Aashiq', 'bhaag Bhutni ke', 'muh mein lele', 'bhai setting karva de ki rat lagana vala',
                  'Hurrrr bhaag bc']


    gf = choice(gfs)
    comp = choice(complement)
    params = {'msg': Name, 'complement': comp, 'gf': gf}
    return render(request, 'show.html', params)


















