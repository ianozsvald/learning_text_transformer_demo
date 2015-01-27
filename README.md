# learning_text_transformer_demo
Demo code for http://annotate.io/ which is a "self-learning text transformer".

This project learns a mapping from "data you have" to "data you want" from a set of examples you provide, you can then send in new data that gets cleaned according to the rules that were learned.

Status: prototype (the example works and you can post your own simple examples)

Getting started
---------------

You need Python 2.7 or 3.4 along with the `requests` module. You can install `requests` using:

    $ pip install requests

To run the demo:

    $ python annotateio_demo.py
    <it'll explain all of its steps>

This demo is self-contained, it needs a connection to the internet, it posts the examples that are contained in the file, no other data (nothing from your machine) is sent.

More information
----------------

A write-up of some of the goals is available here:
 * http://ianozsvald.com/2015/01/10/a-first-approach-to-automatic-text-data-cleaning/
 * http://ianozsvald.com/2015/01/27/annotate-io-self-learning-text-cleaner-demo-online/
