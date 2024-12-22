from django.shortcuts import render, redirect, get_object_or_404
from .models import Car
from .forms import CarForm

# Create your views here.

def car_list(request):
    """Отображение всех машин"""
    cars = Car.objects.all()
    return render(request, 'Car/car_list.html', {'cars':cars})

def car_create(request):
    """Создание новой машины"""
    if request.method == 'POST':
        form = CarForm(request.POST) #NOTE:Не забывать передавать данные через request.POST
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm()
    return render(request, 'Car/car_create.html', {'form':form})

def car_update(request,pk):
    """Обновление машины"""
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm(instance=car)
    return render(request, 'Car/car_update.html', {'car':car, 'form':form})

def car_delete(request,pk):
    """Удалние машины"""
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        car.delete()
        return redirect('car_list')
    return render(request, 'Car/car_delete.html', {'car':car})

def car_detail(request,pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'Car/car_detail.html', {'car':car})





