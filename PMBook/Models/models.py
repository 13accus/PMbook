from django.db import models
from datetime import datetime

# Create your models here

#List of capabilities
#This class is meant for the project class. But, I just added these fields directly to the Project class
class Capability(models.Model):
    #Number associated with capability category
    num = models.IntegerField(default=1)
    #String name of the capabilities (Ex. 1.2 Deliver measurable "high touch" engagements)
    capability = models.CharField(max_length=200)
    def __unicode__(self):
        return self.capability

#List of divisions
class Division(models.Model):
    division = models.CharField(max_length=200)
    def __unicode__(self):
        return self.division

#Table that keeps track of active projects and project scores. 
class History(models.Model):
    score = models.DecimalField(max_digits=6, decimal_places=3)
    active = models.IntegerField()
    timestamp = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.timestamp

#Used as a list of severity levels (Ex. Green, Yellow, Red)
class Health(models.Model):
    health = models.CharField(max_length=200)
    def __unicode__(self):
        return self.health

#List of initiatives 
class Initiative(models.Model):
    initiative = models.CharField(max_length=200)
    def __unicode__(self):
        return self.initiative

#List of levels (Ex. High, Medium , Low)
class Level(models.Model):
    level = models.CharField(max_length=100)
    def __unicode__(self):
        return self.level

#List of Methodologies (Ex. Agile, Waterfall)
class Methodology(models.Model):
    methodology = models.CharField(max_length=20)
    def __unicode__(self):
        return self.methodology

#List of Offices 
class Office(models.Model):
    office = models.CharField(max_length=100)
    def __unicode__(self):
        return self.office

#List of R&I Categories (Ex. Scheduling, Resources)
class RI_Category(models.Model):
    ri_category = models.CharField(max_length=100)
    def __unicode__(self):
        return self.ri_category

#List of Roles (Ex. Business Analyst)
class Role(models.Model):
    role = models.CharField(max_length=100)
    def __unicode__(self):
        return self.role

#List of Milestone types
#
#Used for creating the list of important milestones which are list on the left column of the
#profile page under schedule.
class Schedule(models.Model):
    milestone_type = models.CharField(max_length=100)
    def __unicode__(self):
        return self.milestone_type

#List of Status types (Ex. Active - Green)
class Status(models.Model):
    status = models.CharField(max_length=100)
    def __unicode__(self):
        return self.status


#List of Projects
class Project(models.Model):
    # In future versions, the needyn fields should be updated to have a field for Yes/No
    # responses. As well as, a text field for further detail.

    timestamp = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    # email associated with the person who filled out the intake form
    email = models.CharField(max_length=100)
    division = models.ForeignKey(Division)
    office = models.ForeignKey(Office)
    sponsor = models.CharField(max_length=100)
    # Point of Contact
    poc = models.CharField(max_length=100)
    description = models.CharField(max_length=10000)
    method = models.ForeignKey(Methodology, default=1)
    # Target Start Date
    date = models.DateField(default=datetime.now)
    launchdate = models.DateField(default=datetime.now)
    staff = models.CharField(max_length=10000, default='')
    # Values from answers from intake2.html
    v1 = models.CharField(max_length=10000, default='')
    v2 = models.CharField(max_length=10000, default='')
    v3 = models.CharField(max_length=10000, default='')
    v4 = models.CharField(max_length=10000, default='')
    v5 = models.CharField(max_length=10000, default='')
    comment = models.CharField(max_length=10000, default='')
    # Values from answers from intake3.html
    needyn1 = models.CharField(max_length=10000, default='')
    needyn2 = models.CharField(max_length=10000, default='')
    needyn3 = models.CharField(max_length=10000, default='')
    needyn4 = models.CharField(max_length=10000, default='')
    needyn5 = models.CharField(max_length=10000, default='')
    needyn6 = models.CharField(max_length=10000, default='')
    valueyn1 = models.CharField(max_length=10000, default='')
    valueyn2 = models.CharField(max_length=10000, default='')
    valueyn3 = models.CharField(max_length=10000, default='')
    valueyn4 = models.CharField(max_length=10000, default='')
    valueyn5 = models.CharField(max_length=10000, default='')
    valueyn6 = models.CharField(max_length=10000, default='')
    # These questions may have a categorical response.
    techrisk1 = models.CharField(max_length=10000, default='')
    techrisk2 = models.CharField(max_length=10000, default='')
    techrisk3 = models.CharField(max_length=10000, default='')
    techrisk4 = models.CharField(max_length=10000, default='')
    techrisk5 = models.CharField(max_length=10000, default='')
    techrisk6 = models.CharField(max_length=10000, default='')
    techrisk7 = models.CharField(max_length=10000, default='')
    # capnum = the Capability category number. Used for categorizing projects for one of the reports in projhealthdash.html 
    capnum = models.IntegerField(default=1)
    # cap = string value of Capability (Ex. 1.2 Deliver measurable "high touch" engagements)
    cap = models.CharField(max_length=1000)
    # status of the project (Ex. "Active - Green")
    status = models.ForeignKey(Status, default=1)
    # Most likely a email or phone number. Currrently, there isn't an input field in the html files which would allow for this
    # field to be populated
    poc_contact_info = models.CharField(max_length=100)
    project_id = models.IntegerField()
    def __unicode__(self):
        return self.name

