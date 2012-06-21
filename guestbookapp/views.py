"""
    guestbookapp.views
    ===================

"""
from django.views.generic.simple import direct_to_template
from django.shortcuts import redirect

from guestbookapp.models import Message


def home(request):
    template_values = {}

    if request.method == "POST":
        msg = request.POST.get('message')
        if msg:
            new_msg = Message(text=msg)
            new_msg.put()            
            return redirect(home)
            
        template_values['error'] = True
        
    query = Message.all().order('-created');
    template_values['message_list'] = query.fetch(limit=25)

    return direct_to_template(request, 'guestbookapp/guestbook.html', template_values)