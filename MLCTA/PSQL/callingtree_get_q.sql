select 
    * 
from callingtree 
where callingtree_path = %(path)s 
  and callingtree_filename = %(filename)s 
  and callingtree_callingtreetype_id = (
      select 
        callingtreetype_id 
      from callingtreetype 
      where callingtreetype_desc = %(itype)s        
  )
;