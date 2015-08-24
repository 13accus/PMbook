from django.shortcuts import render_to_response, render
from django.template import RequestContext, Context
from django.http import HttpResponse
from Models.models import Capability, History, Issue, Milestone, Note, Project, Risk, Personnel, RI_Category, Status, Health, Level, Division, Methodology, Office, Status
from django.utils import timezone
import datetime
# Create your views here.

#For the project page.
def projects(request, project):
    
    #If a new issue has been added, it refreshes the page. In doing so, it adds
    #a new issue. 
    if request.POST.get("type", "")  == "issue":
        Title = request.POST.get("title", "")
        Category = request.POST.get("category", "")
        Severity = request.POST.get("severity", "")
        Comment = request.POST.get("comment", "")
        Open_date = request.POST.get("opendate", "")
        Assigned_to = request.POST.get("assignedto", "")
        Next_step = request.POST.get("next_step", "")
        External_dependencies = request.POST.get("externdepend", "")
        Project_id  = request.POST.get("project_id", "")
        IID = request.POST.get("num", "")
        
        new_issue = Issue(title=Title, category=RI_Category.objects.get(ri_category=Category), 
                        severity=Health.objects.get(health=Severity), comment=Comment,
                        project_id=Project_id, open_date=Open_date, close_date="9999-12-12", 
                        assign_to=Assigned_to, next_step=Next_step, 
                        external_dependencies=External_dependencies, issue_id=IID, newest=True)
        new_issue.save()

    #If a new milestone has been added, it refreshes the page. In doing so,
    #it adds a new milestone. 
    if request.POST.get("type", "")  == "milestone": 
        Title = request.POST.get("title", "")
        Comment = request.POST.get("description", "")
        Project_id  = request.POST.get("project_id", "")
        STATUS = request.POST.get("severity", "")
        Baseline_date = request.POST.get("basedate", "")
        Target_date = request.POST.get("targetdate", "")
        Mile_type = request.POST.get("miletype", "")
        ID = request.POST.get("num", "")
        
    #create new milestone                                                                                                                                                                                    
        new_milestone = Milestone(title=Title, comment=Comment, project_id=Project_id,
                                 status = Status.objects.get(status=STATUS),baseline_date=Baseline_date, 
                                 target_date=Target_date,  mile_type=Mile_type, milestone_id=ID, newest=True)
        new_milestone.save()


    #If a new note has been added, it refreshes the page. In doing so, it adds
    #a new note.     
    if request.POST.get("type", "")  == "note":                                                                                                                                                              
        Title = request.POST.get("title", "")
        Comment = request.POST.get("text", "")
        Project_id  = request.POST.get("project_id", "")
        Date = request.POST.get("date", "")
        ID = request.POST.get("num", "")

    #create new note                                                                                                                                                                                                      
        new_note = Note(title=Title, comment=Comment, project_id=Project_id, date=Date, note_id=ID, newest=True)
        new_note.save()


    #If a new risk has been added, it refreshes the page. In doing so, it adds
    #a new risk. 
    if request.POST.get("type", "")  == "risk":                                                                                                                                                             
        Title = request.POST.get("title", "")
        Category = request.POST.get("category", "")
        Severity = request.POST.get("severity", "")
        Probability = request.POST.get("probability", "")
        Comment = request.POST.get("comment", "")
        Open_date = request.POST.get("opendate", "")
        Assigned_to = request.POST.get("assignedto", "")
        Next_step = request.POST.get("next_step", "")
        External_dependencies = request.POST.get("externdepend", "")
        Project_id  = request.POST.get("project_id", "")
        RID = request.POST.get("num", "")

        new_risk = Risk(title=Title, category=RI_Category.objects.get(ri_category=Category), 
                        probability=Level.objects.get(level=Probability), severity=Health.objects.get(health=Severity), 
                        comment=Comment, project_id=Project_id, open_date=Open_date, close_date="9999-12-12", 
                        assigned_to=Assigned_to, next_step=Next_step, external_dependencies=External_dependencies, risk_id=RID, newest=True)
        new_risk.save()
        

    project_id = Project.objects.filter(project_id=project).latest('timestamp').pk
    p = Project.objects.get(pk=project_id)
    
    #Get issue objects and orders them by date
    issues = Issue.objects.filter(project_id=project).filter(newest=True).order_by('-timestamp')
    issues_recent = issues.filter(timestamp__gt= timezone.now() - datetime.timedelta(days=1))
    
    #Get milestone objects and orders them by date
    milestone = Milestone.objects.filter(project_id=project).filter(newest=True).order_by('-timestamp')
    milestone_recent = milestone.filter(timestamp__gt= timezone.now() - datetime.timedelta(days=1))

    #Get note objects and orders them by date
    note = Note.objects.filter(project_id=project).filter(newest=True).order_by('-timestamp')
    note_recent = note.filter(timestamp__gt= timezone.now() - datetime.timedelta(days=1))

    #Get risk objects and orders them by date
    risk = Risk.objects.filter(project_id=project).filter(newest=True).order_by('-timestamp')
    risk_recent = risk.filter(timestamp__gt= timezone.now() - datetime.timedelta(days=1))

    #Get role objects
    personnel = Personnel.objects.filter(project_id=project).filter(active=True)


    #Get number of items
    issue_num = issues.count()
    milestone_num = milestone.count()
    note_num = note.count()
    risk_num = risk.count()

    #Change status of project if the status is changed from the profile page
    if request.POST.get("status", "") != "":
        status = request.POST.get("status", "")
        p.status = Status.objects.get(status=status)
        p.save()

    gstatus = Status.objects.get(status="Active - Green")
    ystatus = Status.objects.get(status="Active - Yellow")
    rstatus = Status.objects.get(status="Active - Red")
    
    #Gets list of Gate Review dates and similar milestones
    mile_type = Milestone.objects.filter(project_id=p.project_id).exclude(mile_type="Other")
    
    # List of all ri_categories
    category = RI_Category.objects.all()
    
    #  compliance = category.get(ri_category="compliance")
    context_instance=RequestContext(request,
                      {'issues' : issues,
                       'p' : p,
                       'milestone' : milestone,
                       'note' : note,
                       'risk' : risk,
                       'personnel' : personnel,
                       'issues_recent' : issues_recent,
                       'milestone_recent' : milestone_recent,
                       'note_recent' : note_recent,
                       'risk_recent' : risk_recent,
                       'milestone_num' : milestone_num,
                       'note_num' : note_num,
                       'risk_num' : risk_num,
                       'issue_num' : issue_num,
                       'gstatus' : gstatus,
                       'ystatus' : ystatus,
                       'rstatus' : rstatus,
                       'mile_type' : mile_type,
                       'compliance' : category.get(ri_category="Compliance"), 
                       'cost' : category.get(ri_category="Cost"),
                       'dependency' : category.get(ri_category="Dependency"),
                       'info_assurance' :category.get(ri_category="Info Assurance"),
                       'organizational' :category.get(ri_category="Organizational"),
                       'privacy' :category.get(ri_category="Privacy"),
                       'resources' :category.get(ri_category="Resources"),
                       'schedule' :category.get(ri_category="Schedule"),
                       'security' : category.get(ri_category="Security"),
                       'strategic' :category.get(ri_category="Strategic"),
                       'scope' :category.get(ri_category="Scope"),
                       'technical' :category.get(ri_category="Technical"),
                       
                       })

    return render_to_response('Models/profile.html', context_instance)






