select
  callingtree_path,
  callingtree_filename
  
from callingtree

where callingtree_id = <dtml-sqlvar id type="int">