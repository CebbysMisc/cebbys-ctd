"""CTD Meta API

This module contains common types for metadata classes.
"""
import lv.cebbys.languages.ctd.__api__ as Api

__all__ = ['ModulePath']

# Re-export ModulePath for use in meta classes
ModulePath = Api.ModulePath
