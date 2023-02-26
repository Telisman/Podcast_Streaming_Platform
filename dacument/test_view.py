# one_year_ago = date.today() - timedelta(days=365)
# username = request.GET.get('username', None)
# sort_by_likes = request.GET.get('sort_by_likes', None)
#
# if username:
#     blog_posts = Podcast_Blog.objects.filter(blog_user__username=username, time_of_blog__gte=one_year_ago).order_by(
#         '-time_of_blog')
# else:
#     blog_posts = Podcast_Blog.objects.filter(time_of_blog__gte=one_year_ago).order_by('-time_of_blog')
# if sort_by_likes:
#     blog_posts = blog_posts.annotate(num_likes=Count('likes')).order_by('-num_likes')
# else:
#     blog_posts = blog_posts.order_by('-time_of_blog')
# blog_comments = []
# for blog in blog_posts:
#     comments = BlogComment.objects.filter(blog=blog).order_by('-time_of_comment')
#     blog_comments.append((blog, comments))
# return render(request, "pages/blog/blog_timeline.html", {'blog_comments': blog_comments})