from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect

from models import WikiItem
from forms import WikiItemForm


def show_all_wiki_items(request):
    wiki_items = WikiItem.objects.all()

    return render_to_response(
        'wiki_items.html',
        {'wiki_items': wiki_items},
        context_instance=RequestContext(request)
    )

def add_wiki_item(request):
    wiki_item_form = WikiItemForm()
    if request.method == 'POST':
        wiki_item_form = WikiItemForm(request.POST)
        if wiki_item_form.is_valid():
            wiki_item_form.save()
            return HttpResponseRedirect('/wiki/novo_item/adicionado_com_sucesso/')

    return render_to_response(
        'add_wiki_item.html',
        {'wiki_item_form': wiki_item_form},
        context_instance=RequestContext(request)
    )

def view_wiki_item(request, wiki_item_id):
    wiki_item = get_object_or_404(WikiItem, id=wiki_item_id)

    return render_to_response(
        'wiki_item.html',
        {'wiki_item': wiki_item},
        context_instance=RequestContext(request)
    )
