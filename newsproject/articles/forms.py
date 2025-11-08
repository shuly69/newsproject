from django import forms
from .models import Articles, Categories, SubCategories



class ArticleForm(forms.ModelForm):
        title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Enter article title'})
    )
        image = forms.ImageField( 
        widget=forms.ClearableFileInput(attrs={'style': 'display:none','accept': 'image/*', 'id': 'imageUpload'}),
    )
        excerpt = forms.CharField(    
        widget=forms.Textarea(attrs={'class': 'textarea-el rich-text-editor', 'placeholder': 'Enter a brief summary of the article',}),
    )
        content = forms.CharField(
        widget=forms.Textarea(attrs={'id': 'quill-container',}),
    )
        meta_description = forms.CharField(
        required=False, 
        widget=forms.Textarea(attrs={'class': 'form-textarea', 'id': 'metaDescription', 'placeholder': 'Enter meta description for SEO', 'rows': 3}),
    )
        meta_keywords = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-input', 'id': 'metaKeywords', 'placeholder': 'Enter meta keywords for SEO'}),
    )
        category = forms.ModelChoiceField(
        queryset=Categories.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'articleCategory', 'required': True}),
    )
        subcategory = forms.ModelChoiceField(
        queryset=SubCategories.objects.all(),  # Initially no subcategories 
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'articleSubCategory'}),
    )
        
        status = forms.ChoiceField(
        choices=[('draft', 'Draft'), ('published', 'Published')],
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'articleStatus'}),
    )
        class Meta:
            model = Articles
            fields = '__all__'
         
        

