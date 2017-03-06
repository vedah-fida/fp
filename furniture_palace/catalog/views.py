from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from catalog.models import Furniture
from django.core import serializers
from django.http import JsonResponse
from catalog.catalog import *


# Create your views here.
def get_furniture(request):
    furniture = Furniture.objects.all()
    serialized_furniture = serializers.serialize('json', furniture)
    return JsonResponse(serialized_furniture, safe=False)


@login_required(login_url='/')
def show_lent_tools(request):
    lent_tools_list = get_lent_tools()
    paginator = Paginator(lent_tools_list, 6)
    page = request.GET.get('page')
    try:
        lent_tools = paginator.page(page)
    except PageNotAnInteger:
        lent_tools = paginator.page(1)
    except EmptyPage:
        lent_tools = paginator.page(paginator.num_pages)

    return render(request, 'catalog/lent_tools_list.html', locals())


@login_required(login_url='/')
def show_tools_record(request):
    lent_tools_list = get_lent_tools_record()
    paginator = Paginator(lent_tools_list, 8)
    page = request.GET.get('page')
    try:
        lent_tools = paginator.page(page)
    except PageNotAnInteger:
        lent_tools = paginator.page(1)
    except EmptyPage:
        lent_tools = paginator.page(paginator.num_pages)

    return render(request, 'catalog/lent_tools_record.html', locals())


@login_required(login_url='/')
def lend_tool_page(request):
    tools = Tool.objects.all()
    temporary_carpenters = TempCarpenter.objects.all()
    return render(request, 'catalog/lend_tool.html', locals())


@login_required(login_url='/')
def lend_to_carpenter(request):
    tool = request.POST['tool']
    temp_carpenter = request.POST['temporary_carpenter']
    lend_tool(tool, temp_carpenter)

    msg = "You've successfully lend the tool"
    tools = Tool.objects.all()
    temporary_carpenters = TempCarpenter.objects.all()
    return render(request, 'catalog/lend_tool.html', {'tools': tools,
                                                      'temporary_carpenters': temporary_carpenters,
                                                      'msg': msg})


@login_required(login_url='/')
def update_lent_tool_page(request):
    lend_id = request.POST['lend_tool']
    lent_tool = get_lent_tool(lend_id)
    return render(request, 'catalog/lent_tool_return.html', locals())


@login_required(login_url='/')
def update_lent_tool(request):
    lend_id = request.POST['lend_id']
    returned = request.POST['returned']
    damaged = request.POST['damaged']
    update_lent_tool_with(lend_id, damaged, returned)

    msg = "Update successful"
    lent_tools = get_lent_tools()
    return render(request, 'catalog/lent_tools_list.html', locals())
