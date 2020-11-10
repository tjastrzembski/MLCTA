select distinct
  callingtree_id,
  callingtree_filename,
  callingtree_path,
  callingtreexcallingtree_acquisition

from callingtree 

join callingtreexcallingtree
  on callingtreexcallingtree_child_id = callingtree_id

where callingtreexcallingtree_scanned;