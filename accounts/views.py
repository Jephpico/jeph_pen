from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


# Create your views here.


#def SignUpView(request):
 #   if request.method == 'POST':
  #      form = UserCreationForm(request.POST)
   #     if form.is_valid():
    #        form.save()
     #       return HttpResponseRedirect ('Blog: PostList')

   
#    else:
 #       form = UserCreationForm()
  #      return render (request, 'accounts\signup.html', {'form':form} )

class  SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')
    



    def save(request):
        data = request.POST
        data.save()


#class  LoginView(generic.CreateView):






def email(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['receiver@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return redirect('redirect to a new page')