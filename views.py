from django.shortcuts import render

# Create your views here.
def disp3_data(request):
	return render(request=request,template_name='html/professionalapp/disp3.html')
def disp4_data(request):
	return render(request=request,template_name='html/professionalapp/disp4.html')