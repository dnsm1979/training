from django.shortcuts import render, redirect

from .models import Positions
from .forms import PositionsForm


def client(request):

    positions = Positions.objects.all()
    form = PositionsForm()
    if request.method == "POST":
        form = PositionsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('positions')
    context = {"positions": positions, "form": form}
    return render(request, 'positions.html', context)
