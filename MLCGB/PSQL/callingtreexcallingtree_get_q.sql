select     
 callingtreexcallingtree_parent_id as cxc_parent_id,  
 callingtreexcallingtree_child_id as cxc_child_id,    
 callingtreexcallingtree_acquisition as cxc_acquisition

from callingtreexcallingtree

where callingtreexcallingtree_parent_id = %(caller_id)s 
  and callingtreexcallingtree_child_id = %(called_id)s;
