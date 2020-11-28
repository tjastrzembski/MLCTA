res0 = context.called_method()
res1 = context.B.called_method()
res2 = context.B.BB.A.called_method()

return [res0, res1, res2]
