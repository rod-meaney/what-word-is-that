# what-word-is-that
This is a project that I created with the sole purpose of teaching myself how to do React front and programming.  Having said that the source code for the React clients is in 2 other projects.  This makes this project three parts

 - [UI for optional authenticated game](https://github.com/rod-meaney/guess-word) : A React Bootstrap application (read directory in this repository contains the build)
 - [UI for authenticated list management](https://github.com/rod-meaney/guess-word-edit) : A React Bootstrap application (edit directory in this repository contains the build)
 - Backend and API's for the 2 frontend modules : Google Cloud App Engine application deployed to Google App Engine and available at [what-word-is-that](https://what-word-is-that.appspot.com/) utilising Google Big Table.
 
## Limitations
The game is not intended to be perfect :-). I have only really tested it on Apple devices and have had a few people test it on none Apple devices and it seems to work. I am expecting issues to be raised and will address them as they arise.

## What next
1. As with all Javascript frameworks they seem to change faster than most people can reasonably keep up with. However it appears i should probably invest in hooks and effects and as time permits I will look at investing in those.
2. The backend is using Google App Engine which I loved since I saw it at Yow in something like 2013.  It has moved on and I need to find something other than the python 2.7 frameworks to build my backends.  Maybe as I investigate AWS and Azure I will build different backends for the same front ends.  
