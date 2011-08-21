# Markdown Unify #
## Purpose ##

Produce a single unified and beautiful HTML document from a Markdown
file.

A standard markdown compiler produces raw HTML with no stylesheets
attached, which is usually pretty ugly. Any images linked from the
markdown file would also be linked from the generated HTML file and
you need to attach them along with the html file if you want to send
the file to someone.

**mdunify** is a very simple script to compile your markdown files and
produce a single HTML file with any images included in that HTML file.

The generated file will contain some CSS so that the appearance of the
document is somewhat beautiful. Currently, these stylesheets include
sensible typography defaults from the [blueprint-css][blue] project.

## Examples ##

Files `README.md.html` and `example/example.md.html` included in this
repository were generated using **mdunify**.

## Install and dependencies ##

After installing the following dependencies using `pip` or
`easy_install`, you can simply clone this repository and run 
`python mdunify.py`.

You need the following packages installed:

- [markdown][pymarkdown] - You can easily install this package using
  `pip install markdown`
- argparse - **You don't need this library if your are using python >= 2.7**.
  You can install argparse using `pip install argparse`

mdunify also depends on [BeautifulSoup][bsoup], which is already
included. The generated HTML files include stylesheets from the
[blueprint-css][blue] project.

## Run ##
### Convert a file ###

To convert a file you can use the following command:

   	   python mdunify.py file.md

This will generate a file named file.md.html

You can obtain a summary of the options available with
`python mdunify.py --help`.

To disable image in-lining you can use `--noinline`.

### Adjust the template ###

You can easily adjust the template used by mdunify:

1. Copy the `template.tpl` file to the same dir as your markdown file
2. Edit the `*.tpl` file according to your needs
3. Run mdunify with `python file.md -t template.tpl`



[blue]: http://www.blueprintcss.org/
[pymarkdown]: http://www.freewisdom.org/projects/python-markdown/
[bsoup]: http://www.crummy.com/software/BeautifulSoup/
