"""Meta Loader Package

This package contains metadata types and the visitor for CTD files.
"""
from lv.cebbys.languages.ctd.meta.visitor import MetaVisitor

# Alias for convenience
CtdMetaVisitor = MetaVisitor

__all__ = [
    'CtdMetaVisitor',
    'MetaVisitor',
]
