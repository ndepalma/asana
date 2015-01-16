from asana import asana
import subprocess

justprint = False

addbyproject = False
addbyassignee = False

## ADD YOUR Asana API key here as string::
asana_api_key = ''

asana_api = asana.AsanaAPI(asana_api_key, debug=False)

myspaces = asana_api.list_workspaces()

ws = myspaces[0]['id']

allprojects = asana_api.list_projects(myspaces[0]['id'], False)

if addbyproject:
    for project in allprojects:
        pid = project['id']
        cmd = 'cit add -p "' + project['name'] + '"'
        if justprint:
            print "", project['name'], ":"
            print "Command: ", cmd
        else:
            subprocess.call(cmd, shell=True)
        tsks = asana_api.get_project_tasks(pid, False)
        for tsk in tsks:
            tid = tsk['id']
            tskm = asana_api.get_task(tid)
            if not tskm['completed'] and tskm['assignee'] == None:
                cmd = 'cit add "' + tsk['name'] + '" +"' + project['name'] + '"'
                if justprint:
                    print "\t", tsk['name']
                    print "Command: ", cmd
                else:
                    subprocess.call(cmd, shell=True)

if addbyassignee:
    me = asana_api.user_info()
    tsks = asana_api.list_tasks(ws, me['id'])
    for tsk in tsks:
        tid = tsk['id']
        tskm = asana_api.get_task(tid)
        if not tskm['completed']:
            cmd = 'cit add "' + tsk['name'] + '" +"Inbox"'
            print "\t", tsk['name']
            #print "Command: ", cmd
            subprocess.call(cmd, shell=True)
