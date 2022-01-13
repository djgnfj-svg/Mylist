from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.utils.translation import ugettext_lazy as _
from django.db import models
# Create your models here.

# class UserManager(BaseUserManager):
# 	def create_user(self, email, nickname, password=None):
# 		if not email:
# 			raise ValueError(_("Users must have an email address"))

# 		user = self.model(
# 			email=self.normalize_email(email),
# 			nickname = nickname,
# 		)

# 		user.set_password(password)
# 		user.save(using=self._db)
# 		return user
	
# 	def create_superuser(self, email, password):        
	
# 		user = self.create_user(            
# 			email = self.normalize_email(email),
# 			password=password        
# 		)
# 		user.is_admin = True
# 		user.is_superuser = True
# 		user.save(using=self._db)
# 		return user

# class User(AbstractBaseUser, PermissionsMixin):    
	
# 	objects = UserManager()
	
# 	email = models.EmailField(        
# 		max_length=255,        
# 		unique=True,    
# 	)
# 	organization = models.CharField(max_length=30)
# 	is_active = models.BooleanField(default=True)
# 	is_admin = models.BooleanField(default=False)

# 	USERNAME_FIELD = 'email'    
# 	REQUIRED_FIELDS = []

# 	def __str__(self):
# 		return self.email

# 	@property
# 	def is_staff(self):
# 		return self.is_admin