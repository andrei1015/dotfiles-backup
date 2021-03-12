# the simple .dotfile manager

#### executable

Double click the file called `backup`. That's it. Either that or your file manager thinks otherwise, in which case you need to tell it to open the file as an application.

###### why?

Searched a bit on the subject, all solutions seemed overcomplicated, plus always wanted to create an app with UI, and coming from web stuff this has been interesting.

###### how?

It doesn't get simpler than this. Through the app you can create a list of files and folders you want to backup, usually dotfiles but you can use it for anything really.

How it works is it takes each location from the list and it makes a copy being mindful of paths. This way you have all your files in a separate folder and you can do with that folder whatever you want to save its contents. You can create a tarball or use git to manage them, I don't care.

* the **add** and **remove selected** buttons are self explanatory. 
* **remove selected** also deletes the backed up path!!!
* the **sync** button goes through your list and copies all the paths to the backup folder. this action **<span style="color:red">overwrites</span>** what you already have in there so be sure to save that snapshot of your dotfiles!
* the **restore** button copies whatever you have in your backups folder to the original locations, **<span style="color:red">overwriting</span>** them if they already exist. i would only use this when on a fresh install to get going faster.

###### why is X feature missing?

I'm a beginner in stuff like this. I'm a beginner in a lot of things. But this is your golden chance! The code is free and open source, feel free to help!

#### roadmap
---

??

###### testing

For testing i have made a few mock locations inside the /etc/skel folder and whenever i want to check something i create a new user. This way you do not risk messing up your own home directory.