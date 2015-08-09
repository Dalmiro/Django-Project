from django.template import RequestContext
from django.shortcuts import render_to_response, render, redirect
from blog.models import Entrada, Contacto, Comentario
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

def home(request):
	context = RequestContext(request)
	posts = Entrada.objects.all()
	post = Entrada.objects.filter(published = True)
   	return render_to_response('Sitio.html', {'posts':post}, context)

def cont(request):
	context = RequestContext(request)
	return render_to_response('Contacto.html',context)

def curric(request):
	context = RequestContext(request)
	return render_to_response('Curriculum.html',context)

def eje(request):
	context = RequestContext(request)
	return render_to_response('Ejercicios.html',context)

def calcu(request):
	context = RequestContext(request)
	return render_to_response('Calculadora.html',context)

def conver(request):
	context = RequestContext(request)
	return render_to_response('Conversor.html',context)

def crono(request):
	context = RequestContext(request)
	return render_to_response('Cronometro.html',context)

def boton(request):
	context = RequestContext(request)
	return render_to_response('Boton.html',context)

def loading(request):
	context = RequestContext(request)
	return render_to_response('BarraCarga.html',context)

def calcu(request):
	context = RequestContext(request)
	return render_to_response('Calculadora.html',context)

def ver_post(request, id_post):
    context = RequestContext(request)
    post = Entrada.objects.get(id=id_post)
    comentarios = Comentario.objects.filter(post_id = id_post)
    return render_to_response('post.html', {'post':post, 'mensajes':comentarios},context)

def contact(request):
    context = RequestContext(request)
    if request.method == 'POST':
        nombre= request.POST['nombre']
        mensaje= request.POST.get('mensaje')
        mail= request.POST['mail']
        contacto = Contacto()
        contacto.nombre = nombre
        contacto.mensaje = mensaje
        contacto.mail = mail
        contacto.save()
        
        send_mail(nombre, mensaje, settings.EMAIL_HOST_USER,['dalmirogrol@gmail.com'], fail_silently=False)
        
    return render_to_response('Contacto.html',
                              context)

def save_message(request):
    context = RequestContext(request)

    if request.method == 'POST':
        mi_post = Entrada.objects.get(id=request.POST['id'])
        nombre= request.POST.get('autor')
        msn= request.POST.get('mensaje')
        mail= request.POST.get('mail')      
        postid = request.POST.get('id') 
        mensaje = Comentario()
        mensaje.autor = nombre
        mensaje.mail = mail
        mensaje.mensaje = msn
        mensaje.post = mi_post
        mensaje.save()
    postid = request.POST.get('id')
    mensajes = Comentario.objects.filter(post=postid)

    return render_to_response('comentarios.html', 
                              {'mensajes':mensajes},
                              context)

        
def ver_mensajes(request, id_mensaje):
    context = RequestContext(request)
    mensajes = Entrada.objects.filter(published = True)
    return render_to_response('post.html', 
                              {'mensaje':mensajes},
                              context)




