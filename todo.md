todo

we need a way to evaluate .group_by(...).agg([...])

ok, got that! later: specialise evaluation of anything
which pandas has built-in way of doing
and maybe multiprocess too!

eventually:
- get rid of Scalar, that's just silly?
  or is it?
- keep it for now, who cares.
- but, need to generalise the definition of expression
- so that output is always sequence of series
- so, let's do...break now. see what needs doing
- then, try getting multi-output expressions?
- maybe, in 1 month, this is doable? 

if I can get this to work for pandas, then it should be fairly
straightforward to get it to run for cudf too?
then, that would rip. like, seriously, RIP.

so, when comparing two things...
well, now what?

how about: an expression should always evaluate to a 1-row column
in binary operations, handle broadcasting

does it make sense to sum one column to multiple others?
no, no way, lhs rule would invalidate

this is...kinda cool. kinda interesting! yeah, keep going, no matter
what, this will be quite cool.

so, I think the basics are there?
remove useless shit. only keep the bare minimum to run tpch?

---

fix filter with multiple conditions!

    dfx = dfx.filter(
        (plx.col("date") >= start_date) & (plx.col("date") <= end_date)
    )