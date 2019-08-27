#!flask/bin/python
# imp module deprecated since version 3.4.
# imp.new_model had been replaced with "importlib.util.module_from_spec()".
#import imp
import types
import importlib
from migrate.versioning import api
from app import db
from config import SQLALCHEMY_DATABASE_URI
from config import  SQLALCHEMY_MIGRATE_REPO

v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
migration = SQLALCHEMY_MIGRATE_REPO + ('/version/%03d_migration.py' % (v+1))
tmp_module = types.ModuleType('old_model')
old_module = api.create_model(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
exec(old_module, tmp_module.__dict__)
script = api.make_update_script_for_model(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, tmp_module.meta, db.metadata)
open(migration, 'wt').write(script)
api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
print('New migraiton saved as ' + migration)
print('Current database version: ' + str(v))