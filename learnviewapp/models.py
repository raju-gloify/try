from django.db import models

# Create your models here.
class PostMedia(models.Model):
    AccountType=(
                ('facebook','Facebook'),
                ('instagram','Instagram'),
                ('twitter','Twitter'),
    )
    PostType=(
        ('staticpost','StaticPost'),
        ('videpost','VideoPost'),
        ('staticstory','StaticStory'),
        ('videostory','VideoStory'),
        ('reels','Reels'),
        ('carouselpost','CarouselPost'),

    )
    amount=models.IntegerField(blank=True,null=True)
    account_type=models.CharField(max_length=15,choices=AccountType)
    post_type=models.CharField(max_length=15,choices=PostType)
    

    def __str__(self):
        return f"POST TYPE {self.post_type} -ACCOUNT TYPE {self.account_type} "
