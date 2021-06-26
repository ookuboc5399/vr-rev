from django.views.generic import View
from django.shortcuts import render, redirect
from app.models import Blog,Product
from .forms import ContactForm,SearchForm
from django.core.mail import BadHeaderError, EmailMessage
from django.http import HttpResponse
from django.conf import settings
import textwrap


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/index.html', {
        })

class CONCEPTView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/concept.html', {
        })

class PRODUCTView(View):
    def get(self, request, *args, **kwargs):
        Product_data = Product.objects.order_by("-id")
        return render(request, 'app/product.html', {
            'Product_data': Product_data
        })

class BLOGView(View):
    def get(self, request, *args, **kwargs):
        post_data = Blog.objects.order_by("-id")
        return render(request, 'app/blog.html', {
            'post_data': post_data,
        })

class BLOGDetailView(View):
    def get(self, request, *args, **kwargs):
        post_data = Blog.objects.get(id=self.kwargs['pk'])
        return render(request, 'app/blog_detail.html', {
            'post_data': post_data
        })

class CONTACTView(View):
    def get(self, request, *args, **kwargs):
        form = ContactForm(request.POST or None)

        return render(request, 'app/contact.html', {
            'form': form
        })
    
    def post(self, request, *args, **kwargs):
        form = form = ContactForm(request.POST or None)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = 'お問い合わせありがとうございます。'
            content = textwrap.dedent('''
                ※このメールはシステムからの自動返信です。
                
                {name} 様
                
                お問い合わせありがとうございました。
                以下の内容でお問い合わせを受け付けいたしました。
                内容を確認させていただき、ご返信させて頂きますので、少々お待ちください。
                
                --------------------
                ■お名前
                {name}
                
                ■メールアドレス
                {email}
                
                ■メッセージ
                {message}
                --------------------
                ''').format(
                    name=name,
                    email=email,
                    message=message
                )

            to_list = [email]
            bcc_list = [settings.EMAIL_HOST_USER]

            try:
                message = EmailMessage(subject=subject, body=content, to=to_list, bcc=bcc_list)
                message.send()
            except BadHeaderError:
                return HttpResponse("無効なヘッダが検出されました。")

            return redirect('index') # 後で変更

        return render(request, 'app/contact.html', {
            'form': form
        })

class QUESTIONView(View):
    def get(self, request, *args, **kwargs):
        form = SearchForm(request.POST or None)

        return render(request, 'app/question.html', {
            'form': form
        })

class PRIVACYView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/privacy.html', {
        })