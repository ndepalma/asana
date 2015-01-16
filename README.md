# Asana2todoist fork
I commited this simple script because I figured it had to be useful for anyone moving between asana and todoist. 

Very simple fork from the original (mad respect to [pandemicsyn](https://github.com/pandemicsyn/asana) for the original asana code.) The intention of this is that you are throwing out all of your asana tools and moving to todoist so you don't want to install all of the asana toolkits just to delete them. [Cit](https://github.com/fatih/cit) was the main command line tool I decided to use for todoist. 

Dead simple Instructions:

1. I started with a cleaned out todoist. If you have items in there already, I can't promise anything but it will probably work anyway. 
2. Get your asana key (read below)
3. Install [cit](https://github.com/fatih/cit) and make sure it's on your _$PATH_
4. Edit the move_it_script.py file and add your API key to the variable _asana_api_key_
5. <pre> $ python move_it_script.py </pre>
6. 'cit ls' to make sure it works
7. Profit.

_Older documentation below_
# Asana python api 

python wrapper for the [Asana API](http://asana.com)

Documentation is available at: [AsanaAPI](http://asana.readthedocs.org/en/latest/index.html)

This project is a work in progress. Here's what's currently available:

- add_project_task
- add_story
- add_tag_task
- create_project
- create_tag
- create_task
- add_parent
- create_subtask
- get_basic_auth
- get_project
- get_project_tasks
- get_story
- get_subtasks
- get_tag_tasks
- rm_tag_task
- get_task_tags
- get_tags
- get_task
- list_projects
- list_stories
- list_tasks
- list_users
- list_workspaces
- rm_project_task
- update_project
- delete_project
- update_task
- update_workspace
- user_info

Todo:

- All the things!
- unittests
- Better error handling

Sample:

    from asana import asana
    asana_api = asana.AsanaAPI('YourAsanaAPIKey', debug=True)

    # see your workspaces
    myspaces = asana_api.list_workspaces()  #Result: [{u'id': 123456789, u'name': u'asanapy'}]

    # create a new project
    asana_api.create_project('test project', myspaces[0]['id'])

    # create a new task
    asana_api.create_task('yetanotherapitest', myspaces[0]['id'], assignee_status='later', notes='some notes')

    # add a story to task
    asana_api.add_story(mytask, 'omgwtfbbq')

