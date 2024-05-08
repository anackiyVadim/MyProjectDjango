from django.contrib.auth import logout, authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.timezone import now
import asyncio

from .forms import RegisterForm, FavoriteForm, CombinedForm, Re_Password, CommentForm, FeedbackForm
from .models import Product, MainSlider, Leaders, News, Tegs, Catalog, Profile, FeaturedProducts, ProductImagesDescr, \
    Comment
from baskCart.forms import CartAddProductForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


def base():
    catalogList = Catalog.objects.all().order_by("pk")
    productGiro = Product.objects.all()
    cart_product_form = CartAddProductForm()
    context = {'catalogList': catalogList, 'productGiro': productGiro, 'cart_product_form': cart_product_form}
    return context


def index(request):
    # productGiro = Product.objects.all()
    mainSlider = MainSlider.objects.all()
    leaders = Leaders.objects.all()
    news = News.objects.all().order_by("-published_date")
    context = {"mainSlider": mainSlider, "leaders": leaders, "news": news}
    context.update(base())
    return render(request, 'firstApp/index.html', context)


def search(request):
    query = request.GET.get('query')
    product = Product.objects.filter(Q(descriptions__icontains=query) | Q(name__icontains=query))
    order_by = request.GET.get('order_by')
    if order_by:
        product = product.order_by(order_by)
    context = {"product": product, "query": query}
    context.update(base())
    return render(request, 'firstApp/catalog.html', context)


def catalog(request, name=None):
    try:
        c = get_object_or_404(Catalog, name=name)
        tegs = Tegs.objects.filter(category=c)
        products = Product.objects.filter(category=c)
        order_by = request.GET.get('order_by')
        if order_by:
            products = products.order_by(order_by)
        paginator = Paginator(products, 9)
        page = request.GET.get('page')
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
        context = {'product': products, 'teg': tegs, 'c': c}
    except BaseException:
        c_с = get_object_or_404(Tegs, name=name)
        tegs = Tegs.objects.all()
        category = Catalog.objects.all()
        products = Product.objects.filter(tegs=c_с)
        order_by = request.GET.get('order_by')
        if order_by:
            products = products.order_by(order_by)
        paginator = Paginator(products, 9)
        page = request.GET.get('page')
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
        context = {'product': products, 'teg': tegs, 'c_с': c_с, 'category': category}
    context.update(base())
    return render(request, 'firstApp/catalog.html', context)


def contact(request):
    if request.method == 'POST':
        fead_back_form = FeedbackForm(request.POST)
        if fead_back_form.is_valid():
            asyncio.run(fead_back_form.send_message())
            return redirect('contact')
    else:
        fead_back_form = FeedbackForm()
    context = {'fead_back_form': fead_back_form}
    context.update(base())
    return render(request, 'firstApp/contact.html', context)


def productCart(request, id=None, name=None):
    try:
        product = get_object_or_404(Product, id=id, name=name)
        imgProductDesc = ProductImagesDescr.objects.all()
        comment = Comment.objects.filter(product=id).order_by("-published_date")
        profile = Profile.objects.get(user=request.user)
        is_favorite = FeaturedProducts.objects.filter(featuredProducts_User=profile,
                                                      featuredProducts_Product=product).exists()
        if request.method == 'POST':
            form_Favorite = FavoriteForm(request.POST)
            form_Comment = CommentForm(request.POST)
            if form_Comment.is_valid():
                comment = form_Comment.save(commit=False)
                comment.published_date = now()
                comment.product = product
                comment.user = request.user
                comment.save()
                return redirect('productCart', id=product.id, name=product.name)
            elif form_Favorite.is_valid():
                form_Favorite.instance.featuredProducts_User = profile
                form_Favorite.instance.featuredProducts_Product = product
                form_Favorite.save()
                return redirect('productCart', id=product.id, name=product.name)
        else:
            form_Comment = CommentForm()
            form_Favorite = FavoriteForm()
        context = {'product': product, 'form_Favorite': form_Favorite, 'is_favorite': is_favorite,
                   'imgProductDesc': imgProductDesc, 'comment': comment, 'form_Comment': form_Comment}
    except BaseException:
        product = get_object_or_404(Product, id=id, name=name)
        imgProductDesc = ProductImagesDescr.objects.all()
        comment = Comment.objects.filter(product=id).order_by("-published_date")
        context = {'product': product, 'imgProductDesc': imgProductDesc, 'comment': comment}
    context.update(base())
    return render(request, 'firstApp/product-cart.html', context)


