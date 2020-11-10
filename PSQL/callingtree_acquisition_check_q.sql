select exists(
select *  
from callingtree 

join callingtreexcallingtree
  on callingtreexcallingtree_child_id = callingtree_id
 
where callingtree_id = %(caller_id)s 
  and %(acquisition_path)s = any(callingtreexcallingtree_acquisition)
) as already_checked;
