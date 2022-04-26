from django.shortcuts import render
from django.db.models.aggregates import Count
from .models import AllMutuelle


def all_mutuelles(request):
    query_set = AllMutuelle.objects.all()
    total = AllMutuelle.objects.aggregate(total=Count("id"))
    pending = AllMutuelle.objects.filter(
        mutuelle_status__exact="P").aggregate(pending=Count('id'))
    complete = AllMutuelle.objects.filter(
        mutuelle_status__exact="C").aggregate(complete=Count('id'))
    return render(request, 'mutuelle/all_mutuelles.html', {'patient': True, 'all_mutuelles': True, 'mutuelles': query_set, 'total_mutuelles': total['total'], 'pending': pending['pending'], 'complete': complete['complete']})