#List of Issues
class Issue(models.Model):
    # Future versions might want to add a target close date
    timestamp = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100, default='No Title')
    severity = models.ForeignKey(Health)
    comment = models.CharField(max_length=10000)
    resolved = models.BooleanField(default=True)
    project_id = models.IntegerField()
    category = models.ForeignKey(RI_Category, default='')
    open_date = models.DateField(default=datetime.now)
    close_date = models.DateField(default=datetime.now)
    next_step = models.CharField(max_length=10000, default= '')
    assign_to = models.CharField(max_length=1000, default='')
    external_dependencies = models.CharField(max_length=10000, default='')
    issue_id = models.IntegerField(default=0)
    # This table will hold the previous version of an issue. The tool only displays the newest verision.
    # I used the newest field to keep track of the lastest modified issue. However, you can probably just
    # use the timestamp.
    newest = models.BooleanField(default=True)
    def __unicode__(self):
        return self.title

#List of Milestones
class Milestone(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100, default='')
    comment = models.CharField(max_length=10000)
    project_id = models.IntegerField()
    mile_type = models.CharField(max_length=100, default='')
    status = models.ForeignKey(Status)
    baseline_date = models.DateField()
    target_date = models.DateField()
    milestone_id = models.IntegerField()
    # This table will hold the previous version of a milestone. The tool only displays the newest verision.
    # I used the newest field to keep track of the lastest modified issue. However, you can probably just
    # use the timestamp.
    newest = models.BooleanField(default=True)
    def __unicode__(self):
        return self.title

#List of Notes
class Note(models.Model):

    timestamp = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100, default='')
    date = models.DateField(default= datetime.now)
    comment = models.CharField(max_length=10000)
    project_id = models.IntegerField()
    note_id = models.IntegerField()
    # This table will hold the previous version of an issue. The tool only displays the newest verision.
    # I used the newest field to keep track of the lastest modified issue. However, you can probably just
    # use the timestamp.
    newest = models.BooleanField(default=True)
    def __unicode__(self):
        return self.title

#List of People and which projects they are working on
class Personnel(models.Model):
    name = models.CharField(max_length=100)
    #There role in a specific project
    role = models.ForeignKey(Role, default='')
    #The project the person is associated with
    project_id = models.IntegerField()
    #Boolean for determining whether the person is still active on the project
    active = models.BooleanField(default=True)
    def __unicode__(self):
        return self.name

#List of Risk
class Risk(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100, default='')
    severity = models.ForeignKey(Health)
    comment = models.CharField(max_length=10000)
    resolved = models.BooleanField(default=True)
    probability = models.ForeignKey(Level)
    project_id = models.IntegerField()
    category = models.ForeignKey(RI_Category)
    open_date = models.DateField(default=datetime.now)
    close_date = models.DateField()
    next_step = models.CharField(max_length=10000)
    assigned_to = models.CharField(max_length=100)
    external_dependencies = models.CharField(max_length=1000)
    risk_id = models.IntegerField()
    # This table will hold the previous version of a milestone. The tool only displays the newest verision.
    # I used the newest field to keep track of the lastest modified issue. However, you can probably just
    # use the timestamp.
    newest = models.BooleanField(default=True)
    def __unicode__(self):
        return self.title

#List of Risk and Issues from all projects
#Current version does not use this class. It was meant to be used for the R&I deck in progreport.html
class RIdeck(models.Model):
    cap = models.IntegerField()
    proj_id = models.IntegerField()
    proj_name = models.CharField(max_length=100)
    bus_own = models.CharField(max_length=100)
    tar_date = models.DateField()
    status1 = models.CharField(max_length=100)
    status2 = models.CharField(max_length=100)
    status3 = models.CharField(max_length=100)
    close_date = models.DateField()
    key_dependencies = models.CharField(max_length=10000)
    timestamp = models.DateTimeField(auto_now=True)