def index(request):
    return render_to_response('Models/index.html', context_instance=RequestContext(request))






#For milestone table
def milestone(request, project):
    
    #if a milestoned is edited or created
    if request.method == 'POST':

        milestone_id = Milestone.objects.filter(project_id=project).filter(milestone_id=request.POST.get("milestone_id", ""))
        if milestone_id.count() > 0:
            m = milestone_id.get(newest=True)
            m.newest = False
            m.save()
        

        Title = request.POST.get("title", "")
        Comment = request.POST.get("comment", "")
        Project_id  = request.POST.get("project_id", "")
        STATUS = request.POST.get("status", "")
        Baseline_date = request.POST.get("baseline_date", "")
        Target_date = request.POST.get("target_date", "")
        ID = request.POST.get("milestone_id", "")

    #create new milestone                                                                                     
        new_milestone = Milestone(title=Title, comment=Comment, project_id=Project_id,
                                  baseline_date=Baseline_date, target_date=Target_date, milestone_id=ID, status =Status.objects.get(status=STATUS), newest=True)
        new_milestone.save()



    project_id = Project.objects.filter(project_id=project).latest('timestamp').pk
    milestone = Milestone.objects.filter(project_id=project).filter(newest=True)
    milestone_num = milestone.count()
    p = Project.objects.get(pk=project_id)
    
    
    context_instance=RequestContext(request,{
            'p' : p,
            'milestone' : milestone,
            'num' : milestone_num,
        })

    return render_to_response('Models/miletable.html', context_instance)
    #return render(request, 'Models/miletable.html', context)








