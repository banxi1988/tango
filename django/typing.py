# coding: utf-8
from typing import Optional, Union, Any, Dict, Collection

__author__ = '代码会说话'
Opt = Optional
OptInt = Union[int,None]
OptFloat = Union[float,None]
OptStr = Union[str,None]
OptBool = Union[bool, None]
OptType = Union[type,None]
OptDict = Union[dict,None]
StrDict = Dict[str,Any]
OptStrDict = Union[Dict[str,Any],None]
Strs = Collection[str]
OptStrs = Union[Collection[str],None]

Str1N = Union[str,Strs]
