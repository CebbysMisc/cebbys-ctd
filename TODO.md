# TODO

This is an idea dump — a checklist of features and improvements that come to mind to implement, in no particular order or priority.

## Ideas

- [x] Review enum and flag integer value generation — implement validations for min value, max value (based on base type), and auto-indexing correctness.
- [ ] Decorators are missing — decorators defined in CTD source shall be accessible on the resolved `Ctd` instances.
- [ ] Column and row must be traceable to any level of parsing — issues that appear during resolution (e.g. missing types, ambiguous references) should be traceable back to the exact file, line, and column that caused them.
- [ ] Aliases are mock instances of a type after resolution these aliases shall be replaced by the aliased type, I have to plan how to perform this in the best manner possible without writing strange replacement code iterating over all datatypes again. I am thinking of implementing mock behavior for the aliased type or updating the Ctd types to have their properties to refer to the type by key, rather than having instance, thus I can then update the value in database when alias is resolved and then I will not need to modify the types again
- [ ] Add support for decorators to have dict and list types as arguments, and named arguments