#For gatedoc. CURRENTLY NOT IN USE
def gatedoc(request, project):
    project_id = Project.objects.filter(project_id=project).latest('timestamp').pk
    p = Project.objects.get(pk=project_id)

    context_instance=RequestContext(request,{
            'p' : p,
            })

    return render_to_response('Models/gatedoc.html', context_instance)





#For risk & issues table
def ri(request, project):

    #creates/edit a risk or issue
    if request.method == 'POST':

        if request.POST.get("risk_or_issue", "")  == "risk":
            Risk_id = Risk.objects.filter(project_id=project).filter(risk_id=request.POST.get("id", ""))
            if Risk_id.count() > 0:
                r = Risk_id.get(newest=True)
                r.newest = False
                r.save()
        if request.POST.get("risk_or_issue", "") == "issue":
            Issue_id = Issue.objects.filter(project_id=project).filter(issue_id=request.POST.get("id", ""))
            if Issue_id.count() > 0:
                i = Issue_id.get(newest=True)
                i.newest = False
                i.save()
        

        
        Title = request.POST.get("title", "")
        Category = request.POST.get("category", "")
        Severity = request.POST.get("severity", "")
        Probability = request.POST.get("probability", "")
        Comment = request.POST.get("comment", "")
        Open_date = request.POST.get("open_date", "")
        Close_date = request.POST.get("close_date", "")
        Assigned_to = request.POST.get("assigned_to", "")
        Next_step = request.POST.get("next_step", "")
        External_dependencies = request.POST.get("external_dependencies", "")
        Project_id  = request.POST.get("project_id", "")
        RID = request.POST.get("id", "")
        IID = request.POST.get("id", "")

        #create new risk or issue                                                                                                                          
        if request.POST.get("risk_or_issue", "") == "issue":
            new_issue = Issue(title=Title, category=RI_Category.objects.get(ri_category=Category), severity=Health.objects.get(health=Severity), comment=Comment, project_id=Project_id, 
                              open_date=Open_date, close_date=Close_date, assign_to=Assigned_to, next_step=Next_step, external_dependencies=External_dependencies, issue_id=IID, newest=True)
            new_issue.save()
        if request.POST.get("risk_or_issue", "") == "risk":
            new_risk = Risk(title=Title, category=RI_Category.objects.get(ri_category=Category), severity=Health.objects.get(health=Severity), probability=Level.objects.get(level=Probability), comment=Comment, project_id=Project_id, 
                            open_date=Open_date, close_date=Close_date, assign_to=Assigned_to, next_step=Next_step, external_dependencies=External_dependencies, risk_id=RID, newest=True)
            new_risk.save()
    
    project_id = Project.objects.filter(project_id=project).latest('timestamp').pk
    risk = Risk.objects.filter(project_id=project).filter(newest=True)
    issue = Issue.objects.filter(project_id=project).filter(newest=True)
    p = Project.objects.get(pk=project_id)
    risk_num = risk.count()
    issue_num = issue.count()

    context_instance=RequestContext(request,{
            'p' : p,
            'risk' : risk,
            'issue' : issue,
            'rnum' : risk_num,
            'inum' : issue_num,
        })

    return render_to_response('Models/ritable.html', context_instance)
    





