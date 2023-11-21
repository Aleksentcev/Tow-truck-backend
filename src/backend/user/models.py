from typing import Any

from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from phonenumber_field import modelfields
# from django.contrib.auth.models import AbstractUser
# from django.db import models

from core.choices import Roles
from user.utils import get_avatar_path


class MyUserManager(BaseUserManager):
    """
    Кастомный менеджер для модели User
    """

    def _create_user(
        self,
        email: str,
        password: str,
        **extra_fields: Any
    ) -> AbstractBaseUser:
        """
        Создает и сохраняет юзера с почтой, телефоном, и паролем
        """
        if not email:
            raise ValueError('Электронная почта обязательна')
        email = self.normalize_email(email).lower()
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(
        self,
        email: str,
        password: str,
        **extra_fields: Any
    ) -> AbstractBaseUser:
        """
        Создает юзера
        """
        # extra_fields.setdefault('is_staff', False)
        # extra_fields.setdefault('is_superuser', False)
        return self._create_user(
            email,
            password,
            **extra_fields
        )

    def create_superuser(
        self,
        email: str,
        password: str,
        **extra_fields: Any
    ) -> AbstractBaseUser:
        """
        Создает суперюзера
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(
            email,
            password,
            **extra_fields
        )


class User(AbstractBaseUser):
    """
    Кастомная модель пользователя.
    """
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', 'phone',)

    # username = models.CharField(
    #     verbose_name='Имя пользователя',
    #     max_length=150,
    #     unique=True,
    # )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=150,
        blank=True,
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=150,
        blank=True,
    )
    phone = modelfields.PhoneNumberField(
        'Телефон',
        region='RU',
        unique=True,
        blank=True,
        null=True,
    )
    email = models.EmailField(
        'Электронная почта',
        unique=True,
        error_messages={
            'unique': 'Этот адрес электронной почты уже зарегистрован.'
        }
    )
    is_verified = models.BooleanField(
        "Подтверждение",
        default=False
    )
    role = models.CharField(
        verbose_name='Роль',
        help_text='Роль пользователя с правами доступа',
        max_length=30,
        choices=Roles.choices,
        default=Roles.USER
    )

    objects = MyUserManager()

    class Meta:
        ordering = ("email", "phone",)
        unique_together = ("email", "phone",)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        return self.email

    @property
    def is_admin(self):
        return self.role == Roles.ADMIN or self.is_superuser

    def clean(self) -> None:
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)


class Avatar(models.Model):
    user = models.OneToOneField(
        User,
        related_name='avatar',
        on_delete=models.CASCADE,
    )
    image = models.ImageField(
        'Аватар',
        blank=True,
        null=True,
        upload_to=get_avatar_path,
    )

    class Meta:
        verbose_name = 'Аватар'
        verbose_name_plural = 'Аватарки'
        ordering = ('user',)

    def __str__(self) -> str:
        return self.user.first_name
