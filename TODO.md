# TODO

This is an idea dump — a checklist of features and improvements that come to mind to implement, in no particular order or priority.

## Ideas

- [/] Review enum and flag integer value generation — implement validations for min value, max value (based on base type), and auto-indexing correctness.
- [ ] Decorators are missing — decorators defined in CTD source shall be accessible on the resolved `Ctd` instances.
- [ ] Column and row must be traceable to any level of parsing — issues that appear during resolution (e.g. missing types, ambiguous references) should be traceable back to the exact file, line, and column that caused them.
- [ ] Keywords cannot be used in namespace path, and if used then namespace can have path element which then is resolved to none/empty and its valid but it shall not be valid
