# ~/projects/django-web-app/merchex/listings/views.py

from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Comic
from listings.forms import ContactUsForm, BandForm, ComicForm
from django.core.mail import send_mail
from django.shortcuts import redirect 


def band_list(request):  # renommer la fonction de vue
    bands = Band.objects.all()
    return render(request,
                  'listings/band_list.html',  # pointe vers le nouveau nom de modèle
                  {'bands': bands})


def band_detail(request, id):  # notez le paramètre id supplémentaire
    band = Band.objects.get(id=id)
    # nous passons l'id au modèle
    return render(request, 'listings/band_detail.html', {'band': band})


def about(request):
    one_comic = Comic.objects.all()
    return render(request, 'listings/comics.html', {"one_comic": one_comic})


def comic_detail(request, id):
    comic = Comic.objects.get(id=id)
    return render(request, 'listings/comic_detail.html', {'comic': comic})


def contact(request):
    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
        )
        return redirect('email-sent')  # ajoutez cette instruction de retourn
    # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).

    else:
        # ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactUsForm()

    return render(request,
                'listings/contact.html',
                {'form': form})


def band_create(request):
   form = BandForm()
   return render(request,
            'listings/band_create.html',
            {'form': form})


def band_update(request, id):
    band = Band.objects.get(id=id)
    form = BandForm(instance=band)  # on pré-remplir le formulaire avec un groupe existant
    return render(request,
                            'listings/band_update.html',
                            {'form': form})

def comic_create(request):
        if request.method == 'POST':
            form = ComicForm(request.POST)
            if form.is_valid():
                comic = form.save()

                return redirect('comic-detail', comic.id)
            
        else:
            form = ComicForm()

        return render(request,
            'listings/comic_create.html',
            {'form': form})


def comic_update(request, id):
    comic = Comic.objects.get(id=id)

    if request.method == 'POST':
        form = ComicForm(request.POST, instance=comic)
        if form.is_valid():
            #maj du comic dans la bdd
            form.save()
            # retour à la page du comic
            return redirect('comic-detail', comic.id)
        
        else:
            form = ComicForm(instance=comic)


    form = ComicForm(instance=comic)
    return render(request, 'listings/comic_update.html', {'form': form})


def comic_delete(request, id):
    comic = Comic.objects.get(id=id)

    if request.method == 'POST':
        comic.delete()
        return redirect('comic-list')

    return render(request, 'listings/comic_delete.html', {'comic' : comic})