#For note table
def note(request, project):
    if request.method == 'POST':

        
        Note_id = Note.objects.filter(project_id=project).filter(note_id=request.POST.get("note_id", ""))
        if Note_id.count() > 0:
            n = Note_id.get(newest=True)
            n.newest = False
            n.save()





        Title = request.POST.get("title", "")
        Comment = request.POST.get("comment", "")
        Project_id  = request.POST.get("project_id", "")
        Date = request.POST.get("date", "")
        ID = request.POST.get("note_id", "")

    #create new note           
        new_note = Note(title=Title, comment=Comment, project_id=Project_id, date=Date, note_id=ID, newest=True)
        new_note.save()

    project_id = Project.objects.filter(project_id=project).latest('timestamp').pk
    note = Note.objects.filter(project_id=project).filter(newest=True)
    note_num = note.count()
    p = Project.objects.get(pk=project_id)


    context_instance=RequestContext(request,{
            'p' : p,
            'note' : note,
            'num' : note_num,
        })

    return render_to_response('Models/notetable.html', context_instance)                                                                                                                                                         


    project_id = Project.objects.filter(project_id=project).latest('timestamp').pk
    note = Note.objects.filter(project_id=project).filter(newest=True)
    p = Project.objects.get(pk=project_id)
    
    context_instance=RequestContext(request,{
            'p' : p,
            'note' : note,
        })

    return render_to_response('Models/notetable.html', context_instance)








