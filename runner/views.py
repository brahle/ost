import subprocess

from django.shortcuts import render

# Create your views here.
def pokreni(request):
	proc = subprocess.Popen('dir', stdout=subprocess.PIPE)
	output = proc.stdout.read()
	return output

