# coding: utf-8
from typing import TypeVar, List, Tuple,TYPE_CHECKING

if TYPE_CHECKING:
  from django.template import Template

__author__ = '代码会说话'

TemplateParamType = TypeVar("TemplateParamType",Template,str,List[str],Tuple[str])