#If you use the search bar. If possible, future versions should just redirect to project.
def search(request):
    project = "0"
    if request.method == 'POST':
        project = request.POST.get("project_id", "")

    if request.POST.get("type", "")  == "issue":                                                                                                             
        Title = request.POST.get("title", "")
        Category = request.POST.get("category", "")
        Severity = request.POST.get("severity", "")
        Comment = request.POST.get("comment", "")
        Open_date = request.POST.get("opendate", "")
        Assigned_to = request.POST.get("assignedto", "")
        Next_step = request.POST.get("next_step", "")
        External_dependencies = request.POST.get("externdepend", "")
        Project_id  = request.POST.get("project_id", "")
        IID = request.POST.get("num", "")

        new_issue = Issue(title=Title, category=RI_Category.objects.get(ri_category=Category), severity=Health.objects.get(health=Severity), comment=Comment, project_id=Project_id,
                              open_date=Open_date, close_date="9999-12-12", assign_to=Assigned_to, next_step=Next_step, external_dependencies=External_dependencies, issue_id=IID, newest=True)
        new_issue.save()

    if request.POST.get("type", "")  == "milestone":                                                                                                      
        Title = request.POST.get("title", "")
        Comment = request.POST.get("description", "")
        Project_id  = request.POST.get("project_id", "")
        STATUS = request.POST.get("severity", "")
        Baseline_date = request.POST.get("basedate", "")
        Target_date = request.POST.get("targetdate", "")
        ID = request.POST.get("num", "")

    #create new milestone                                                                                                                                             
                                                                                                                                                                       
        new_milestone = Milestone(title=Title, comment=Comment, project_id=Project_id, status = Status.objects.get(status=STATUS),baseline_date=Baseline_date, target_date=Target_date,  milestone_id=ID, newest=True)
        new_milestone.save()

    if request.POST.get("type", "")  == "note":                                                                                                                                                                                                                           
        Title = request.POST.get("title", "")
        Comment = request.POST.get("text", "")
        Project_id  = request.POST.get("project_id", "")
        Date = request.POST.get("date", "")
        ID = request.POST.get("num", "")    

    project_id = Project.objects.filter(project_id=project).latest('timestamp').pk
    p = Project.objects.get(pk=project_id)

 
    if request.POST.get("type", "")  == "risk":
        Title = request.POST.get("title", "")
        Category = request.POST.get("category", "")
        Severity = request.POST.get("severity", "")
        Probability = request.POST.get("probability", "")
        Comment = request.POST.get("comment", "")
        Open_date = request.POST.get("opendate", "")
        Assigned_to = request.POST.get("assignedto", "")
        Next_step = request.POST.get("next_step", "")
        External_dependencies = request.POST.get("externdepend", "")
        Project_id  = request.POST.get("project_id", "")
        RID = request.POST.get("num", "")

        new_risk = Risk(title=Title, category=RI_Category.objects.get(ri_category=Category), probability=Level.objects.get(level=Probability), severity=Health.objects.get(health=Severity), comment=Comment, project_id=Project_id, open_date=Open_date, close_date="9999-12-12", assigned_to=Assigned_to, next_step=Next_step, external_dependencies=External_dependencies, risk_id=RID, newest=True)
        new_risk.save()

    project_id = Project.objects.filter(project_id=project).latest('timestamp').pk
    p = Project.objects.get(pk=project_id)

    #Get issue objects                                                                                                                                                 
    issues = Issue.objects.filter(project_id=project).filter(newest=True).order_by('-timestamp')
    issues_recent = issues.filter(timestamp__gt= timezone.now() - datetime.timedelta(days=1))
    #Get milestone objects                                                                                                                                             
    milestone = Milestone.objects.filter(project_id=project).filter(newest=True).order_by('-timestamp')
    milestone_recent = milestone.filter(timestamp__gt= timezone.now() - datetime.timedelta(days=1))

    #Get note objects                                                                                                                                                  
    note = Note.objects.filter(project_id=project).filter(newest=True).order_by('-timestamp')
    note_recent = note.filter(timestamp__gt= timezone.now() - datetime.timedelta(days=1))

    #Get risk objects                                                                                                                                                  
    risk = Risk.objects.filter(project_id=project).filter(newest=True).order_by('-timestamp')
    risk_recent = risk.filter(timestamp__gt= timezone.now() - datetime.timedelta(days=1))
    #Get role objects                                                                                                                                                  
    personnel = Personnel.objects.filter(project_id=project).filter(active=True)


    #Get number of items                                                                                                                                               
    issue_num = issues.count()
    milestone_num = milestone.count()
    note_num = note.count()
    risk_num = risk.count()

    gstatus = Status.objects.get(status="Active - Green")

    if request.POST.get("status", "") != "":
        status = request.POST.get("status", "")
        p.status = Status.objects.get(status=status)
        p.save()

    gstatus = Status.objects.get(status="Active - Green")
    ystatus = Status.objects.get(status="Active - Yellow")
    rstatus = Status.objects.get(status="Active - Red")

    mile_type = Milestone.objects.filter(project_id=p.project_id).exclude(mile_type="Other")
    
    # List of all ri_categories                                                                                                                                                                                                                   
    category = RI_Category.objects.all()
  #  compliance = category.get(ri_category="compliance")                                                                                                                                                                                          
    context_instance=RequestContext(request,
                      {'issues' : issues,
                       'p' : p,
                       'milestone' : milestone,
                       'note' : note,
                       'risk' : risk,
                       'personnel' : personnel,
                       'issues_recent' : issues_recent,
                       'milestone_recent' : milestone_recent,
                       'note_recent' : note_recent,
                       'risk_recent' : risk_recent,
                       'milestone_num' : milestone_num,
                       'note_num' : note_num,
                       'risk_num' : risk_num,
                       'issue_num' : issue_num,
                       'gstatus' : gstatus,
                       'ystatus' : ystatus,
                       'rstatus' : rstatus,
                       'mile_type' : mile_type,
                       'compliance' : category.get(ri_category="Compliance"),
                       'cost' : category.get(ri_category="Cost"),
                       'dependency' : category.get(ri_category="Dependency"),
                       'info_assurance' :category.get(ri_category="Info Assurance"),
                       'organizational' :category.get(ri_category="Organizational"),
                       'privacy' :category.get(ri_category="Privacy"),
                       'resources' :category.get(ri_category="Resources"),
                       'schedule' :category.get(ri_category="Schedule"),
                       'security' : category.get(ri_category="Security"),
                       'strategic' :category.get(ri_category="Strategic"),
                       'scope' :category.get(ri_category="Scope"),
                       'technical' :category.get(ri_category="Technical"),

                       })

    return render_to_response('Models/profile.html', context_instance)





