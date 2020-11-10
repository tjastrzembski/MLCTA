res = context.actual_datetime_get_q()
assert len(res) == 1
return 'HELLO WORLD! It\'s {now}'.format(
    now=res[0].actual_datetime
)
