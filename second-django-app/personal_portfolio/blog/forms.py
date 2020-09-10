from django import forms

# @6.3

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={      # tell HTML to load this field as a Text Input element.
                "class": "form-control",        # attrs --> allows us to specify CSS classes. as well as a placeholder.
                "placeholder": "Your Name"
            }
        )
    )
    body = forms.CharField(
        widget=forms.Textarea(              # tell HTML to load a TEXT AREA element.
            attrs={
                "class": "form-control",
                "placeholder": "Leave a comment!"
            }
        )
    )

# When a form is posted, a POST request is sent to the server. So, in the view function we need to check if,
# a POST request has been received. We can then create a comment from the form fields.
# Django also comes with is_valid() so that we can check all fields have been entered correctly.

