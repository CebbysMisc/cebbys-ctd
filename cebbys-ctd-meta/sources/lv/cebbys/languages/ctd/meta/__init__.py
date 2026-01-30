"""Meta Loader Package

This package contains metadata types and the loader for CTD files.
"""
from lv.cebbys.languages.ctd.meta.visitor import MetaVisitor as CtdMetaVisitor
from lv.cebbys.languages.ctd.meta.loader import MetaLoader as CtdMetaLoader
from lv.cebbys.languages.ctd.meta.parser import MetaParser

# Aliases for convenience
MetaVisitor = CtdMetaVisitor
MetaLoader = CtdMetaLoader

__all__ = [
    'CtdMetaVisitor',
    'CtdMetaLoader',
    'MetaVisitor',
    'MetaLoader',
    'MetaParser',
]
