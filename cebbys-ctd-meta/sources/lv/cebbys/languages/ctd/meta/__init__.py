"""Meta Loader Package

This package contains metadata types and the visitor for CTD files.
"""
from lv.cebbys.languages.ctd.meta.visitor import MetaVisitor as CtdMetaVisitor

# Alias for convenience
MetaVisitor = CtdMetaVisitor

__all__ = [
    'CtdMetaVisitor',
    'MetaVisitor',
]
