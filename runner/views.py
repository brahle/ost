import subprocess

from django.http import HttpResponse
from django.shortcuts import render

from ost.settings import EXECUTABLE, TIMEOUT

def main(request, start_speed=1.0):
	context = {
		'start_speed': start_speed,
		'timeout': TIMEOUT*1000,
	}
	return render(request, 'index.html', context)	

def run(request, parametar):
	proc = subprocess.Popen([EXECUTABLE, parametar], stdout=subprocess.PIPE)
	output = proc.stdout.read()
	return HttpResponse(output)

