# Build a blog on "Read the Docs"

:material-tag-multiple: :
`blog` `mkdocs` `github` `read the docs`


## Introduction

This blog summarises how to build a blog on RTD with MkDocs and GitHub.
This combination might not suit everyone but meets most of my needs. 
I want to write my blogs in a quick manner but still in a nice-look format.
I want to publish my blogs easily and spend less time on publishing process.
I want the modifications to be easily traceable.
I want the whole blog site to be moveable and easy to migrate to another site.
I've been using RTD, MkDocs and GitHub for project documentation.
And I find them good for building a blog website too.


## Pros and cons

*Pros*:

- Blogs are written in Markdown.
  MkDocs got heaps of useful plugins and Markdown extensions that makes writing
  documentation a piece of cake.
- The way to publish on GitHub and render on RTD is easy and mature.
  You can even directly write your blog on GitHub.
- GitHub as a version control tool natually traces the modifications.
- MkDocs generates a static HTML website from the Markdown files.
  It is highly moveable because there is no database associated with it.

*Cons*:

- Each file size is limited to 100MB and the total repository size is limited to 10GB
  by GitHub. A rough calculation suggests I won't hit these limits for decades.


## Instructions

If you are still reading this blog, you might want to build one like it.
Follow the instruction below, you should find it easy.


### Preparation

- Install Python and setup a virtual environment.
Please read [this page][setup_python_link] to install Python and setup a virtual
environment for building a blog.

  [setup_python_link]: ../../2021/03/setup_python_study_env_on_windows.md

- Prepare GitHub and RTD account.
If you did not sign up with [GitHub][github_link] or [RTD][rtd_link] yet,
please do so by following the instructions on their websites.

  [github_link]: https://github.com/
  [rtd_link]: https://readthedocs.org/

- Install GitHub Desktop.
[GitHub Desktop][gh_desktop_link] is a convenient app for working with GitHub
if you are not familiar with Git CLI.

  [gh_desktop_link]: https://desktop.github.com/


### Create a GitHub repository for the blog

- With GitHub Desktop, create a new repository for the blog website.
The repository name is going to be part of the URL. So please spend some time to
make it unique and easy to remember.

- Go to the [GitHub repository web page of this blog][gh_blog_link] and
follow `Code` --> `Download ZIP` to download the whole repository as a template.

  [gh_blog_link]: https://github.com/jacklinquan/quanlin

- Copy all the contents of the template to the folder of the new blog repository
and customise `LICENSE`, `mkdocs.yml`, `README.md`, `docs/index.md` and `docs/blog`.


### Preview the blog website on the local machine

It is always wise to preview the blog website before you publish it.

- Enter the Python virtual environment you created for building the blog and `cd` to
the folder of the blog repository where you can find the `mkdocs.yml` file.

- Install all the required packages.
``` powershell
pip install -r docs\requirements.txt
```

- Run the MkDocs server.
``` powershell
mkdocs serve
```

- In a web browser (e.g. Chrome) enter `http://127.0.0.1:8000/` and you should see
the blog website running on your local machine.

- Change the blog files or write your first "hello world" blog and save it. You can
find MkDocs server detecting the changes and reflecting the changes on the web page.

- When you are happy with the blog website, commit and push all the changes to GitHub.


### Publish the blog website

- Sign in with [RTD][rtd_link], and `Import a Project`. For the first time you will
need to link your RTD account with your GitHub account.

- Select the blog repository and follow the steps to set it up.

- After successfully building the website, you should see it work very soon.
If your repository name is unique enough, the URL of your blog website should look
like `[YOUR-REPO-NAME].readthedocs.io` or `[YOUR-REPO-NAME].rtfd.io`.

- Every time when you commit new blogs or make any change to the blogs, RTD will
rebuild the whole website and reflect the changes.


*[RTD]: Read the Docs
*[CLI]: Command Line Interface
*[URL]: Uniform Resource Locator
