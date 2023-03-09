#encoding:utf-8
import sys
import os
projectPath = os.path.abspath(os.path.join(os.getcwd()))
sys.path.append(projectPath)
from apps.admin.models import Articles
