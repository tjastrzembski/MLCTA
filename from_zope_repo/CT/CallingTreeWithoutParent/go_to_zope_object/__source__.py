context.layout_init()

id = context.REQUEST.get('id', None)

if id is None:
    context.layout_end()
    return

res = context.callingtree_get_q(id=id)
if len(res) == 0:
    context.layout_end()
    return    

url = '{path}/{filename}/manage_main'.format(
    path=res[0].callingtree_path,
    filename=res[0].callingtree_filename
)
context.layout_end(redirect=url)
