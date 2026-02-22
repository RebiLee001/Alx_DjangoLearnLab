from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import CustomUser
from .models import Post
from .serializers import PostSerializer

class FollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser, id=user_id)

        if user_to_follow == request.user:
            return Response(
                {"error": "You cannot follow yourself"},
                status=status.HTTP_400_BAD_REQUEST
            )

        request.user.following.add(user_to_follow)

        return Response(
            {"message": f"You are now following {user_to_follow.username}"},
            status=status.HTTP_200_OK
        )


class UnfollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser, id=user_id)

        request.user.following.remove(user_to_unfollow)

        return Response(
            {"message": f"You unfollowed {user_to_unfollow.username}"},
            status=status.HTTP_200_OK
        )
    
    Checks for “Create a view in the posts app that generates a feed based on the posts from users that the current user follows. This view should return posts ordered by creation date, showing the most recent posts at the top.” task

posts/views.py doesn't contain: ["Post.objects.filter(author__in=following_users).order_by", "following.all()"]