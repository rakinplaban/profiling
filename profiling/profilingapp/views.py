from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404,redirect

from .models import Profile
from .forms import ProfileForm

# Create your views here.

def index(request):
    profile_list = Profile.objects.all()
    
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect(request.path_info)
        else:
            form = ProfileForm()
            return redirect(request.path_info)
    
    else:
        context = {
            'profile_list': profile_list
        }
        return render(request, 'index.html', context)


def profile_create(request):
    data = dict()

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            
            # Fetch the updated profile list
            profile_list = Profile.objects.all()
            context = {
                'profile_list': profile_list
            }

            data['valid'] = True
            data['success'] = render_to_string('success/create-success.html', context)
            data['profile_list'] = render_to_string('profile/profile_list.html', context)
            return JsonResponse(data)
        
        else:
            # Include form errors in the response
            data['html_form'] = render_to_string('profile/profile_create.html', {'form': form}, request=request)
            return JsonResponse(data)

    else:
        # Render the form for the first time
        data['html_form'] = render_to_string('profile/profile_create.html', {'form': ProfileForm()}, request=request)
        return JsonResponse(data)


def profile_edit(request, id):
    
    data = dict()
    
    profile = get_object_or_404(Profile,id=id)
    
    profile_dic = {
        'profile': profile
    }

    if request.method == 'POST':
        
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        
        if form.is_valid():
            form.save()
            
            profile_list = Profile.objects.all()
            context = {
                'profile_list': profile_list
            }

            data['valid'] = True
            data['success'] = render_to_string('success/edit-success.html')
            data['profile_list'] = render_to_string('profile/profile_list.html', context)
            return JsonResponse(data)
        
        else:
            data['edit_form'] = render_to_string('profile/profile_edit.html', profile_dic)
            return JsonResponse(data)
    
    else:
        data['edit_form'] = render_to_string('profile/profile_edit.html', profile_dic)
        return JsonResponse(data)


def profile_delete(request, id):
    data = dict()
    profile = get_object_or_404(Profile, id=id)  # Use get_object_or_404 for better error handling
    
    if request.method == 'POST':
        profile.delete()
        profile_list = Profile.objects.all()
        context = {'profile_list': profile_list}
        data['valid'] = True
        data['success'] = render_to_string('success/delete-success.html')
        data['profile_list'] = render_to_string('profile/profile_list.html', context)
        return JsonResponse(data)
    else:
        context = {'profile': profile}
        data['delete_form'] = render_to_string('profile/profile_delete.html', context, request=request)
        return JsonResponse(data)