from enum import Enum

BucketVarsPerms = Enum('bucket_vars_perms', 'read-only editable')
BucketVarsType = Enum('bucket_vars_type', 'var verb noun')
# Is inanimate a gender? Full name? This is coming straight from a sql dump...
GendersGender = Enum('genders_gender', 'male female Androgynous inanimate full name')
