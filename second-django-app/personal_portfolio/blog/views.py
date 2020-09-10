from django.shortcuts import render
from blog.models import Post, Comment
from blog.forms import CommentForm
# Create your views here.

def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')  # obtain a query set containing all the posts in the database.
                                                        # # order the query set through argument 
                                                        # -created_on where minus(-) sign tells django to 
                                                        # start with the largest value rather than the smallest
        
    context = {                                         
        'posts': posts,
    }
    return render(request, "blog_index.html", context)


# Now for blog_category view function.
def blog_category(request, category):
    posts = Post.objects.filter(                    # django query set filter
        categories__name__contains=category         # conditions to be met for an object to be retrieved.
    ).order_by('-created_on')                       # order by latest.

    context = {
        'category': category,
        'posts': posts,
    }
    return render(request, "blog_category.html", context)


# now blog_detail view function.
def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)                  # get post based on primary key (pk)

    # @6.4
    form = CommentForm()                    # create instance of our form class.
    if request.method == 'POST':            # has a POST request been received?
        form = CommentForm(request.POST)    # If yes, create a new instance of our form with the request populated with the data.
        if form.is_valid():                 # Check to see if form is valid.
            comment = Comment(              # Create new instance of comment.
                author=form.cleaned_data['author'],   # form.cleaned_data represents a dictionary, with keys such as author, body etc.
                body=form.cleaned_data['body'],
                post=post                 # don't forget to add current post to the comment.
            )
            comment.save()                  # save the comment.
            
    comments = Comment.objects.filter(post=post)    # retrieve comments for the specific post using filter
    context = {
        'post': post,
        'comments': comments,
        'form': form,           # add form to context dictionary so we can access the form in HTML template.
    }

    return render(request, "blog_detail.html", context)