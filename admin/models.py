from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.hashers import make_password, check_password

USER_ROLE = (
    (1, 'ADMIN'),
    (2, 'EXPERT')
)

class UserAdmin(User):
    username = models.CharField(max_length=80, unique=True)
    password = models.CharField(max_length=20)
    role = models.PositiveIntegerField(choices=USER_ROLE, default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        user = User.objects.filter(id=self.id).first()
        if not user:
            self.password = make_password(self.password)
            super().save(*args, **kwargs)
            return self

        if not check_password(self.password, user.password):
            self.password = make_password(self.password)

        super().save(*args, **kwargs)
        return self






