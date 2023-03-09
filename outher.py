#User  detail view first exsemple!!!


# @login_required
# def user_detail(request, user_id):
#     user = get_object_or_404(PodcastUser, user_id=self.kwargs['pk'])
#     try:
#         user_info = UserInfo.objects.get(user=user)
#     except UserInfo.DoesNotExist:
#         user_info = ''
#     blogs = Podcast_Blog.objects.filter(blog_user=user).order_by('-time_of_blog')
#     blog_comments = []
#     for blog in blogs:
#         comments = BlogComment.objects.filter(blog=blog).order_by('-time_of_comment')
#         blog_comments.append((blog, comments))
#
#     followers_count = user.followers.count()
#     following_count = user.following.count()
#     context = {
#         'user': user,
#         'followers_count': followers_count,
#         'following_count': following_count,
#         'user_info': user_info,
#         'blog_comments': blog_comments,
#     }
#     return render(request, 'pages/users//user_detail.html', context)





