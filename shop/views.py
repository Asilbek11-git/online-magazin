from django.shortcuts import render, redirect
from django.contrib import messages  
from .models import Mahsulot 

def index(request):
    kategoriya_nomi = request.GET.get('kategoriya')




    if kategoriya_nomi and kategoriya_nomi.strip() != '':

        tozalangan_kategoriya = kategoriya_nomi.strip()
        

        mahsulotlar = Mahsulot.objects.filter(kategoriya__icontains=tozalangan_kategoriya)
    else:
        mahsulotlar = Mahsulot.objects.all()


    savat = request.session.get('savat', {})
    savat_soni = sum(savat.values())
    
    savat_mahsulotlari = Mahsulot.objects.filter(id__in=savat.keys())
    savat_jami = sum(m.narx * savat[str(m.id)] for m in savat_mahsulotlari)

    context = {
        'mahsulotlar': mahsulotlar,
        'savat_soni': savat_soni,
        'savat_jami': savat_jami,
        'tanlangan_kategoriya': kategoriya_nomi, 
    }

    return render(request, 'shop/mahsulot_list.html', context)


def savatga_qoshish(request, mahsulot_id):
    miqdor = int(request.GET.get('qty', 1))
    savat = request.session.get('savat', {})
    
    mahsulot_id_str = str(mahsulot_id)
    if mahsulot_id_str in savat:
        savat[mahsulot_id_str] += miqdor
    else:
        savat[mahsulot_id_str] = miqdor
        
    request.session['savat'] = savat
    request.session.modified = True
    
    messages.success(request, "Mahsulot savatga muvaffaqiyatli qo'shildi!")

    return redirect(request.META.get('HTTP_REFERER', 'index'))