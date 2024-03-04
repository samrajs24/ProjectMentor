from django.shortcuts import render, get_object_or_404, redirect
from .models import LearningItem
from .forms import LearningItemForm

from django.views import View
from django.http import JsonResponse
from django.db.models import Q
from .models import LearningItem
from django.urls import reverse
# Create your views here.

class LearningItemsList(View):
    def get(self, request):
        learning_items = LearningItem.objects.all()
        return render(request, 'learning_items_list.html', {'learning_items': learning_items})

class LearningItemDetail(View):
    def get(self, request, pk):
        learning_item = get_object_or_404(LearningItem, pk=pk)
        return render(request, 'learning_item_detail.html', {'learning_item': learning_item})

class LearningItemCreate(View):
    def get(self, request):
        form = LearningItemForm()
        return render(request, 'learning_item_form.html', {'form': form})

    def post(self, request):
        form = LearningItemForm(request.POST, request.FILES)
        if form.is_valid():
            learning_item = form.save()
            return redirect(reverse('learning_item_detail', kwargs={'pk': learning_item.pk}))
        return render(request, 'learning_item_form.html', {'form': form})

class LearningItemUpdate(View):
    def get(self, request, pk):
        learning_item = get_object_or_404(LearningItem, pk=pk)
        form = LearningItemForm(instance=learning_item)
        return render(request, 'learning_item_form.html', {'form': form})

    def post(self, request, pk):
        learning_item = get_object_or_404(LearningItem, pk=pk)
        form = LearningItemForm(request.POST, request.FILES, instance=learning_item)
        if form.is_valid():
            learning_item = form.save()
            return redirect(reverse('learning_item_detail', kwargs={'pk': learning_item.pk}))
        return render(request, 'learning_item_form.html', {'form': form})

class LearningItemDelete(View):
    def get(self, request, pk):
        learning_item = get_object_or_404(LearningItem, pk=pk)
        return render(request, 'learning_item_confirm_delete.html', {'learning_item': learning_item})

    def post(self, request, pk):
        learning_item = get_object_or_404(LearningItem, pk=pk)
        learning_item.delete()
        return redirect('learning_items_list')


class SearchView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('query', '')
        
        # Perform search query against your learning item model
        results = LearningItem.objects.filter(
            Q(title__icontains=query) |   # Search title field for partial matches
            Q(description__icontains=query)  # Search description field for partial matches
        )
        
        # You may customize this part to format the search results according to your needs
        search_results = []
        for result in results:
            search_results.append({
                'title': result.title,
                'description': result.description,
                'profile_picture_url': result.profile_picture.url if result.profile_picture else None,
                'mentor_name': result.name,
                'start_time': result.start_time.strftime("%Y-%m-%d %H:%M:%S") if result.start_time else None,
                'end_time': result.end_time.strftime("%Y-%m-%d %H:%M:%S") if result.end_time else None,
            })
        
        # Return the search results as JSON response
        return JsonResponse({'results': search_results})
