from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class Library(models.Model):
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=255, validators=[MinLengthValidator(5)])
    telephone = models.CharField(max_length=10, validators=[MinLengthValidator(10)])
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    name = models.CharField(max_length=100, unique=True)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    language = models.CharField(max_length=30)
    items_available = models.IntegerField(default=0)
    library = models.ForeignKey(Library, on_delete=models.PROTECT, related_name='books')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class MemberManager(BaseUserManager):
    def create_user(self, username, email, first_name, last_name, library, password=None, **extra_fields):
        if not username:
            raise ValueError('El nombre de usuario es obligatorio')
        if not email:
            raise ValueError('El email es obligatorio')

        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            library=library,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, first_name, last_name, library, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(username, email, first_name, last_name, library, password, **extra_fields)

class Member(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True, validators=[
        RegexValidator(
            regex=r'^\S+$',
            message='El nombre de usuario no puede contener espacios.'
        )
    ])
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, validators=[MinLengthValidator(4)])
    last_name = models.CharField(max_length=30, validators=[MinLengthValidator(4)])
    library = models.ForeignKey(Library, on_delete=models.PROTECT, related_name='member')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'library']

    objects = MemberManager()

    def __str__(self):
        return self.username
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
class Management(models.Model):
    member = models.ForeignKey(Member, on_delete=models.PROTECT, related_name='manage_members')
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='manage_books')
    assigned_at = models.DateTimeField(auto_now_add=True)
    returned_at = models.DateTimeField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.member.username} - {self.book.name}"
