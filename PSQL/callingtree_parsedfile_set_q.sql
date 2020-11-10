update callingtree 
set 
  callingtree_author = 'perfact',
  callingtree_modtime = now(),
  callingtree_fileparsed = %(modtime)s,
  callingtree_functionlist = %(functionlist)s
where callingtree_path = %(path)s
  and callingtree_filename= %(filename)s;
