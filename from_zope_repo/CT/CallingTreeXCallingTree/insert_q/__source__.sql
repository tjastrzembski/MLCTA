insert into callingtreexcallingtree (
 callingtreexcallingtree_author,
 
 callingtreexcallingtree_parent_id,
 callingtreexcallingtree_child_id,
 callingtreexcallingtree_acquisition
) values (
 <dtml-sqlvar expr="aq_inner.username()" type="string">,
 
 <dtml-var expr="sql_int(parent_id)">,
 <dtml-var expr="sql_int(child_id)">,
 <dtml-var expr="sql_string(acquisition)">
) returning callingtreexcallingtree_id