# резервная копия кода карточки товара
# @login_required
# def productCart(request, id=None, name=None):
#     product = get_object_or_404(Product, id=id, name=name)
#     profile = Profile.objects.get(user=request.user)
#     imgProductDesc = ProductImagesDescr.objects.all()
#     comment = Comment.objects.filter(product=id).order_by("-published_date")
#     is_favorite = FeaturedProducts.objects.filter(featuredProducts_User=profile,
#                                                   featuredProducts_Product=product).exists()
#     if request.method == 'POST':
#         form_Favorite = FavoriteForm(request.POST)
#         form_Comment = CommentForm(request.POST)
#         if form_Comment.is_valid():
#             comment = form_Comment.save(commit=False)
#             comment.published_date = now()
#             comment.product = product
#             comment.user = request.user
#             comment.save()
#             return redirect('productCart', id=product.id, name=product.name)
#         elif form_Favorite.is_valid():
#             form_Favorite.instance.featuredProducts_User = profile
#             form_Favorite.instance.featuredProducts_Product = product
#             form_Favorite.save()
#             return redirect('productCart', id=product.id, name=product.name)
#     else:
#         form_Comment = CommentForm()
#         form_Favorite = FavoriteForm()
#     context = {'product': product, 'form_Favorite': form_Favorite, 'is_favorite': is_favorite, 'imgProductDesc': imgProductDesc, 'comment': comment, 'form_Comment': form_Comment}
#     context.update(base())
#     return render(request, 'firstApp/product-cart.html', context)


@login_required
def remove_favorite(request, id=None):
    product = get_object_or_404(Product, pk=id)
    profile = Profile.objects.get(user=request.user)
    featured_product = FeaturedProducts.objects.get(featuredProducts_User=profile, featuredProducts_Product=product)
    featured_product.delete()
    return redirect('productCart', id=product.id, name=product.name)


def registr(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            profile = Profile.objects.create(user=new_user, phone=form.cleaned_data['phone'])
            return redirect('login_User')
    else:
        form = RegisterForm()
    context = {'form': form}
    context.update(base())
    return render(request, 'firstApp/registr.html', context)


def profile(request):
    featuredProducts = FeaturedProducts.objects.all()
    user_Info = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        re_pass = Re_Password(request.POST)
        update_form = CombinedForm(request.POST, request.FILES, instance=request.user)
        if update_form.is_valid():
            update_form.save()
            return redirect('profile')
        elif re_pass.is_valid():
            update_pass_user = re_pass.save(user=request.user)
            update_session_auth_hash(request, update_pass_user)
            return redirect('profile')
    else:
        update_form = CombinedForm(instance=request.user)
        re_pass = Re_Password(request.POST)
    context = {'user_Info': user_Info, 'featuredProducts': featuredProducts, 'update_form': update_form,
               're_pass': re_pass}
    context.update(base())
    return render(request, 'firstApp/account.html', context)


def logoutView(request):
    logout(request)
    return redirect('index')


def login_User(request):
    context = {}
    context.update(base())
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'firstApp/login.html',
                          {'error_message': 'Неправильное имя пользователя или пароль.'})
    else:
        return render(request, 'firstApp/login.html', context)


def news(request):
    news = News.objects.all().order_by("-published_date")
    context = {"news": news}
    context.update(base())
    return render(request, 'firstApp/news.html', context)


def newsPost(request, id=None, title=None):
    newsPosts = get_object_or_404(News, id=id, title=title)
    context = {'newsPosts': newsPosts}
    context.update(base())
    return render(request, 'firstApp/newsPost.html', context)


# прочие представления
def company(request):
    context = {}
    context.update(base())
    return render(request, 'firstApp/company.html', context)


def services(request):
    context = {}
    context.update(base())
    return render(request, 'firstApp/services.html', context)


def serviceRepair(request):
    context = {}
    context.update(base())
    return render(request, 'firstApp/ServiceRepair.html', context)


def wholesale(request):
    context = {}
    context.update(base())
    return render(request, 'firstApp/wholesale.html', context)


def faq(request):
    context = {}
    context.update(base())
    return render(request, 'firstApp/faq.html', context)
# ===========================================================================