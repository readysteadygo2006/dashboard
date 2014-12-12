from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q


class Playbook(models.Model):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    def __str__(self):
        return "PB:{0}".format(self.name)

class Role(models.Model):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    def __str__(self):
        return "ROLE:{0}".format(self.name)

class Inventory(models.Model):
    name = models.CharField(max_length=300)

class Machine(models.Model):
    name = models.CharField(max_length=300)
    ip = models.CharField(max_length=300)
    member_of = models.ForeignKey(Inventory, related_name="has_member")
    def __str__(self):
        return "M:{0}".format(self.name)


class PlaybookStatus(models.Model):
    date = models.DateTimeField()
    logfile = models.CharField(max_length=300)
    playbook = models.CharField(max_length=300)
    machine = models.ForeignKey(Machine, related_name="playbook_history")
    execOptions = models.CharField(max_length=300)
    def __str__(self):
        return "{0} : {1}".format(self.playbook, self.date)

class RoleStatus(models.Model):
    date = models.DateTimeField()
    logfile = models.CharField(max_length=300)
    run_by = models.ForeignKey(Playbook, related_name="executes")
    machine = models.CharField(max_length=300)
    execOptions = models.CharField(max_length=300)
    def __str__(self):
        return "{0} : {1}".format(self.playbook, self.date)






