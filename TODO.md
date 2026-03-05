# TODO

This is an idea dump — a checklist of features and improvements that come to mind to implement, in no particular order or priority.

## Ideas

- [ ] Column and row must be traceable to any level of parsing — issues that appear during resolution (e.g. missing types, ambiguous references) should be traceable back to the exact file, line, and column that caused them.
- [ ] Decorators are missing — decorators defined in CTD source shall be accessible on the resolved `Ctd` instances.
