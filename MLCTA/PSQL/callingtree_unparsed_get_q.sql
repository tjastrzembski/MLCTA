select 
  callingtree_id as id,
  callingtree_path as path,
  callingtree_filename as filename,
  callingtreetype_desc as itype,
  callingtree_filemodded as modtime

from callingtree

join callingtreetype
  on callingtreetype_id = callingtree_callingtreetype_id
  
where callingtreetype_parseable is true
  and ( callingtree_fileparsed is null 
  or callingtree_fileparsed != callingtree_filemodded);