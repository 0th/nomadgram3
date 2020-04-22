from django.db import models
from nomadgram.users import models as user_model





class TiemStampedModel(models.Model):

        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
        
        class Meta:
            abstract = True

class Image(TiemStampedModel):
    
    """ Image Model """
    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()
    creator = models.ForeignKey(user_model.User,on_delete=models.CASCADE)

class Comment(TiemStampedModel):
    """ Comment Model """
    message = models.TextField()
    creator = models.ForeignKey(user_model.User,on_delete=models.CASCADE)
    image = models.ForeignKey(Image,on_delete=models.CASCADE)

class Like(TiemStampedModel):
    
    """ Like Model """
    creator = models.ForeignKey(user_model.User,on_delete=models.CASCADE)
    image = models.ForeignKey(Image,on_delete=models.CASCADE)
    



