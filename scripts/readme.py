#!/usr/bin/env python3
# coding=utf8
"""toc.py

Generate README.md File.
"""
from __future__ import absolute_import, print_function, unicode_literals

import logging
import re

LOGGER = logging.getLogger(__name__)


def has_non_empty_values(obj, *attrs):
  """Check for empty values.

  Args:
    obj (dict): object to get values from.
    attrs (str): attributes to check for emptiness.

  Returns:
    bool: True if `parsed_values` has empty values otherwise False.
  """
  return all(map(obj.get, attrs))


def has_empty_values(obj, *attrs):
  """Check for empty values.

  Args:
    obj (dict): object to get values from.
    attrs (str): attributes to check for emptiness.

  Returns:
    bool: True if `parsed_values` has empty values otherwise False.
  """
  return not has_non_empty_values(obj, *attrs)


def _title(val, min_len=4):
  return val.upper() if len(val) <= min_len else val.title()


def _split_join_title(val, sep, joiner=" ", maxsplit=-1):
  return joiner.join(map(_title, val.split(sep, maxsplit)))


def _splitn(val, *sep, maxsplit=0, flags=0):
  pattern = r"{0}".format("|".join(sep))
  parts = re.split(
      pattern, val,
      maxsplit=maxsplit,
      flags=flags
  )
  return tuple(filter(None, parts))


def _splitn_join(val, *sep, func=None, joiner=" ", maxsplit=0, flags=0):
  parts = _splitn(
      val, *sep,
      maxsplit=maxsplit,
      flags=flags
  )
  if func is None:
    return joiner.join(parts)
  return joiner.join(map(func, parts))


def main():
  """CLI Entry Point.

  Returns:
    int: 0 if success otherwise 1.
  """
  import os

  _SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
  _ROOT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
  _EXCLUSIONS = ("venv", os.path.basename(_SCRIPT_DIR))

  def _markdown_file_ref(_text, _filepath):
    return "[{0}]({1})".format(_text, _filepath.replace(_ROOT_DIR, "."))

  def _not_startswith_dot(val):
    return not val.startswith(".")

  def _not_in_exclusions(val):
    return val not in _EXCLUSIONS

  def _root_dir_join(val):
    return os.path.join(_ROOT_DIR, val)

  def _is_directory(val):
    return os.path.isdir(_root_dir_join(val))

  def _directory_title(val):
    return _title(os.path.basename(val))

  # list directories

  dirlist = os.listdir(_ROOT_DIR)

  # filter out

  dirlist = filter(_is_directory, dirlist)
  dirlist = filter(_not_startswith_dot, dirlist)
  dirlist = filter(_not_in_exclusions, dirlist)

  # expand/join

  dirlist = map(_root_dir_join, dirlist)

  # generate table of contents from file names

  results = []

  for dirpath in dirlist:
    section = {}

    section_name = section.setdefault("name", _directory_title(dirpath))
    section_topic_links = section.setdefault("topics", [])  # noqa

    for filename in os.listdir(dirpath):
      filepath = os.path.join(dirpath, filename)

      file_basename, file_ext = os.path.splitext(filename)
      if file_ext.lower() != ".md":
        LOGGER.debug("skipping non-markdown file: %s", file_ext)
        continue

      if file_basename.lower() == "readme":
        section["link"] = _markdown_file_ref(section_name, filepath)
        continue

      section_topic_title = _split_join_title(file_basename, "_")
      section_topic_link = _markdown_file_ref(section_topic_title, filepath)

      section_topic_links.append(section_topic_link)

    section_topic_links.sort()

    results.append(section)

  def _get_name(obj):
    return obj["name"]

  results.sort(key=_get_name)

  with open(_root_dir_join("README.md"), "w+") as fd:
    fd.write("# Cloud Docs\n\n")

    fd.write("Cloud Documentation and Notes Repository\n\n")
    fd.write("<hr>\n\n")

    for section in results:
      fd.write("- {0}\n\n".format(section.get("link", section["name"])))

      for topic in section["topics"]:
        fd.write("    - {0}\n".format(topic))

      fd.write("\n<hr>\n\n")
  return 0


if __name__ == '__main__':
  import sys

  sys.exit(main())
