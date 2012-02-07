#!/usr/bin/python

import sys, string
from xml.sax import handler, make_parser, saxutils

reload(sys)
sys.setdefaultencoding('utf-8')

class ContentGenerator(handler.ContentHandler):

  def __init__(self, out = sys.stdout):
    handler.ContentHandler.__init__(self)
    self._out = out

  def startDocument(self):
    self._out.write('<?xml version="1.0" encoding="utf-8"?>\n')

  def startElement(self, name, attrs):
    self._out.write('<' + name)
    for (name, value) in attrs.items():
      self._out.write(' %s="%s"' % (name, saxutils.escape(value)))
    self._out.write('>')

  def endElement(self, name):
    self._out.write('</%s>' % name)

  def characters(self, content):
    self._out.write(saxutils.escape(content).strip())

  def ignorableWhitespace(self, content):
    self._out.write(content)
      
  def processingInstruction(self, target, data):
    self._out.write('<?%s %s?>' % (target, data))


def test(inFileName):
  outFile = sys.stdout
  parser = make_parser()
  parser.setContentHandler(ContentGenerator(outFile))
  parser.parse(inFileName)

def main():
  args = sys.argv[1:]
  if len(args) != 1:
    print 'usage: python trimxml.py infile.xml'
    sys.exit(-1)
  test(args[0])

if __name__ == '__main__':
  main()