#For first page of intake
def intakeOne(request):

    pname = request.POST.get("name", "")
    pemail = request.POST.get("email", "")
    pdivision = request.POST.get("division", "")
    poffice = request.POST.get("office", "")
    psponsor = request.POST.get("sponsor", "")
    ppoc = request.POST.get("poc", "")
    pdescription = request.POST.get("description", "")
    pmethod = request.POST.get("method", "")
    pdate = request.POST.get("date", "")
    plaunchdate = request.POST.get("launchdate", "")
    pstaff = request.POST.get("staff", "")
    v1 = request.POST.get("value1", "")
    v2 = request.POST.get("value2", "")
    v3 = request.POST.get("value3", "")
    v4 = request.POST.get("value4", "")
    v5 = request.POST.get("value5", "")
    comment = request.POST.get("comment", "")
    needyn1 = request.POST.get("needyn1", "")
    needyn2 = request.POST.get("needyn2", "")
    needyn3 = request.POST.get("needyn3", "")
    needyn4 = request.POST.get("needyn4", "")
    needyn5 = request.POST.get("needyn5", "")
    needyn6 = request.POST.get("needyn6", "")
    valueyn1 = request.POST.get("valueyn1", "")
    valueyn2 = request.POST.get("valueyn2", "")
    valueyn3 = request.POST.get("valueyn3", "")
    valueyn4 = request.POST.get("valueyn4", "")
    valueyn5 = request.POST.get("valueyn5", "")
    valueyn6 = request.POST.get("valueyn6", "")
    techrisk1 =request.POST.get("techrisk1","")
    techrisk2 =request.POST.get("techrisk2","")
    techrisk3 =request.POST.get("techrisk3","")
    techrisk4 =request.POST.get("techrisk4","")
    techrisk5 =request.POST.get("techrisk5","")
    techrisk6 =request.POST.get("techrisk6","")
    techrisk7 =request.POST.get("techrisk7","")

    context_instance=RequestContext(request,{
            'name' : pname,
            'email': pemail,
            'division' : pdivision,
            'office' : poffice,
            'sponsor' : psponsor,
            'poc' : ppoc,
            'description' : pdescription,
            'method' : pmethod,
            'date' : pdate,
            'launchdate' : plaunchdate,
            'staff' : pstaff,
            'value1' : v1,
            'value1' : v2,
            'value1' : v3,
            'value1' : v4,
            'value1' : v5,
            'comment' : comment,
            'needyn1' : needyn1,
            'needyn2' :needyn1,
            'needyn3' :needyn1,
            'needyn4' :needyn1,
            'needyn5' :needyn1,
            'needyn6' :needyn1,
            'valueyn1' :valueyn1,
            'valueyn2' :valueyn2,
            'valueyn3' :valueyn3,
            'valueyn4' :valueyn4,
            'valueyn5' :valueyn5,
            'valueyn6' :valueyn6,
            'techrisk1':techrisk1,
            'techrisk2':techrisk2,
            'techrisk3':techrisk3,
            'techrisk4':techrisk4,
            'techrisk5':techrisk5,
            'techrisk6':techrisk6,
            'techrisk7':techrisk7,
                                    })

    if request.POST.get("back2", "") != "":
        return render_to_response('Models/intake1.html', context_instance)
    if request.POST.get("next1", "") != "" or request.POST.get("next3", ""):
        if pemail == "":
            context_instance=RequestContext(request, {
                    'error' : 'We need your email in order to complete the process'
                })
            return render_to_response('Models/intake1.html', context_instance)
        return render_to_response('Models/intake2.html', context_instance)
    if request.POST.get("next2", "") != "":
        return render_to_response('Models/intake3.html', context_instance)
    
    
    if Project.objects.filter(name=pname).count() > 0:
        project_id = Project.objects.filter(name=pname).latest('timestamp').project_id
    else:
        project_id = Project.objects.count() + 1000


    # create new object of history
    if request.POST.get("submit", "") != "":
        project=Project(
        name = pname,
        email = pemail,
        division = Division.objects.get(division=pdivision),
        office = Office.objects.get(office=poffice),
        sponsor = psponsor,
        poc = ppoc,
        description = pdescription,
        method = Methodology.objects.get(methodology=pmethod),
        date = pdate,
        launchdate = plaunchdate,
        staff = pstaff,
        v1 = v1,
        v2 = v2,
        v3 = v3,
        v4 = v4,
        v5 = v5,
        comment = comment,
        needyn1 = needyn1,
        needyn2 = needyn2,
        needyn3 = needyn3,
        needyn4 = needyn4,
        needyn5 = needyn5,
        needyn6 = needyn6,
        valueyn1 = valueyn1,
        valueyn2 = valueyn2,
        valueyn3 = valueyn3,
        valueyn4 = valueyn4,
        valueyn5 = valueyn5,
        valueyn6 = valueyn6,
        techrisk1 = techrisk1,
        techrisk2 = techrisk2,
        techrisk3 = techrisk3,
        techrisk4 = techrisk4,
        techrisk5 = techrisk5,
        techrisk6 = techrisk6,
        techrisk7 = techrisk7,
        status = Status.objects.get(status="Pending"),
        poc_contact_info = "",
        project_id = project_id,
        )

        project.save()

        return render_to_response('Models/confirmation.html', context_instance)
    
    else:
        return render_to_response('Models/intake1.html', context_instance)





