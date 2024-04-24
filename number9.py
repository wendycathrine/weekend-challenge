#!/usr/bin/env python

def concatenate_strings(*args, sep=" "):
    """
    This fnction concatenates strings that have been passed to it
    """
    return sep.join(args)

print(concatenate_strings("Woman","in","STEM"))    