from django.shortcuts import render
from random import choice

def index(request):
    return render(request,'index.html')


def show(request):

    Name = request.GET.get('text' , 'default')
    gfs = ['Neha','Chhavi' ,'Preety', 'Shurbhi', 'Angoori', 'anita', 'Sonam', 'Pooja', 'Kirti', 'Priya', 'Muskaan', 'Bhavana'
        , 'Prabha', 'Pinki', 'Shweta']

    complement = ['arrey ye to tatti h', 'Handsome boy', 'Number 1 in flirting',
                  'Dharti pe Boj', 'ittu sa h iska',
                  'Smarty londe', 'choribaaz', 'Dieheart Gabru', 'Bihaari hai sala', 'katai zeher',
                  'Chugalkhor', 'auntiyon pe buri nazar daalna band kar de', 'saale kutega tu to',
                  'andi bandi sandi aage samaj jaa', 'sala Feku', 'Hot man', 'maccho man', 'chal chakke'
        , 'Oe Aashiq', 'bhaag Bhutni ke', 'muh mein lele', 'bhai setting karva de ki rat lagana vala',
                  'Hurrrr bhaag bc']

    if request.GET.get("text") == ("Hemant"):
        gf = "Neha"
        comp = choice(complement)
        params = {'msg': Name, 'complement': comp, 'gf': gf}
        return render(request, 'show.html', params)

    elif  request.GET.get("text") == ("Abhisek"):
        gf = "Chhavi"
        comp = choice(complement)
        params = {'msg': Name, 'complement': comp, 'gf': gf}
        return render(request, 'show.html', params)

    elif  request.GET.get("text") == ("Golu"):
        gf = "varsha"
        comp = choice(complement)
        params = {'msg': Name, 'complement': comp, 'gf': gf}
        return render(request, 'show.html', params)

    elif  request.GET.get("text") == ("Kapil"):
        gf = "B***C"
        comp = "saale ye Name allowed nhi h dusra try kar BC"
        params = {'msg': Name, 'complement': comp, 'gf': gf}
        return render(request, 'show.html', params)

    elif  request.GET.get("text") == ("Anshul"):
        gf = choice(gfs)
        compl = "Smarty boy, All girls have crush on him"
        params = {'msg': Name, 'complement': compl, 'gf': gf}
        return render(request, 'show.html', params)


    else:
        gf = choice(gfs)
        comp = choice(complement)
        params = {'msg': Name, 'complement': comp, 'gf': gf}
        return render(request, 'show.html', params)










