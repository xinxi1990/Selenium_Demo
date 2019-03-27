#!/usr/bin/env python
# -*- coding: utf-8 -*-


def test_person(yaml_output):
    print("Test for %s" % yaml_output['test'])
    for person in yaml_output['persons']:
        assert person['age'] == 20, "I am %s" % person['name']