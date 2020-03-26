from django import forms


class TopicForm(forms.Form):
    topic = forms.CharField(label='Your topic', max_length=100)


class KeyConceptsForm(forms.Form):
    concept1 = forms.CharField(label='Key Concept 1', max_length=100)
    concept2 = forms.CharField(label='Key Concept 2', max_length=100)
    concept3 = forms.CharField(label='Key Concept 3', max_length=100, required=False)
    concept4 = forms.CharField(label='Key Concept 4', max_length=100, required=False)


class RelatedForm1(forms.Form):
    concept1_keyword1 = forms.CharField(label='Keyword 1', max_length=100)
    concept1_keyword2 = forms.CharField(label='Keyword 2', max_length=100, required=False)
    concept1_keyword3 = forms.CharField(label='Keyword 3', max_length=100, required=False)
    concept1_keyword4 = forms.CharField(label='Keyword 4', max_length=100, required=False)
    concept1_keyword5 = forms.CharField(label='Keyword 5', max_length=100, required=False)
    concept1_keyword6 = forms.CharField(label='Keyword 6', max_length=100, required=False)
    concept1_keyword7 = forms.CharField(label='Keyword 7', max_length=100, required=False)


class RelatedForm2(forms.Form):
    concept2_keyword1 = forms.CharField(label='Keyword 1', max_length=100)
    concept2_keyword2 = forms.CharField(label='Keyword 2', max_length=100, required=False)
    concept2_keyword3 = forms.CharField(label='Keyword 3', max_length=100, required=False)
    concept2_keyword4 = forms.CharField(label='Keyword 4', max_length=100, required=False)
    concept2_keyword5 = forms.CharField(label='Keyword 5', max_length=100, required=False)
    concept2_keyword6 = forms.CharField(label='Keyword 6', max_length=100, required=False)
    concept2_keyword7 = forms.CharField(label='Keyword 7', max_length=100, required=False)


class RelatedForm3(forms.Form):
    concept3_keyword1 = forms.CharField(label='Keyword 1', max_length=100)
    concept3_keyword2 = forms.CharField(label='Keyword 2', max_length=100, required=False)
    concept3_keyword3 = forms.CharField(label='Keyword 3', max_length=100, required=False)
    concept3_keyword4 = forms.CharField(label='Keyword 4', max_length=100, required=False)
    concept3_keyword5 = forms.CharField(label='Keyword 5', max_length=100, required=False)
    concept3_keyword6 = forms.CharField(label='Keyword 6', max_length=100, required=False)
    concept3_keyword7 = forms.CharField(label='Keyword 7', max_length=100, required=False)


class RelatedForm4(forms.Form):
    concept4_keyword1 = forms.CharField(label='Keyword 1', max_length=100)
    concept4_keyword2 = forms.CharField(label='Keyword 2', max_length=100, required=False)
    concept4_keyword3 = forms.CharField(label='Keyword 3', max_length=100, required=False)
    concept4_keyword4 = forms.CharField(label='Keyword 4', max_length=100, required=False)
    concept4_keyword5 = forms.CharField(label='Keyword 5', max_length=100, required=False)
    concept4_keyword6 = forms.CharField(label='Keyword 6', max_length=100, required=False)
    concept4_keyword7 = forms.CharField(label='Keyword 7', max_length=100, required=False)


class EmailForm(forms.Form):
    user_name = forms.CharField(label="Your Name", max_length=100)
    user_email = forms.EmailField(label="Your Email", max_length=100)
    instructor_email = forms.EmailField(label="Instructor Email (optional)", max_length=100, required=False)
    course = forms.CharField(label="Course Prefix/Number", max_length=100, required=False)


