import sys
import unittest

try:
    import markbit
except:
    sys.path.append(".")
    import markbit
from BeautifulSoup import BeautifulSoup as bsoup

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.encoded_image = u"""iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAABGdBTUEAALGPC/xhBQAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB9YGARc5KB0XV+IA
AAAddEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIFRoZSBHSU1Q72QlbgAAAF1JREFUGNO9zL0NglAAxPEfdLTs4BZM4DIO4C7OwQg2JoQ9LE1exdlYvBBeZ7jqch9//q1uH4TLzw4d6+ErXMMcXuHWxId3KOETnnXXV6MJpcq2MLaI97CER3N0vr4MkhoXe0rZigAAAABJRU5ErkJggg==""".replace('\n', '')

    def test_tag_parse(self):
        tag = """<img src="tests/img.png" />"""
        expected = """<img src="data:image/png;base64,%s" />""" % (self.encoded_image)
        self.assertEquals(expected, unicode(markbit.convert_imgtag_to_base64(tag)).replace('\n',''))

    def test_parse_html_document(self):
        as_html = """<html><body><div><img src="tests/img.png"/></div></body></html>"""
        expected = """<html><body><div><img src="data:image/png;base64,%s" /></div></body></html>""" % (self.encoded_image)

        self.assertEquals(expected, unicode(markbit.convert_html_to_inline(as_html)).replace('\n',''))
        


    def test_img_fetch(self):
        mime_type, content = markbit.get_image("tests/img.png")

        self.assertEquals("image/png", mime_type)
        self.assertEquals(self.encoded_image, content.replace('\n', ''))
        
        
if __name__ == '__main__':
    unittest.main()
