---
layout: post
title: How this site was built
date: 2020-05-29 14:33 -0400
tags: jekyll Githhub
image: /assets/img/gitjekyll.jpg
optimized_image: /assets/img/gitjekyll_optimized.png
description: "How to build a site with Github and Jekyll"
---



# How to install and maintain a Github hosted website using jekyll

## Install Jekyll

[https://jekyllrb.com/](https://jekyllrb.com/)

The first step is installing Jekyll on your machine.
There are detailed instruction on how to do this.

## Install Github

[https://gitforwindows.org/](https://gitforwindows.org/)

If you're on Mac or Linux, Git is most likely already installed. If you're on Windows, go to git-for-windows.github.io and follow the instructions to install Git. 


Once you have those installed, goto your command line and type these commands to makes sure it has installed properly.
Its not important to have the same version as me this step is more as a double check. 

![image]({{ site.baseurl }}/assets/img/jekyll_git_version.JPG)

## Create a new Site

Open up your terminal navigate to the place where you want to store your site files.
  and then run the 
 Jekyll new command, and then give a name for the project, I'll call it "projectHB"



![walking]({{ site.baseurl }}/assets/img/run_jekyll_new.JPG)

Running Jekyll new creates a new folder called "projectHB" with a bunch of files inside. 

cd into that folder
Then you want to open it up in your favorite text editor or code editor. I use Visual Studio Code but you should use whatever IDE you are comgortable with. 

Jekyll sets up a blog-style site with a sample post in this _post folder. 
If you are building a blog, any new post you write will go into this _post folder as well. 

Now initialize a git repository for this project.

"git init" to initialize a git repository

![image]({{ site.baseurl }}/assets/img/git_init.JPG)

"git add ."

![image]({{ site.baseurl }}/assets/img/git_add_period.JPG)

and "git commit -m" and I'll just say "build" as the note

![image]({{ site.baseurl }}/assets/img/git_commit_m_build.JPG)


Make sure you have navigated inside the site folder you created then run the following 

If you're on Windows you need to run a command called
"bundle lock --add-platform ruby", and then "bundle lock --add-platform x86_64-linux"


![image]({{ site.baseurl }}/assets/img/bundle_lock_add-platform_x86_64_linux.JPG)


## Preview the site

To preview the site, we'll run this command in the terminal.


bundle exec jekyll serve

![image]({{ site.baseurl }}/assets/img/bundel_exec_jekyll_serve.JPG)



Then open a web browser and post this into the URL

 http://127.0.0.1:4000/

This is what the site should look like at this point

![image]({{ site.baseurl }}/assets/img/preview_site.JPG)

 GO back into the terminal and press Control + C to stop the preview server.
 
 
![image]({{ site.baseurl }}/assets/img/ctrl_c.JPG)

## Install a Theme

There are many Jekyll themes available on sites like jekyllthemes.org and jekyllthemes.io 


Most themes come with instructions that will tell you how to install the theme in your project. 

On https://jamstackthemes.dev/  I found a blog site theme just like my favorite website medium. Its called Mediumish. Now I will follow the link to the gituhub repository where the theme is located 
![image]({{ site.baseurl }}/assets/img/mediumish-jekyll-template.JPG)

https://github.com/wowthemesnet/mediumish-theme-jekyll
![image]({{ site.baseurl }}/assets/img/githubtheme.JPG)




Now click on clone or download
![image]({{ site.baseurl }}/assets/img/githubtheme.JPG)

then click on download zip
![image]({{ site.baseurl }}/assets/img/downloadzip.JPG)

Loacte where you downloaded the file
![image]({{ site.baseurl }}/assets/img/locatedownload.JPG)

Extract the file to a new file folder
![image]({{ site.baseurl }}/assets/img/with_new_project_open.JPG)

With both folders open located your project file that holds the the basic jekyll theme you created 
![image]({{ site.baseurl }}/assets/img/select_all_new_theme.JPG)

Open the project folder and select all the folders and delete them
Open the new download and extracted theme. Select them all 
Then move them all to the project folder
![image]({{ site.baseurl }}/assets/img/move_to_new_project_folder.JPG)


Then run "bundle install" again
![image]({{ site.baseurl }}/assets/img/bundle_install_with_template.JPG)

Then run "bundel exec jekyll serve".
You can now pre-view your site by going to http://127.0.0.1:4000/
![image]({{ site.baseurl }}/assets/img/bundel_exec_jekyll_serve_new_theme.JPG)

## Now open the file folder in your IDE of choice. 
![image]({{ site.baseurl }}/assets/img/open_editor.JPG)








## The configuration file config.yml

Every jekyll project contains a configuration file called _config.yml

Open you editor and naviagate to your project file. 
Then open the configuration file. 

![image]({{ site.baseurl }}/assets/img/open_config_file.JPG)


You can change the title of your site
Add an email address here and  add a description as 

Later on, when you get ready to publish the site and you have your own domain name, you want to put that  in the Url property. 

if you make changes to config.yml, they won't be picked up until after your restart the previous server manually. 
What I mean by that is go into the terminal, press in Ctrl+C to stop it, now run "bundle exec jekyll serve" to see your changes




## Add a Post

Posts go in the underscore posts folder. You can manually create a new file in that folder. In order for it to publish, the file name must be exactly like the others. And it must be a .md or markdown file format. 


![image]({{ site.baseurl }}/assets/img/new_post.JPG)

## Edit front matter content

The section at the top of each post file is called the front matter. This section stores metadata or properties about the post. You can change or add to these properties to change things about the post. 
![image]({{ site.baseurl }}/assets/img/front_matter.JPG)


## Add a Page

When you want to edit the about page simple open it in your IDE. It too is in markdown lanuage and easy to edit. 

If you would like to add new pages you will do it here under the pages folder. For example if you want to create a page
describing how you made your site this might be a great place for it 

![image]({{ site.baseurl }}/assets/img/add_pages.JPG)

## Generate the Site Files

To deploy the site to the web, you'll need to run a different command to tell Jekyll to generate the final site files. 

bundle exec jekyll build 
![image]({{ site.baseurl }}/assets/img/bundel_exec_jekyll_build.JPG)


All of the site files are saved in folder called site. 
We need  upload these files to a web server. 
Make sure that everything is checked into Git. 
git status
![image]({{ site.baseurl }}/assets/img/git_status.JPG)

git add .

![image]({{ site.baseurl }}/assets/img/git_add_period.JPG)
 
git commit -m "build"
![image]({{ site.baseurl }}/assets/img/git_commit_m_build.JPG)

## Set up for Github

Sign into Github and click New

![image]({{ site.baseurl }}/assets/img/click_new.JPG)

Push an existing repository from the command line
git push --set-upstream origin master

![image]({{ site.baseurl }}/assets/img/git_push_done.JPG)

What it will say when its done



## Deploy with netifly

Log into netlify 
https://www.netlify.com/

Follow instructions and give Netlify acccess to the new repo
![image]({{ site.baseurl }}/assets/img/give_netlify_access.JPG)


Add custom Domain
![image]({{ site.baseurl }}/assets/img/add_custom_domain.JPG)




# Add new Posts to website from Command line

Open the website file in your IDE
![image]({{ site.baseurl }}/assets/img/open_editor.JPG)

Go into the psot folder and create a new folder. 
Jekyll will only publish your new post if you follow the title format YYYY-MM-DD.
Start every new post with the date that you want it published.
![image]({{ site.baseurl }}/assets/img/new_md.JPG)


Open the Command line Run "git status"
![image]({{ site.baseurl }}/assets/img/git_status.JPG)

Add the changes to the local git repo with "git add ."
![image]({{ site.baseurl }}/assets/img/git_add_period.JPG)

Commit the new post with git commit -m "name the change" 
![image]({{ site.baseurl }}/assets/img/git_commit_new_post.JPG)

Add it to the github repo with git push
![image]({{ site.baseurl }}/assets/img/git_push_new_post.JPG)