#For pending project table
def pending(request):
    project = Project.objects.filter(status=Status.objects.get(status="Pending"))

    context_instance=RequestContext(request, {
                    'project' : project
                })
    return render_to_response('Models/pending.html', context_instance)    



#For MPL
def mpl(request):
    project = Project.objects.all()
    context_instance=RequestContext(request, {
                    'project' : project
                })
    return render_to_response('Models/mpl.html', context_instance)






#For reports
def report(request):
    project_red = Project.objects.filter(status=Status.objects.get(status="Active - Red"))
    project_yellow = Project.objects.filter(status=Status.objects.get(status="Active - Yellow"))
    project_green = Project.objects.filter(status=Status.objects.get(status="Active - Green"))
    project_complete = Project.objects.filter(status=Status.objects.get(status="Completed")).filter(timestamp__gt= timezone.now() - datetime.timedelta(days=90))
    
    risk = Risk.objects.filter(timestamp__gt= timezone.now() - datetime.timedelta(days=7))
    issue = Issue.objects.filter(timestamp__gt= timezone.now() - datetime.timedelta(days=7))
    note = Note.objects.filter(timestamp__gt= timezone.now() - datetime.timedelta(days=7))
    milestone = Milestone.objects.filter(timestamp__gt= timezone.now() - datetime.timedelta(days=7))
   
    no_response = 0
    response_issue = 0
    response_none = 0
    gcap1 = project_green.filter(capnum=1).count()
    ycap1 = project_yellow.filter(capnum=1).count()
    rcap1 = project_red.filter(capnum=1).count()
    gcap2 = project_green.filter(capnum=2).count()
    ycap2 = project_yellow.filter(capnum=2).count()
    rcap2 = project_red.filter(capnum=2).count()
    gcap3 = project_green.filter(capnum=3).count()
    ycap3 = project_yellow.filter(capnum=3).count()
    rcap3 = project_red.filter(capnum=3).count()
    gcap4 = project_green.filter(capnum=4).count()
    ycap4 = project_yellow.filter(capnum=4).count()
    rcap4 = project_red.filter(capnum=4).count()
    gcap5 = project_green.filter(capnum=5).count()
    ycap5 = project_yellow.filter(capnum=5).count()
    rcap5 = project_red.filter(capnum=5).count()
    gcap6 = project_green.filter(capnum=6).count()
    ycap6 = project_yellow.filter(capnum=6).count()
    rcap6 = project_red.filter(capnum=6).count()
    gcap7 = project_green.filter(capnum=7).count()
    ycap7 = project_yellow.filter(capnum=7).count()
    rcap7 = project_red.filter(capnum=7).count()
    gcap8 = project_green.filter(capnum=8).count()
    ycap8 = project_yellow.filter(capnum=8).count()
    rcap8 = project_red.filter(capnum=8).count()
    ccap1 = project_complete.filter(capnum=1).count()
    ccap2 = project_complete.filter(capnum=2).count()
    ccap3 = project_complete.filter(capnum=3).count()
    ccap4 = project_complete.filter(capnum=4).count()
    ccap5 = project_complete.filter(capnum=5).count()
    ccap6 = project_complete.filter(capnum=6).count()
    ccap7 = project_complete.filter(capnum=7).count()
    ccap8 = project_complete.filter(capnum=8).count()

    for p in project_red:
        if issue.filter(project_id=p.project_id).count() == 0 and risk.filter(project_id=p.project_id).count() == 0 and note.filter(project_id=p.project_id).count() == 0 and milestone.filter(project_id=p.project_id).count() == 0:
            no_response += 1           
        elif issue.filter(project_id=p.project_id).count() > 0:
            response_issue += 1
        else:
            response_none += 1

    for p in project_yellow:
        if issue.filter(project_id=p.project_id).count() == 0 and risk.filter(project_id=p.project_id).count() == 0 and note.filter(project_id=p.project_id).count() == 0 and milestone.filter(project_id=p.project_id).count() == 0:
            no_response+= 1
        elif issue.filter(project_id=p.project_id).count() > 0:
            response_issue += 1
        else:
            response_none += 1

    for p in project_green:
        if issue.filter(project_id=p.project_id) == 0 and risk.filter(project_id=p.project_id) == 0 and note.filter(project_id=p.project_id) == 0 and milestone.filter(project_id=p.project_id) == 0:
            no_response+= 1
        elif issue.filter(project_id=p.project_id) > 0:
            response_issue += 1
        else:
            response_none += 1

    if History.objects.all().count() == 0 or History.objects.filter(timestamp__gt= timezone.now() - datetime.timedelta(days=7)).count() == 0:
        active = project_red.count() + project_yellow.count() + project_green.count()
        score = ( (project_yellow.count() * 50) + (project_green.count() * 100) ) / (active)
        h = History(score=score, active=active)
        h.save()

    history = History.objects.all()
        
    
    context_instance=RequestContext(request, {
            'no_response' : no_response,
            'response_issue' : response_issue,
            'response_none' : response_none,
            'gcap1' : gcap1,
            'ycap1' : ycap1,
            'rcap1' : rcap1,
            'gcap2' : gcap2,
            'ycap2' : ycap2,
            'rcap2' : rcap2,
            'gcap3' : gcap3,
            'ycap3' : ycap3,
            'rcap3' : rcap3,
            'gcap4' : gcap4,
            'ycap4' : ycap4,
            'rcap4' : rcap4,
            'gcap5' : gcap5,
            'ycap5' : ycap5,
            'rcap5' : rcap5,
            'gcap6' : gcap6,
            'ycap6' : ycap6,
            'rcap6' : rcap6,
            'gcap7' : gcap7,
            'ycap7' : ycap7,
            'rcap7' : rcap7,
            'gcap8' : gcap8,
            'ycap8' : ycap8,
            'rcap8' : rcap8,
            'ccap1' : ccap1,
            'ccap2' : ccap2,
            'ccap3' : ccap3,
            'ccap4' : ccap4,
            'ccap5' : ccap5,
            'ccap6' : ccap6,
            'ccap7' : ccap7,
            'ccap8' : ccap8,
            'history' : history,
                })

    return render_to_response('Models/projhealthdash.html', context_instance)


#For the Risk & Issues Deck. MORE WORK NEEDS TO BE DONE IN ORDER TO PUSH 
#INFORMATION ABOUT ALL CURRENT RISK AND ISSUES INTO THE TABLE.
def deck(request):
    context_instance=RequestContext(request)

    return render_to_response('Models/progreport.html', context_instance)
