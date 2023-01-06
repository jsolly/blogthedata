from django import forms
from .models import Post

choices = [
    ("productivity", "productivity"),
    ("geodev", "geodev"),
    ("portfolio", "portfolio"),
    ("resources", "resources"),
]
# choices = Category.objects.all().values_list(
#     "name", "name"
# )
# comment this if doing an initial DB migration or changing databases.


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "title",
            "slug",
            "category",
            "metadesc",
            "draft",
            "metaimg",
            "metaimg_alt_txt",
            "metaimg_attribution",
            "content",
            "snippet",
        )

        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "autofocus": True}
            ),
            "slug": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "how-to-write-a-great-slug",
                }
            ),
            "category": forms.Select(choices=choices, attrs={"class": "form-control"}),
            "metadesc": forms.TextInput(attrs={"class": "form-control"}),
            "metaimg_alt_txt": forms.TextInput(attrs={"class": "form-control"}),
            "metaimg_attribution": forms.TextInput(attrs={"class": "form-control"}),
        }
