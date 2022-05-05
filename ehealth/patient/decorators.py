from django.http import HttpResponse
from django.shortcuts import redirect
def check_patient(f):
	def wrapper(request,*args,**kwargs):
		d={"patient":1,"medecin":2,"pharmacist":3}
		role=request.session["role"]
		if role =="patient": 
			return f(request,*args,**kwargs)
		else:
			return redirect('landing:redirect',loginp=d[role])
		
	return wrapper