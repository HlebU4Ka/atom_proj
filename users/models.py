from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Create your models here.

class CustomUserManager(BaseUserManager):
    """
    Кастомный менеджер пользователей.

    Позволяет создавать пользователей и суперпользователей.
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Создает и сохраняет пользователя с указанным адресом электронной почты и паролем.

        Параметры:
        - email: Адрес электронной почты пользователя.
        - password: Пароль пользователя (по умолчанию None).
        - **extra_fields: Дополнительные поля пользователя.

        Возвращает:
        - Пользователь.
        """
        if not email:
            raise ValueError('Поле Email должно быть заполнено')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Создает и сохраняет суперпользователя с указанным адресом электронной почты и паролем.

        Параметры:
        - email: Адрес электронной почты суперпользователя.
        - password: Пароль суперпользователя (по умолчанию None).
        - **extra_fields: Дополнительные поля суперпользователя.

        Возвращает:
        - Суперпользователь.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Суперпользователь должен иметь is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Суперпользователь должен иметь is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Кастомная модель пользователя.

    Поля:
    - email: Адрес электронной почты пользователя (уникальный).
    - name: Имя пользователя.
    - is_active: Флаг, указывающий на активность пользователя (по умолчанию True).
    - is_staff: Флаг, указывающий на доступ к административной панели (по умолчанию False).

    """
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    chat_id = models.CharField(max_length=255, blank=True, null=True)  # Поле для хранения chat_id телеграма
    telegram_username = models.CharField(max_length=255, blank=True,
                                         null=True)  # Поле для хранения имени пользователя в телеграме
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email