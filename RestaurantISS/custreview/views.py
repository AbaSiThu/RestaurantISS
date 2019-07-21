from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Restaurant, Review, Comment

def index(request):
    context = {}

    category=Category.objects.all()
    restaurant=Restaurant.objects.all()

    category_dict = dict()

    for dd in category:
        category_dict[dd.Catid] = dd.Catname



    

    context={
        'category':category,
        'restaurant':restaurant
    }

    return render(request, 'home.html',context)




def category(request, restaurant_id):
    print(restaurant_id)

    restaurant = Restaurant.objects.all().filter(Catid=restaurant_id)
    print(restaurant)

   

    

    category=Category.objects.all()
    context={
        'category':category,
        'restaurant':restaurant
    }
    return render(request, 'home.html', context)


def detail(request, restaurant_id):
    restaurant = Restaurant.objects.all().filter(Resid=restaurant_id)
    review=Review.objects.all().filter(Resid=restaurant_id)
    
    
    
    x=0
    count=0
    countfor1=0
    countfor2=0
    countfor3=0
    countfor4=0
    countfor5=0
    for val in review:
        if val.Rating==1:
            countfor1+=1
        elif val.Rating==2:
            countfor2+=1
        elif val.Rating==3:
            countfor3+=1
        elif val.Rating==4:
            countfor4+=1
        else:
            countfor5+=1
        x+=val.Rating
        count+=1
    

    print("count")

    print(countfor1)
    print(countfor2)
    print(countfor3)

    print(countfor4)
    print(countfor5)
    
    print("total")

    print(x)
    print(count)

    avg=x/count

    answer = str(round(avg, 2))
    print(avg)

    context={
        'restaurant':restaurant,
        'review':review,
        'avg':answer,
        'count':count,
        'countfor1':countfor1,
        'countfor2':countfor2,
        'countfor3':countfor3,
        'countfor4':countfor4,
        'countfor5':countfor5
    }
    return render(request, 'detail.html', context)

def vote(request, restaurant_id):
    print(restaurant_id)
    print(request.POST['rating'])
    restaurant = Restaurant.objects.get(Resid=restaurant_id)
    review=Review.objects.all().last()
    reid=review.Revid+1
    review = Review.objects.create(Revname=request.POST['ratingname'],Revid=reid,Rating=request.POST['rating'],Resid=restaurant)
    restaurant = Restaurant.objects.all().filter(Resid=restaurant_id)
    review=Review.objects.all().filter(Resid=restaurant_id)
    x=0
    count=0
    countfor1=0
    countfor2=0
    countfor3=0
    countfor4=0
    countfor5=0
    for val in review:
        if val.Rating==1:
            countfor1+=1
        elif val.Rating==2:
            countfor2+=1
        elif val.Rating==3:
            countfor3+=1
        elif val.Rating==4:
            countfor4+=1
        else:
            countfor5+=1
        x+=val.Rating
        count+=1
    

    print("count")

    print(countfor1)
    print(countfor2)
    print(countfor3)

    print(countfor4)
    print(countfor5)
    
    print("total")

    print(x)
    print(count)

    avg=x/count

    print(avg)
    answer = str(round(avg, 2))
    context={
        'restaurant':restaurant,
        'review':review,
        'avg':answer,
        'count':count,
        'countfor1':countfor1,
        'countfor2':countfor2,
        'countfor3':countfor3,
        'countfor4':countfor4,
        'countfor5':countfor5
    }
    return render(request, 'detail.html', context)

def reply(request, review_id):
    review = Review.objects.all().filter(Revid=review_id)
    comment= Comment.objects.all().filter(Revid=review_id)
    review1 = Review.objects.get(Revid=review_id)
    restaurant = Restaurant.objects.filter(review=review1)

    
    context={
        'restaurant':restaurant,
        'review':review,
        'comment':comment
    }
   
    return render(request, 'reply.html',context)

def commentData(request, review_id):
    print(review_id)
    print(request.POST['commentname'])
    review = Review.objects.get(Revid=review_id)
    comment=Comment.objects.all().last()
    coid=comment.Comid+1
    comment = Comment.objects.create(Ce_text=request.POST['commentname'],Comid=coid,Revid=review)
    
    review = Review.objects.all().filter(Revid=review_id)
    comment= Comment.objects.all().filter(Revid=review_id)
    review1 = Review.objects.get(Revid=review_id)
    restaurant = Restaurant.objects.filter(review=review1)

    
    context={
        'restaurant':restaurant,
        'review':review,
        'comment':comment
    }
   
    return render(request, 'reply.html',context)
    




