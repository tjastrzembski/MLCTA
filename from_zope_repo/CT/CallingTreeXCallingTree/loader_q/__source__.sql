select
 callingtreexcallingtree_author as author,
 fmt_datetime(callingtreexcallingtree_modtime) as modtime,
 
 
 (select name from callingtree_sel where id = callingtreexcallingtree_parent_id) as parent_name,
 callingtreexcallingtree_parent_id as parent_id,
 (select name from callingtree_sel where id = callingtreexcallingtree_child_id) as child_name,
 callingtreexcallingtree_child_id as child_id,
 callingtreexcallingtree_acquisition as acquisition

from
 callingtreexcallingtree
 

<dtml-sqlgroup where>
 callingtreexcallingtree_id = <dtml-sqlvar id type="int">::bigint  
<dtml-and>
 <dtml-var expr="db_selfilter_sql('callingtreexcallingtree', 'callingtreexcallingtree_id')">
</dtml-sqlgroup>
