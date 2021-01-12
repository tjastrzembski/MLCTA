insert into callingtree (
 callingtree_author,
 callingtree_path,
 callingtree_filename,
 callingtree_callingtreetype_id,
 callingtree_filemodded,
 callingtree_scanned
 )
select  
    'perfact',
    %(path)s,
    %(filename)s,
    callingtreetype_id,
     to_timestamp(%(file_modded)s),
    true 
     
from callingtreetype 
where callingtreetype_desc = %(itype)s 

on conflict (callingtree_path, callingtree_filename) do update 
set  
  callingtree_author = 'perfact',
  callingtree_modtime = now(),
  callingtree_filemodded =  to_timestamp(%(file_modded)s),
  callingtree_scanned = true 

where callingtree.callingtree_filename = %(filename)s 
  and callingtree.callingtree_path = %(path)s;