from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from formtools.wizard.views import CookieWizardView

from .forms import *
from .populate import Populator


FORMS = [("topic", TopicForm),
         ("key_concepts", KeyConceptsForm),
         ("related1", RelatedForm1),
         ("related2", RelatedForm2),
         ("related3", RelatedForm3),
         ("related4", RelatedForm4),
         ]

TEMPLATES = {"topic": "topic.html",
             "key_concepts": "key_concepts.html",
             "related1": "related.html",
             "related2": "related.html",
             "related3": "related.html",
             "related4": "related.html",

             }

CURRENT_CONCEPT = {"related1": "concept1",
                   "related2": "concept2",
                   "related3": "concept3",
                   "related4": "concept4", }


def key_concept3_exists(hermione):
    cleaned_data = hermione.get_cleaned_data_for_step('key_concepts') or {'concept3': ''}
    return bool(cleaned_data['concept3'])


def key_concept4_exists(hermione):
    cleaned_data = hermione.get_cleaned_data_for_step('key_concepts') or {'concept4': ''}
    return bool(cleaned_data['concept4'])


class KeywordWizard(CookieWizardView):
    url_name = 'keyword_step'
    condition_dict = {"related3": key_concept3_exists, "related4": key_concept4_exists}
    initial_dict = {'search': {'query': ''}}

    def get_context_data(self, form, **kwargs):
        context = super(KeywordWizard, self).get_context_data(form=form, **kwargs)
        if self.steps.current == 'key_concepts' or self.steps.current == 'related':
            cleaned_data = self.get_cleaned_data_for_step('topic')
            context.update({'topic_term': cleaned_data['topic']})
        if 'related' in self.steps.current:
            key_concepts_dictionary = self.get_cleaned_data_for_step('key_concepts')
            current_concept = key_concepts_dictionary[CURRENT_CONCEPT[self.steps.current]]
            context.update({'key_concepts': key_concepts_dictionary,
                            'current_concept': current_concept})
        return context

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        all_the_things = self.get_all_cleaned_data()
        data = Populator.create_dict(all_the_things)
        search_data = Populator.create_query(data)
        self.request.session['search_data'] = {'data': data, 'search': search_data}
        return redirect('keywords/search')


def error_404(request, exception=None):
    return render(request, '404.html')


def error_500(request, exception=None):
    return render(request, '500.html')


def search(request):
    context = request.session.get('search_data', None)
    if context is None:
        return HttpResponseRedirect("keywords")
    context['email_form'] = EmailForm
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            params = {}
            params['user_name'] = form.cleaned_data['user_name']
            params['user_email'] = form.cleaned_data['user_email']
            params['instructor_email'] = form.cleaned_data['instructor_email']
            params['course'] = form.cleaned_data['course']
            params['subject'] = 'Results of Keyword Tool'
            params['sender'] = 'INSTITUTION_EMAIL' # TODO: edit with your institution's email
            params['query'] = context['search']
            plain_message = render_to_string('email.txt', {'params': params})
            html_message = render_to_string('email.html', {'params': params})
            recipients = [params['user_email'], params['instructor_email']]
            send_mail(params['subject'], plain_message, params['sender'], recipients, html_message=html_message)
            messages.success(request, 'Email sent successfully.')
            return HttpResponseRedirect("keywords/search")
    return render(request, 'search.html', context)
