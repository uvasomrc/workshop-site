# SOMRC Workshops Site

[![Build Status](https://travis-ci.org/uvasomrc/workshop-site.svg?branch=master)](https://travis-ci.org/uvasomrc/workshop-site)

Serves teaching content for SOMRC workshops. Commits here will automatically publish to https://workshops.somrc.virginia.edu/ via TravisCI.
Content can be written in either standard markdown, HTML, or Rmarkdown.

More about workshop offerings can be found [here](https://www.rc.virginia.edu/education/workshops/).

## Contributing

The material hosted on this site is written in Markdown and R Markdown (see [lessons](/content/lessons/)). Content is rendered with the `blogdown` R package, which uses the `hugo` static site generator. Because many of these lessons require R package dependencies, we've put together a portable environment using `Docker` that includes everything necessary to build the site. 

### Getting started

First, install `Git` and clone this repository:

`git clone https://github.com/uvasomrc/workshop-site.git`

`cd workshop-site`
 
### Creating a new lesson

To create a new lesson, add a markdown or R markdown file underneath the `content/lesson` directory. 

Alternatively, if you're using the `hugo` command-line interface the following will stub out a new `.Rmd` lesson file for you:

`hugo new lesson/{lesson-name}`

### Testing a new lesson locally

Once you've written your content, you can test the new lesson using an environment that includes all of the site dependencies. This environment is available as a `Docker` image:

<https://hub.docker.com/r/somrc/hugo-workshop-build/>

To work with this containerized image, make sure you have `Docker` installed and then pull the image:

`docker pull somrc/hugo-workshop-build`

From the root the workshop site folder (wherever you've cloned the `Git` repository), update permissions on your machine so that `test-site.sh` is executable ...

`chmod +x test-site.sh`

... and then run the `test-site.sh` script:

`docker run -v $(pwd):/root/workshop-site -p 4321:4321 somrc/hugo-workshop-build /root/workshop-site/test-site.sh`

If you open a web browser and navigate to `localhost:4321` you should see a built version of the site. Any changes you make to the site on your computer will trigger the site to attempt a rebuild and refresh automatically.
