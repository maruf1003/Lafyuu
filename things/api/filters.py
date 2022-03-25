from things.models import UserCard


def get_queryset(self):
    return UserCard.objects.filter(user=self.request.user).all()