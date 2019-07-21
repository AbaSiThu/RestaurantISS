from django.db import models



class Category(models.Model):
    Catname = models.CharField(max_length=100)
    Catid = models.IntegerField(primary_key=True)

    def __str__(self):
        # return '{}/{}'.format(self.Cname,self.Cid)
        return self.Catname


class Restaurant(models.Model):
    Catid = models.ForeignKey(Category,db_column='Catid', on_delete=models.Aggregate)
    Resname = models.CharField(max_length=200)
    Resid = models.IntegerField(primary_key=True)
    Resadd=models.CharField(max_length=300)
    Resimage=models.CharField(max_length=300, null=True)
    Resdesc=models.CharField(max_length=300, null=True)

    def __str__(self):
     return '{}/{}/{}/{}/{}/{}'.format(self.Resid,self.Resname,self.Resadd,self.Catid,self.Resimage,self.Resdesc)
       # return self.Rid

class Review(models.Model):
    Revname = models.CharField(max_length=200)
    Revid = models.IntegerField(primary_key=True)
    Rating = models.IntegerField(default=0)
    Resid = models.ForeignKey(Restaurant,db_column='Resid',on_delete=models.Aggregate)

    def __str__(self):
        return '{}/{}/{}/{}'.format(self.Revid,self.Revname,self.Rating,self.Resid)

class Comment(models.Model):
    Comid = models.IntegerField(primary_key=True)
    Ce_text = models.CharField(max_length=200)
    Revid= models.ForeignKey(Review,db_column='Revid',on_delete=models.Aggregate)

    def __str__(self):
        return '{}/{}/{}'.format(self.Comid,self.Ce_text,self.Revid)

