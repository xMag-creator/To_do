from django.db import models


class Items(models.Model):
    """
    Class representing the structure of tasks to be performed.

    
    Fields: 
        name (CharField): Item name.
        finished (BooleanField): Information about completing the item.
        parent_item (ForeignKey): Parent item pk.
    """
    name = models.CharField(max_length=256)
    finished = models.BooleanField(default=False)
    parent_item = models.ForeignKey('self',
                                    on_delete=models.CASCADE,
                                    null=True,
                                    blank=True,
                                    related_name='children')
