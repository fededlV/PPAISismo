from django.db import models

# Create your models here.

# Create a class for likes 
class Likes(models.Model):
    # Create a foreign key to the user model
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # Create a foreign key to the post model
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    # Create a date field for the date of the like
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} liked {self.post.title}"
