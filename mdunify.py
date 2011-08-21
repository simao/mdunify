#!/usr/bin/env python2.7
#
# Simple script to produce a single unified beautiful HTML file from a
# Markdown file
#
# Time-stamp: <01:06:42 Sun 21-08-2011 obelix>

import sys
import logging
import codecs
from string import Template
import os
import StringIO
import argparse
import urllib
import mimetools
from BeautifulSoup import BeautifulSoup as bsoup

import markdown

DEFAULT_TEMPLATE_FILE = "template.tpl"


def convert_html_to_inline(html):
    """
    Parses an html document and substitutes img tags with inlined
    base64 encoded images

    Arguments:
    - `html`: An html, represented as a str object
    """
    soup = bsoup(html)

    for tag in soup.findAll('img'):
        new_tag = convert_imgtag_to_base64(unicode(tag))
        tag.replaceWith(new_tag)

    return soup


def convert_imgtag_to_base64(tag):
    """
    Returns an image tag with the URI substituted by a base64
    representation of the resource

    Arguments:
    - `tag`: A BeautifulSoup object representing an img tag
    """
    assert isinstance(tag, basestring)
    soup = bsoup(tag)
    tag = soup.contents[0]
    img_uri = tag['src']
    mime_type, data = get_image(img_uri)
    tag['src'] = "data:%s;base64,%s" % (mime_type, data)

    return tag


def get_image(uri):
    """
    Get image from uri and return a tuple containing the mime type of
    the image and a base64 representation of the image.

    Arguments:
    - `uri`: Uri for the image to fetch
    """
    log = logging.getLogger(__name__)
    log.info("Getting image from %s", uri)
    fd = urllib.urlopen(uri)
    mime_msg = fd.info()
    output = StringIO.StringIO()
    mimetools.encode(fd, output, 'base64')
    return (mime_msg.get('Content-Type'), output.getvalue())


def main():
    LOG_FORMAT = '[%(levelname).1s] [%(asctime)s] [%(name)s] %(message)s'
    logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)
    log = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(
        description='Prettify and Unify a markdown file.')
    parser.add_argument('-t', '--template', dest='template',
                        action='store',
                        help='Template file. Default is %s'
                        % DEFAULT_TEMPLATE_FILE)
    parser.add_argument('file', help='Path to the markdown file')
    parser.add_argument('-o', '--output', dest='output',
                        action='store',
                        help='Path to where the new file will be written. Existing files will be overwritten')
    parser.add_argument('--force', dest='force',
                        action='store_true',
                        default=False,
                        help='Force overwrite of output file.')
    parser.add_argument('--no-inline', '--ni', dest='inline',
                        action='store_false',
                        default=True,
                        help='Do not inline images using base64 encoding')

    args = parser.parse_args()

    if not args.template:
        script_dir = os.path.dirname(os.path.realpath(__file__))
        template_file = os.path.join(script_dir, DEFAULT_TEMPLATE_FILE)
    else:
        template_file = args.template

    if not os.path.exists(template_file):
        log.fatal("Could not find template file %s", template_file)
        sys.exit(-1)

    if not args.output:
        output_file = args.file + ".html"
    else:
        output_file = args.output

    if os.path.exists(output_file) and not args.force:
        log.fatal("Error: Could not save file. %s already exists and force was not used" % output_file)
        sys.exit(-1)
                
    with codecs.open(template_file, 'r', encoding='utf-8') as fd:
        template = Template(fd.read())

    parsed_md = StringIO.StringIO()

    markdown.markdownFromFile(input=args.file,
                          output=parsed_md,
                          encoding="utf8")

    parsed_md = parsed_md.getvalue().decode('utf8')

    if args.inline:
        parsed_md = convert_html_to_inline(parsed_md)

    with codecs.open(output_file, 'w', encoding='utf-8') as fd:
        log.info("Saving output file to %s", output_file)

        contents = template.substitute({
                "markdown_content": unicode(parsed_md)
                })
        fd.write(contents)

    log.info("Done.")

if __name__ == "__main__":
    main()
