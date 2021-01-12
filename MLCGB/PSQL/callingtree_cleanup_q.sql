delete from callingtree 
where  callingtree_path ~ %(path)s
  and  callingtree_scanned = false;