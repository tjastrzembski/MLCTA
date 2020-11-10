select 
  callingtree_id as id,
  callingtree_path as path,
  callingtree_filename as filename,
  (select 
    callingtreetype_desc 
   from callingtreetype  
   where callingtreetype_id = callingtree_callingtreetype_id) as itype,
  callingtree_filemodded as modtime 

from callingtree
where callingtree_fileparsed is null 
  or callingtree_fileparsed != callingtree_filemodded;