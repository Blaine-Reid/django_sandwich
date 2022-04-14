
import random
from django.shortcuts import render
from django.views import View

menu ={
    'meats':['beef','chicken','turkey','pastrami'],
    'cheeses':['jack','cheddar','swiss','pepper jack'],
    'condiments':['mustard','mayo','vinegar'],
    'veggies':['lettace','tomato','onion','pickles','olives'],
    'breads':['white','rye','wheat','sourdough']
}

# Create your views here.
class IndexView(View):
    def get(self,request):

        return render(request=request, template_name='index.html')


class SandwichView(View):
    def get(self, request):
        return render(
            request=request,
            template_name='ingrediants.html',
            context={'menu':menu.keys()}
            )


class IngrediantView(View):
    def get(self, request, ingrediant):
        if request.method == "GET":
            if ingrediant in menu:
                return render(
                    request=request,
                    template_name='ingrediant_list.html',
                    context={
                        'ingrediant':ingrediant,
                        'ingrediants':menu[ingrediant]
                        })
            else:
                return render(
                    request=request,
                    template_name='404.html',
                )


class RandomView(View):
    def get(self, request):
        context={
            'meat': random.choice(menu['meats']),
            'cheese':random.choice(menu['cheeses']),
            'condiment':random.choice(menu['condiments']),
            'veggie':random.choice(menu['veggies']),
            'bread':random.choice(menu['breads']),
        }

        if request.method == 'GET':
            return render(
                request=request,
                template_name='random.html',
                context= context
            )


