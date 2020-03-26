from django.conf.urls import url
from .forms import *
from .views import KeywordWizard, error_404, error_500, search

all_keywords_forms = (
    ('topic', TopicForm),
    ('key_concepts', KeyConceptsForm),
    ('related1', RelatedForm1),
    ('related2', RelatedForm2),
    ('related3', RelatedForm3),
    ('related4', RelatedForm4),
)

keyword_wizard = KeywordWizard.as_view(all_keywords_forms, url_name='keyword_step',)

urlpatterns = [
    url(r'^keywords/(?P<step>.+)/$', keyword_wizard, name='keyword_step'),
    url(r'^keywords$', keyword_wizard, name='keyword'),
    url(r'^$', keyword_wizard, name='keyword'),
    url(r'^search$', search, name='search'),
]

handler404 = error_404
handler500 = error_500
