from django import forms


class PostForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()

    def clean_title(self):
        cleaned_data = self.cleaned_data  # dict {}
        print(cleaned_data)
        title = cleaned_data.get('title')
        print(title)
        if title.lower().strip() == "tree":
            raise forms.ValidationError("This title already exists !!")
        return title
