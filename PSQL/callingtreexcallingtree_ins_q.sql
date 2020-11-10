insert into callingtreexcallingtree (     
 callingtreexcallingtree_author,      
 callingtreexcallingtree_parent_id,   
 callingtreexcallingtree_child_id,    
 callingtreexcallingtree_acquisition
)  values (
  'perfact',
   %(caller_id)s,
   %(called_id)s,
   %(acquisition_path)s  
) 
on conflict (callingtreexcallingtree_parent_id, callingtreexcallingtree_child_id) 
do update set  
  callingtreexcallingtree_author = 'perfact',
  callingtreexcallingtree_modtime = now(),
  callingtreexcallingtree_acquisition =  %(acquisition_path)s
 
where callingtreexcallingtree.callingtreexcallingtree_parent_id = %(caller_id)s 
  and callingtreexcallingtree.callingtreexcallingtree_child_id = %(called_id)s;
